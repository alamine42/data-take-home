from __future__ import print_function

import datetime
import os
import json
import argparse
import csv
import logging

from datetime import date
from dateutil.parser import parse

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

STATES = {}

FIELDS = [
	'city', 'name', 'bio', 'job', 'gender', 
	'zipcode', 'birthdate', 'start_date', 'start_date_description',
	'state', 'address', 'email'
	]

def read_data(path):
	"""
	Function to read data from CSV file
	"""
	with open(path, 'r') as f:
		reader = csv.DictReader(f)
		for row in reader:
			yield(row)

def normalize_bio(raw_bio):
	"""
	Normalize bio values to a space-delimited string.
	"""
	raw_bio = raw_bio.replace('\n', ' ').replace('\t', ' ')
	return ' '.join(raw_bio.split())

def add_to_state_dict(state_dict):
	"""
	Takes a dict of the form {'state_abbr': 'AL', 'state_name': 'Alabama'} and
	converts it to an entry of the form {'AL': 'Alabama'} to be added to the 
	global state dict
	"""
	global STATES
	if state_dict['state_abbr'] not in STATES:
		STATES[state_dict['state_abbr']] = state_dict['state_name']


def main(data_path, state_path, output_path):

	# Build a dictionary of the form {'state_abbr': 'state_name'} for easier
	# replacement in the next step
	for state in read_data(state_path):
		add_to_state_dict(state)

	with open(output_path, 'w') as f_out:
		
		writer = csv.DictWriter(f_out, fieldnames=FIELDS)
		writer.writeheader()

		for idx, row in enumerate(read_data(data_path)):
			row['bio'] = normalize_bio(row['bio'])
			row['state'] = STATES[row['state']]
			try:
				start_date = parse(row['start_date'])
				row['start_date'] = start_date.strftime('%Y-%m-%d')
			except ValueError:
				row['start_date'] = ''
				row['start_date_description'] = row['start_date']

			writer.writerow(row)


if __name__ == '__main__':
	
	parser = argparse.ArgumentParser(description='Enigma\'s super duper CSV reader')
	parser.add_argument('-d', '--data', action='store', dest='data_path', default='data.csv',
		help='Specify the path to the CSV file')
	parser.add_argument('-s', '--states', action='store', dest='state_path', default='state_abbreviations.csv',
		help='Specify the path to the state abbreviations file')
	parser.add_argument('-o', '--output', action='store', dest='output_path', default='enriched.csv',
		help='Specify the path to the enriched output file')
	my_args = parser.parse_args()

	main(
		data_path=my_args.data_path,
		state_path=my_args.state_path,
		output_path=my_args.output_path
	)
