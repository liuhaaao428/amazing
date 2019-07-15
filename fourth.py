#! /usr/bin/env python  
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     fourth.py
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

# 在本地新建文件夹，命名为cat_img，用以保存下载的图片。具体语句的含义，可看代码猜测，也可百度方法的含义
folder = 'cat_img'
if not os.path.exists(folder):
    os.makedirs(folder)


# 新建一个函数，命名为download，作用是从网页中图片对应的代码，将图片下载到本地，下载路径为上面的folder文件夹中
def download(url):
    response = requests.get(url, headers=header)
    name = url.split('/')[-1]
    f = open(folder + '/' + name + '.jpg', 'wb')
    f.write(response.content)
    f.close()
    return True


# 网页的基本信息，包含网址url，和请求头header。这里的cat_url就是图片对应的网址，header的作用是防止反爬机制
cat_url = 'http://placekitten.com/450/1000'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

# 执行图片下载函数download，下载图片
download(cat_url)
print('OK')
# 运行完毕之后，可以查看本地，一张猫的图片已经下载到了//cat_img这个文件夹下