# Data Take Home Exercises

Thank you for taking the time to attempt these exercises. We're sincerely thankful for your time in attempting these. 
We estimate depending on your skill level these exercises to take between 30 minutes to 2 hours. If you find yourself
taking more than 2 hours, you may be over-engineering the solution, consider taking an easier option.

## Instructions

Please create a fork of this repository. Create a folder named `solution` and place your responses here. When ready please notify
your coordinator to take a look.

### Structure

[edgar](edgar) - company listing site. To start the web application review the readme in the folder

[files](files) - csv files

## Questions

### Web Scrape

Write a script to scrape a sample site and output its data in JSON.

edgar is a company listings site containing ten pages of company links. Each link endpoint holds company-specific data such 
as name, description and address. The sole requirement of this part of the test is to produce JSON of all of the company 
listings data for the site.

Please commit a "edgar.json" file of the parsed company listings data along with your solution code in the `solution/edgar` folder.
Please include a `requirements.txt` file if necessary

#### Recommended libraries: 

[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) contains a robust HTML parser.

Python's [json](https://docs.python.org/2/library/json.html) module is convenient for [JSON](http://json.org) format. 

### Data Prep

Write a script to transform input CSV to desired output CSV. 

You will find a CSV file in the files folder under [data.csv](files/data.csv). There are two steps (plus an optional bonus - Date offset) to this part of the test. Each step concerns manipulating the values for a single field according to the step's requirements. The steps are as follows:

**String cleaning** - The bio field contains text with arbitrary padding, spacing and line breaks. Normalize these values to a space-delimited string.

**Code swap** - There is a supplementary CSV in the files folder under [state_abbreviations.csv](files/state_abbreviations.csv). This "data dictionary" contains state abbreviations alongside state names. For the state field of the input CSV, replace each state abbreviation with its associated state name from the data dictionary.

**Date offset** - The start_date field contains data in a variety of formats. These may include e.g., "June 23, 1912" or "5/11/1930" (month, day, year). But not all values are valid dates. Invalid dates may include e.g., "June 2018", "3/06" (incomplete dates) or even arbitrary natural language. Add a start_date_description field adjacent to the start_date column to filter invalid date values into. Normalize all valid date values in start_date to ISO 8601 (i.e., YYYY-MM-DD).

Your script should take [data.csv](files/data.csv) as input and produce a cleansed "enriched.csv" file according to the step requirements above. 

Please commit a "enriched.csv" file along with your solution code in the `solution/csv` folder.

Recommended libraries:

Python's [csv](https://docs.python.org/2/library/csv.html) module is standard for dealing with CSV data.

