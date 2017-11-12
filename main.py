# -*- coding: utf-8 -*-
import sys
#import datetime
import os
import pymongo
#import pyquery
import requests

from requests import Request, Session

# Declaration
home_page_url = 'https://onejav.com/'
search_page_url = 'https://onejav.com/search/'
# Search example
# https://onejav.com/search/EBOD?page=1

search_code = 'EBOD'
s=requests.Session()

keep_searching = True
searching_page_number = 1
while (keep_searching):
    r1= s.get(search_page_url + search_code + '?page' + searching_page_number.__str__(), verify=False)
    print r1.content
    searching_page_number = searching_page_number + 1
    sleep(10)