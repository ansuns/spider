#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'RoLiHop'


import re
import urllib.parse, time, os
from bs4 import BeautifulSoup

class HtmlParser(object):
    def parser(self, new_url, html_cont):
        if new_url is None or html_cont is None:
            return
        #soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        soup = BeautifulSoup(html_cont, 'html.parser')
        new_urls = self._get_new_urls(new_url, soup)
        new_data = self._get_new_data(new_url, soup)

        return new_urls, new_data

    def _get_new_urls(self, new_url, soup):
        new_urls = set()
        #links = soup.find_all('a', href=re.compile(r"/item/\S"))
        #links = soup.find_all('a', href=re.compile(r"/item/\."))
        links = soup.find_all('a',href=re.compile(r'/ent/*.?'))  #获得新网页内所有RUL
        for link in links:
            new_link = link['href']
            new_full_link = urllib.parse.urljoin(new_url, new_link)
            new_urls.add(new_full_link)
        return new_urls

        #传入图片地址，文件名，保存单张图片
    def saveImg(self,imageURL, fileName, number):

        splitPath = imageURL.split('.')

        fTail = splitPath.pop()

        r1 = u'[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，\n。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'#用户也可以在此进行自定义过滤字符
        r2 = u'\s+;'

        fileName = re.sub(r1, '', fileName) #过滤内容中的各种标点符号
        if fileName is None:
            fileName = range(0, 100)
        fileName = time.strftime('%Y%m%d%H') + '/'  + str(number)   + '_' + fileName  + '.' + fTail
        u = urllib.request.urlopen(imageURL)
        data = u.read()
        f = open(fileName, 'wb')
        f.write(data)
        print(u"保存一张图片为:", fileName)
        f.close()


    def _get_new_data(self, new_url, soup):
        res_data = []
        title_node = soup.find('div', class_='Mid2L_con').find_all("p")
        number = 1
        for ii in title_node:
            t = ii.img
            if t == None:
                continue

            soupX = BeautifulSoup(str(ii.img), 'html.parser')
            t = soupX.find('img')['src']
            self.saveImg(t,ii.get_text(), number)
            number += 1
            res_data.append({'title':ii.get_text(),'summary':ii.get_text(),'url':new_url, 'img':t})
        return res_data

