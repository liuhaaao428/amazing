#! /usr/bin/env python  
# -*- coding: utf-8 -*-
import re
import requests
r = "12ad56fdds756gd"
matchObj = re.findall('\d+[a-zA-Z]*' , r)
print(matchObj)
