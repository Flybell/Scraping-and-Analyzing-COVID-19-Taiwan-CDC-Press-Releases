"""Script: process file data"""

import re #regular expression
import io #for UTF8 processing
from bs4 import BeautifulSoup #HTML parser library
import glob #to create file name from variable

#import functions
from Parse_File import get_date, case_num

num = 0

#extract data from press releases
with open("daily_new_cases.txt", "w+") as file:
    file.write("Date" + 7*" " + "New Cases\n")
    for name in glob.glob('[0-9][0-9][0-9][0-9]-[0-9][0-9]*.txt'):
        number = case_num(name)
        if number:
            file.write(f"{get_date(name):{10}} {number}\n")
            num = num + int(number)
            
print("Created new file of daily new cases.")
print(f"Total number of cases: {num}")
