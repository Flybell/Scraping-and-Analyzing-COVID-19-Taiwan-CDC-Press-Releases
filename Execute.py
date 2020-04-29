import re #regular expression
import io #for UTF8 processing
from bs4 import BeautifulSoup #HTML parser library
import glob #to create file name from variable

#import functions
from Parse_File import get_date, case_num
from Scrape_Web import get_info, create_file, get_url

#generate a list web pages that satisfy
#search term "新增 確診" starting Jan 1, 2020
page_urls = []
part_1 = "https://www.cdc.gov.tw/Bulletin/List/MmgtpeidAR5Ooai4-fgHzQ?page="
part_3 = "&startTime=2020.01.01&keyword=%27%E6%96%B0%E5%A2%9E%20%E7%A2%BA%E8%A8%BA%27"
for n in range(1, 25): #known: a total of 24 pages
    page_urls.append(part_1 + str(n) + part_3)

#generate a list of press release urls from
#the web pages and write them into "URLS.txt"
for page in page_urls:
    url_list = get_url(page)
    with open("URLS.txt", "a+") as url_file:
        for url in url_list:
            url_file.write(url+"\n")

#from the URLS.txt file, create individual text files
#for each press release
with open("URLS.txt", "r+") as url_file:
    url_list = url_file.readlines()
for url in url_list:
   date, title, text = get_info(url)
   create_file(date, title, text)
