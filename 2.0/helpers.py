import os
import random
import sys
from datetime import datetime
import time
import requests
from bs4 import  BeautifulSoup
import pandas as pd
import lxml

import eventlet

import settings
from userAgents import user_agents, randomUserAgents


def soup(url,headers):
    ''' url = full glassdoor.com/reviews url'''
    session = requests.Session()
    req = session.get(url, headers=headers)
    bs = BeautifulSoup(req.text, 'lxml')
    return bs

pages = set()
def getPages(url, head):
    ''' Gets a set of ALL "Next Page" hrefs '''
    global pages
    bs = soup(url, head)
    nextPage = bs.find('div',{'class',"flex-grid tbl margTop"})
    for link in nextPage.findAll('a'):
        if 'href' in link.attrs:
            url = 'https://glassdoor.com{}'.format(link.attrs['href'])
            if url not in pages:
            #new page
                pages.add(url)
    #get last page
    for lastPage in nextPage.findAll('li',{'class':'page last'}):
        lastPage = 'https://glassdoor.com{}'.format(lastPage.a['href'])
        getPages(lastPage, head)
    return pages

