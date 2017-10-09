#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'RoLiHop'
from datetime import datetime
import time, urllib.request
from bs4 import BeautifulSoup, re, os

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, new_data):
        if new_data is None:
            return
        self.datas.append(new_data)


    def output_html(self):
        number = 0
        str = time.strftime('%Y%m%d%H%M%S') + '.html'
        fout = open(str, 'w', encoding="utf-8")
        fout.write("<html>")
        fout.write("<head><meta http-equiv=\"content-type\" content=\"text/html;charset=utf-8\"></head>")
        fout.write("<body>")
        fout.write("<table>")
        for dataddddd in self.datas:
            for data in dataddddd:
                #self.saveImg(data['img'], data['title'], number)
                fout.write("<tr>")
                fout.write("<td>%s</td>" % data['url'])
                fout.write("<td><a href='%s'>%s</a></td>" % (data['url'], data['title']))
                fout.write("<td><img src='%s' width='120px' height='90px' /></td>" % data['img'])
                fout.write("</tr>")
                number += 1
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")