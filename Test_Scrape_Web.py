import unittest
import re #regular expression
import io
from bs4 import BeautifulSoup #web parsing library
#----#make requests as a browser
import requests
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
#----
from Scrape_Web import create_url, make_request, find_next_page, get_url, make_url_list

#test urls go here
test_url = 'https://www.cdc.gov.tw/Bulletin/List/MmgtpeidAR5Ooai4-fgHzQ?page=1&startTime=2020.01.01&keyword=新增 確診'

class GetDataTestCase(unittest.TestCase):

    def test_create_url(self):

        url = create_url(1, "2020.01.01", "新增 確診")
        self.assertEqual(url, 'https://www.cdc.gov.tw/Bulletin/List/MmgtpeidAR5Ooai4-fgHzQ?page=1&startTime=2020.01.01&keyword=新增 確診')


    def test_find_next_page(self):

        url = find_next_page(test_url)
        self.assertTrue(re.search("page=2", url))

    def test_get_url(self):

        url = ['https://www.cdc.gov.tw/Bulletin/Detail/gu4Xy8NSvNN8jtDBCjtmpw?typeid=9', 'https://www.cdc.gov.tw/Bulletin/Detail/l4frSPhB3__zcRYtVaL7Iw?typeid=9', 'https://www.cdc.gov.tw/Bulletin/Detail/b3DXJvk3FzKKA2vaMSuRGg?typeid=9', 'https://www.cdc.gov.tw/Bulletin/Detail/_J3etjloskIxHngWaXmdfw?typeid=9', 'https://www.cdc.gov.tw/Bulletin/Detail/rr6EFmDuIf_-IUNcGJ9YEA?typeid=9', 'https://www.cdc.gov.tw/Bulletin/Detail/6q-9BQ7MNJFRADWSuw3E5w?typeid=9']
        url_list = get_url(test_url)
        self.assertEqual(url_list, url)


#    def test_no_cases(self): #get date and title

#        date = get_info(test_url)[0]
#        title = get_info(test_url)[1]
#        self.assertEqual(date, ("2020-04-29"))
#        self.assertEqual(title, "今日無新增病例，累計311人解除隔離")


#    def test_create_file(self): #create file with date and title inserted
#        create_file("4000-04-04","今日無新增病例，累計311人解除隔離", "dummy text")

unittest.main()
