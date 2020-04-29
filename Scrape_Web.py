import re #regular expression
import io #UTF8 processing
from bs4 import BeautifulSoup #HTML parser library
import requests #make requests as a browser
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

#----------------------------------------
#find all pages based on search criteria
#----------------------------------------
def find_all_pages():
    page_urls = []
    #part 1 and 3 come from search term "新增 確診" starting Jan 1, 2020
    part_1="https://www.cdc.gov.tw/Bulletin/List/MmgtpeidAR5Ooai4-fgHzQ?page="
    part_3 = "&startTime=2020.01.01&keyword=%27%E6%96%B0%E5%A2%9E%20%E7%A2%BA%E8%A8%BA%27"
    for n in range(1, 25): #known: a total of 24 pages
        page_urls.append(part_1 + str(n) + part_3)
    return page_urls

#find all links on page that refer to press releases
def get_url(url):
    url_list = []
    req = requests.get(url, headers) #request HTML
    soup = BeautifulSoup (req.content, "html5lib") #make soup object
    for a in soup.find_all('a', {"href": re.compile("typeid=9$")}):
        if "新增" in a["title"]:
            url = "https://www.cdc.gov.tw" + a['href']
            url_list.append(url)
    return url_list

#create list of press releases url
def write_url(url_list):
    with open("URLS.txt", "a+") as url_file:
        for url in url_list:
            url_file.write(url+"\n")

#get URL from file of urls and create files
def list_of_urls(file):
    with open(file, "r+") as url_file:
        url = url_file.readlines()
    return url

#get the text from the right spot in the HTML file through URL
def get_info(url):
    req = requests.get(url, headers) #request HTML
    soup = BeautifulSoup (req.content, "html5lib") #make soup object

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

#create new file with date as file name and text as content
def create_file(date, title, text):
    if (date, title, text):
        filename = "%s.txt" % date
        with io.open(filename, "w+", encoding="UTF8") as newfile:
            text = text.replace(" ", "") #remove all spaces
            sentences= re.sub("，|。", "\n", text) #one sentence per line
            newfile.write(title+"\n")
            newfile.write(date+"\n")
            newfile.write(sentences)
    else:
        print("no data")
