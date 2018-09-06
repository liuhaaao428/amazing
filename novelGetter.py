#! /usr/bin/env python  
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     novelGetter.py
   Description :
   Author :       liuhao
   date：          2018/9/6
-------------------------------------------------
   Change Activity:
                   2018/9/6:
-------------------------------------------------
"""
import requests
from bs4 import BeautifulSoup
import re
import os
def download(url):
    response= requests.get(url).text
    soup= BeautifulSoup(response, 'lxml')
    txt= soup.find_all('div',{'class':'showtxt'})
    #print(txt)
    #print(url)
    os.chdir(r'F:\code\hua')
    f= open('testNovel.txt', 'w')
    for t in txt:
        t= t.text.replace(u'\xa0', u' ')
        f.write(t)
    f.close()

download('http://www.biqukan.com/1_1094/5386269.html')