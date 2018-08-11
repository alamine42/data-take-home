# Data Take Home Exercises - Mehdi's Solutions

Both scripts are in Python 2. See additional notes below for each.

One thing to point out is that the `edgar` code did not have a requirements.txt, which I added. As part of that move, I also replaced the Flask pagination module to make things work.

## Web Scraper

To run it:
```
python web_scraper.py
```
This will look for the Edgar site on `http://localhost:5000/companies` and will the write the JSON output to `edgar_companies.json` in the same directory.

For usage options:
```
python web_scraper.py -h
```

## CSV Reader

To run it:
```
python csv_reader.py
```
This will look for `data.csv` and `state_abbreviations.csv` in the same directory. It will output `enriched.csv` in the same directory. 

For usage options:
```
python csv_reader.h -h
```

Obviously, if you've just cloned this repo, running it with the default options won't work. You should try this:
```
python csv_reader.py -d ../files/data.csv -s ../files/state_abbreviations.csv
```

I'd like to thank Stack Overflow for saving the lives of engineers and developers everywhere.

