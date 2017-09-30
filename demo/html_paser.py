#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'RoLiHop'


import re
import urllib.parse
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

    def _get_new_data(self, new_url, soup):
        res_data = []
        title_node = soup.find_all("p")
        for ii in title_node:
            temp = ii
            #sssoup = BeautifulSoup(temp, 'html.parser')
            res_data.append({'title':ii.get_text(),'summary':ii.get_text(),'url':new_url})
        return res_data

