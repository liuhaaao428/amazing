#! /usr/bin/env python  
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     studentsListGetter.py
   Description :
   Author :       liuhao
   date：          2018/9/8
-------------------------------------------------
   Change Activity:
                   2018/9/8:
-------------------------------------------------
"""
import requests
from bs4 import BeautifulSoup
import re
import os
def test(url):
    payload={'xh':'2016211956'}#暴露学号了2333
    response=requests.get(url,params=payload).text
    soup= BeautifulSoup(response, features='lxml')
    course_urllist=soup.find_all('a',{'target': '_blank'})
    for list in course_urllist:
        res=requests.get('http://jwzx.cqupt.edu.cn/kebiao/'+list['href']).text
        stusoup=BeautifulSoup(res,features='lxml')
        mixlist=stusoup.find_all('td')
        for mlist in mixlist:

            stulist=re.findall(r'^[\u4e00-\u9fa5]{2,3}$',mlist.text)
            #这里是真的累，学生姓名和学院学好这些乱七八糟属性的tag全是一样的，难以处理
            x=0
            length=len(stulist)
            while x < length:
                if stulist[x]=='学号'or stulist[x]=='姓名'or stulist[x]=='性别'or stulist[x]=='专业号'or stulist[x]=='专业名'or stulist[x]=='学院' or stulist[x]=='年级'or stulist[x]=='在校' or stulist[x]=='正常' or stulist[x]=='必修' or stulist[x]=='班级' or stulist[x]=='选修':
                    #万万没想到python的或运算竟然是or
                    stulist.remove(stulist[x])
                    x=x-1
                    length=length-1
                x=x+1
            #print(stulist)
            os.chdir(r'F:\code\hua')
            f=open('namelist.txt','a')
            f.writelines(stulist)
    #print()
test('http://jwzx.cqupt.edu.cn/kebiao/kb_stu.php')