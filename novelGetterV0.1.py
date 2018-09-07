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
#今天的目标是爬取一本完整的小说
import requests
from bs4 import BeautifulSoup
import re
import os
def download(url):
    response= requests.get(url).text
    soup= BeautifulSoup(response, 'lxml')
    section_urllist=soup.find_all('dd')#获取章节网址
    #原本我的想法是通过小说阅读网页中的‘下一章’获取章节网址
    #但是我发现在小说主页有所有章节的网址，就用了这种取巧的方法，缺点是最后几章
    # 内容会在开头重复出现
    #print(section_urllist.a['href'])
    for section_url in section_urllist:
        res=requests.get('http://www.biqukan.com'+section_url.a['href'],timeout=5).text
        #获取章节网址后发现缺少一部分，在这里要加上
        section_soup=BeautifulSoup(res, features='lxml')
        #这里我犯了一个错误。。。。直接BeautifulSoup(url)。。。
        txt= section_soup.find('div',{'class': 'showtxt'})
        section_name=section_soup.find('h1')
        #获取章节名
        #print(txt)
        #print(section_name)
        os.chdir(r'F:\code\hua')
        f = open('testNovelsectionname.txt', 'a')
        f.writelines(section_name.text.replace(u'\xa0', u' ')+'\n')
        f.writelines(txt.text.replace(u'\xa0', u' ')+'\n')
        #直到现在我都还没找到如何自动给文章分段
        print('正在下载 '+section_name.text)
    f.close()
    print('Download completed.')

download('http://www.biqukan.com/1_1094/')
#今天的任务算是勉强完成