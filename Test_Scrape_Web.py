import unittest
import re #regular expression
import io
from bs4 import BeautifulSoup #web parsing library
#----#make requests as a browser
import requests
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
#----

from Scrape_Web import get_info, create_file

#test urls go here
url = "https://www.cdc.gov.tw/Bulletin/Detail/l4frSPhB3__zcRYtVaL7Iw?typeid=9"

class GetDataTestCase(unittest.TestCase):

    def test_no_cases(self): #get date and title

        date = get_info(url)[0]
        title = get_info(url)[1]
        self.assertEqual(date, ("2020-04-29"))
        self.assertEqual(title, "今日無新增病例，累計311人解除隔離")

    def test_create_file(self): #create file with date and title inserted
        create_file("4000-04-04","今日無新增病例，累計311人解除隔離", "dummy text")

unittest.main()
