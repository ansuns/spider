#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'RoLiHop'

import urllib.request, http.cookiejar
from bs4 import BeautifulSoup

url = 'https://www.baidu.com/'

#1
response = urllib.request.urlopen(url)
print(response.getcode())
print(response.read())

#2
request = urllib.request.Request(url)
#伪装为浏览器请求
request.add_header('User-Agent', 'Mozilla/5.0')
response2 = urllib.request.urlopen(request)
print(response2.getcode())
print(response2.read())

#3
cj = http.cookiejar.CookieJar()
openner = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(openner)
response3 = urllib.request.urlopen(request)
print(response3.getcode())
print(cj)
print(response3.read())