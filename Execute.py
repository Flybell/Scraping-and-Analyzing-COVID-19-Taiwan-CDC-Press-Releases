"""The main script"""


import re #regular expression
import io #for UTF8 processing
from bs4 import BeautifulSoup #HTML parser library
import glob #to create file name from variable

#import functions
from Scrape_Web import *

#search for COVID-19 related press releases on the Taiwan CDC website
#since a particular date
#with a particular set of search terms
first_url = create_url(1, "2020.01.01", "新增 確診")

#iterate through all search pages to create
#a list of URLs of COVID-10 related press releases
url_list = []
next_url = first_url
while next_url:
    soup = make_request(next_url)
    url_list.extend(get_url(soup))
    next_url = find_next_page(soup)

#create URLS.txt file (list of urls) for future reference
write_url(url_list)

#create files from list of urls for future data analysis
for url in url_list:
  date, title, text = get_info(url)
  create_file(date, title, text)
