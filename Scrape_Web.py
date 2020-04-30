"""Methods: scrape press releases from web and store in  text files"""

import re #regular expression
from bs4 import BeautifulSoup #web parsing library
import io
#----make requests as a browser-----#
import requests
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
#----------------------------------#

def create_url(page_num, start_time, end_time, search_term):
    """creates an url from page number, time stamp, and search terms"""
    """timestamp format: \d\d\d\d.\d\d.\d\d""" #2020.01.01 #新增 確診
    base="https://www.cdc.gov.tw/Bulletin/List/MmgtpeidAR5Ooai4-fgHzQ"
    url = base + "?page=" + str(page_num) + "&startTime=" + str(start_time) + "&endTime=" + str(end_time) + "&keyword=" + str(search_term)
    return url

def make_request(url):
    """request HTML from url with beautiful soup"""
    req = requests.get(url, headers)
    soup = BeautifulSoup (req.content, "html5lib")
    return soup

def find_next_page(soup):
    """returns url of next page"""
    base = "https://www.cdc.gov.tw"
    next_page = soup.find_all("a", rel="next", text="下一頁")
    if next_page:
        next_url = base + next_page[0]["href"]
        return next_url
    else:
        None

def get_url(soup):
    """ find all the COVID-19 related press releases on the page"""
    """criteria: any(s in a["title"] for s in ('新增', '確診', '肺炎')"""
    url_list = []
    for a in soup.find_all('a', {"href": re.compile("typeid=9$")}):
        if any(s in a["title"] for s in ('新增', '確診', '肺炎')):
            url = "https://www.cdc.gov.tw" + a['href']
            url_list.append(url)
    return url_list

def write_url(url_list):
    """create URLS.txt file of press release url"""
    with open("URLS.txt", "a+") as url_file:
        for url in url_list:
            url_file.write(url+"\n")

def read_urls(file):
    """get list of urls from file"""
    with open(file, "r+") as url_file:
        url_list = url_file.readlines()
    return url_list

def get_info(url):
    """get press release date, title, and text from press release url"""
    soup = make_request(url)

    #get press release title
    title_text = soup.find("h2", "con-title").text.strip()
    title = title_text.partition('\n')[0]

    #get press release content and date
    div = soup.find_all("div") #find div tags
    for ele in div:
        for div2 in ele("div","text-right"):
            if "發佈日期" in div2.text:
                text = ele.text
                date = re.findall("\d\d\d\d-\d\d-\d\d", div2.text)[0]
                break #prevents reiterating upwards to all div parents
    return date, title, text

def create_file(date, title, text, n):
    """create new text files, one for each press release"""
    """with date as file name and text as content"""
    filename = "%s_%s.txt" % (date, n)
    with io.open(filename, "w+", encoding="UTF8") as newfile:
        text = text.replace(" ", "") #remove all spaces
        sentences= re.sub("，|。", "\n", text) #one sentence per line
        newfile.write(title+"\n")
        newfile.write(date+"\n")
        newfile.write(sentences)
        print(filename)

def batch_create_files(url_list):
    n=0
    for url in url_list:
        date, title, text = get_info(url)
        if (date, title, text):
            create_file(date, title, text, n)
            n= n+1
        else:
            print("no data")


#def find_last_section(first_url):
#    """find the last section"""
#    next_url = first_url
#    while next_url:
#        final_url = next_url
#        next_url = find_next_section(make_request(next_url))
#    page_num = re.search("page=([0-9]+)", str(final_url))
#    return page_num.group(1)

#def create_url_list(period, keywords):
#    page_urls = []
#    page = create_url(1, period, keywords)
#    while page:
#    for n in range(1, n): #known: a total of 24 pages
#        page_urls.append(create_url(n, period, keywords))
#    return page_urls
