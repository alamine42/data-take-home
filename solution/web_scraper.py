from __future__ import print_function

import datetime
import requests
import json
import math
import argparse
import logging

from bs4 import BeautifulSoup

COMPANY_MASTER_LIST = []

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def get_html(url):
	"""
	Retrieves page source for a url
	"""
	response = requests.get(url)
	if response.status_code == 200:
		return response.text
	else:
		raise Exception('There was a problem retrieving the HTML from the URL provided. \
			Please try with a different URL.')

def parse_company_table_html(pagination_soup_html):
	"""
	Gets a beautiful soup object that represents the company list table in HTML 
	and extracts the list of companies from it
	"""
	data = []
	for row in pagination_soup_html:
		cols = row.find_all('td')
		cols = [ele.text.strip() for ele in cols]
		data.append({'id': cols[0], 'company': cols[1]})

	return data

def parse_pagination_info_html(table_soup_html):
	"""
	Gets a beautiful soup object that represents the pagination info in HTML 
	and extracts the total number of companies and the number of companies shown per page
	"""
	total_companies = 0
	companies_per_page = 0
	bolded_info = table_soup_html.find_all('b')

	try:
		companies_per_page = int(bolded_info[0].text.split('-')[1].strip())
		total_companies = int(bolded_info[1].text.strip())
	except Exception:
		print('Could not extract number of companies')

	return (total_companies, companies_per_page)

def main(edgar_url, json_path):

	main_page_html = get_html(edgar_url)
	main_soup = BeautifulSoup(main_page_html, 'html.parser')
	
	# First, figure out how many companies per page and how many total companies there are
	pagination_info_html = main_soup.find('div', attrs={'class':'pagination-page-info'})
	total_companies, companies_per_page = parse_pagination_info_html(pagination_info_html)
	
	# Figure out number of pages
	total_pages = int(math.ceil(float(total_companies) / float(companies_per_page)))
	
	# Now loop through all the pages and fetch the companies
	for i in range(1, total_pages+1):
		# Form the correct url
		url_to_fetch = edgar_url + '?page=' + str(i)
		# Get a beautiful soup object
		main_soup = BeautifulSoup(get_html(url_to_fetch), 'html.parser')
		# Extract the table html from the DOM
		company_rows_html = main_soup.find('table', attrs={'class':'table-hover'}).find('tbody').find_all('tr')
		# Get the table html parsed and build the list of companies
		COMPANY_MASTER_LIST.append(parse_company_table_html(company_rows_html))
	
	with open(json_path, 'w') as outfile:
		json.dump(COMPANY_MASTER_LIST, outfile)

if __name__ == '__main__':
	
	parser = argparse.ArgumentParser(description='Enigma\'s super duper web scraper')
	parser.add_argument('-u', '--url', action='store', dest='edgar_url', default='http://localhost:5000/companies/',
		help='Specify the URL to /companies web page')
	parser.add_argument('-j', '--json', action='store', dest='json_path', default='edgar_companies.json',
		help='Specify the path to the output JSON file')
	my_args = parser.parse_args()

	main(
		edgar_url=my_args.edgar_url,
		json_path=my_args.json_path
	)