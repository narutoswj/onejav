# -*- coding: utf-8 -*-

"""This file works on Spider AV info and download Torrent file from OENJAV.COM"""

#import sys
#import datetime
import time
import os
#import pymongo
#import pyquery
import requests

#from requests import Request
from pyquery import PyQuery as pq

# Declaration
HOME_PAGE_URL = 'https://onejav.com'
SEARCH_PAGE_URL = 'https://onejav.com/search/'
TORRENT_ROOT_PATH = '/media/joey/7f35cc7a-09cf-4e4d-a0b8-eb44b43df59f/Torrent/'

# Search example
# https://onejav.com/search/EBOD?page=1

SEARCH_CODE = 'ABP'
SESSION = requests.Session()

if not os.path.exists(TORRENT_ROOT_PATH + SEARCH_CODE):
    os.mkdir(TORRENT_ROOT_PATH + SEARCH_CODE)

keep_searching = True
searching_page_number = 1
while keep_searching:
    r1 = SESSION.get(SEARCH_PAGE_URL + SEARCH_CODE + '?page=' + searching_page_number.__str__(), verify=False)
    print r1.content

    page_pyquery = pq(r1.content)
    #print page_pyquery
    if page_pyquery('h1').text() <> 'Not Found':
        container = page_pyquery('.card')

        for card in container:
            title = pq(card)('h5')('a').text()
            coverpage_url = pq(card)('img').attr('src')
            capacity = pq(card)('h5')('span').text()
            release_date = pq(card)('.is-6').text()
            tags = pq(card)('.tag')
            description = pq(card)('.has-text-grey-dark').text()
            download_url = HOME_PAGE_URL + pq(card)('.button').attr('href')

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

            if not os.path.exists(TORRENT_ROOT_PATH + SEARCH_CODE + '/' + title + '.torrent'):
                download_torrent = SESSION.get(download_url, verify=False)
                #print download_torrent
                f = open(TORRENT_ROOT_PATH + SEARCH_CODE + '/' + title + '.torrent', 'wb')
                f.write(download_torrent.content.replace(windows_line_ending, linux_line_ending))
                f.close()
            
    else:
        keep_searching = False
    #Set incremental
    searching_page_number = searching_page_number + 1
    time.sleep(2)
