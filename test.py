#! /usr/bin/env python  
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test
   Description :
   Author :       liuhao
   date：          2018/9/5
-------------------------------------------------
   Change Activity:
                   2018/9/5:
-------------------------------------------------
"""
import requests
import os
url='http://tupian.aladd.net/2017/8/yinyangshihuaniaojuantupian.jpg'
r =requests.get(url)
os.chdir(r'F:\code\hua')
course = open('huaniaojuan.jpg', 'wb')
course.write(r.content)
course.close()