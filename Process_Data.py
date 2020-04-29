"""Script: process file data"""

import re #regular expression
import io #for UTF8 processing
from bs4 import BeautifulSoup #HTML parser library
import glob #to create file name from variable

#import functions
from Parse_File import get_date, case_num
from Scrape_Web import get_info, create_file, get_url

#extract data from press releases
with open("daily_new_cases.txt", "w+") as file:
    file.write("Date" + 7*" " + "New Cases\n")
    for name in glob.glob('[0-9][0-9][0-9][0-9]-[0-9][0-9]*.txt'):
        file.write(f"{get_date(name):{10}} {case_num(name)}\n")
