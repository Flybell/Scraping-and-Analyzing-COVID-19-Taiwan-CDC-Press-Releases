import unittest
import re #regular expression
import io
from bs4 import BeautifulSoup #web parsing library
#----#make requests as a browser
import requests
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
#----
from Scrape_Web import create_url, make_request, find_next_page, get_url, read_urls, get_info, create_file

#test urls go here
test_url = 'https://www.cdc.gov.tw/Bulletin/List/MmgtpeidAR5Ooai4-fgHzQ?page=19&startTime=2020.01.01&keyword=新增 確診'
test_pr_url = "https://www.cdc.gov.tw/Bulletin/Detail/gu4Xy8NSvNN8jtDBCjtmpw?typeid=9"
soup = make_request(test_url)

class GetDataTestCase(unittest.TestCase):

    def test_create_url(self):
        url = create_url(1, "2020.01.01", "新增 確診")
        self.assertEqual(url, 'https://www.cdc.gov.tw/Bulletin/List/MmgtpeidAR5Ooai4-fgHzQ?page=1&startTime=2020.01.01&keyword=新增 確診')

    def test_find_next_page(self):
        url = find_next_page(soup)
        self.assertTrue(re.search("page=20", url))

    def test_get_url(self):
        """the urls got are typeid=9 bulletins"""
        """example: 'https://www.cdc.gov.tw/Bulletin/Detail/gu4Xy8NSvNN8jtDBCjtmpw?typeid=9'"""
        url_list = get_url(soup)
        type = re.findall(".{8}$", url_list[0])
        self.assertEqual(type[0], "typeid=9")

#    def test_no_cases(self):
#       """ this test requires a HTTP request, not suitable as a unit test"""
#        date = get_info(test_pr_url)[0]
#        title = get_info(test_pr_url)[1]
#        self.assertEqual(date, ("2020-04-30"))
#        self.assertEqual(title, "今日無新增病例，累計322人解除隔離")

    def test_create_file(self): #create file with date and title inserted
        create_file("0000-00-00","今日無新增病例，累計311人解除隔離", "dummy text")

unittest.main()
