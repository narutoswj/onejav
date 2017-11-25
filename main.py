# -*- coding: utf-8 -*-
import sys
#import datetime
import time
import os
import pymongo
import pyquery
import requests

from requests import Request, Session
from pyquery import PyQuery as pq

# Declaration
home_page_url = 'https://onejav.com'
search_page_url = 'https://onejav.com/search/'

# Search example
# https://onejav.com/search/EBOD?page=1

search_code = 'ABP'
s=requests.Session()

keep_searching = True
searching_page_number = 1
while (keep_searching):
    r1= s.get(search_page_url + search_code + '?page=' + searching_page_number.__str__(), verify=False)
    print r1.content

    page_pyquery = pq(r1.content)
    #print page_pyquery
    if (page_pyquery('h1').text() <> 'Not Found'):
        container = page_pyquery('.card')

        for card in container:
            title = pq(card)('h5')('a').text()
            coverpage_url = pq(card)('img').attr('src')
            capacity = pq(card)('h5')('span').text()
            release_date = pq(card)('.is-6').text()
            tags = pq(card)('.tag')
            description = pq(card)('.has-text-grey-dark').text()
            download_url = home_page_url + pq(card)('.button').attr('href')

            print title
            print coverpage_url
            print capacity
            print release_date
            print description
            print download_url
            for tag in tags:
                tag_name = pq(tag)('a').text()
                print tag_name
            
            windows_line_ending = '\r\n'
            linux_line_ending = '\n'

            download_torrent= s.get(download_url, verify=False)
            #print download_torrent
            f = open(title + '.torrent','wb')
            f.write(download_torrent.content.replace(windows_line_ending, linux_line_ending))
            f.close()
            
    else:
        keep_searching = False
    #Set incremental
    searching_page_number = searching_page_number + 1
    time.sleep(2)