#! /usr/bin/env python  
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     third.py
   Description :
   Author :       liuhao
   date：          2018/9/5
-------------------------------------------------
   Change Activity:
                   2018/9/5:
-------------------------------------------------
"""
import requests
import re
import os
from bs4 import BeautifulSoup
url='http://aladd.net/archives/31861.html'
html = requests.get(url).text
pic_url = re.findall('<img src="(.*?)" alt=', html, re.S)
i= 0
for each in pic_url:
    print(each)
    try:
        pic = requests.get(each,timeout=10)
    except requests.exceptions.ConnectionError:
        print("error , timeout")
        continue
    os.chdir(r'F:\code\hua')
    f = open('huaniaojuan'+str(i)+'.jpg', 'wb')
    f.write(pic.content)
    f.close()
    i = i + 1
