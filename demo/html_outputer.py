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

    #创建新目录
    def mkdir(self,path):
        path = time.strftime('%Y%m%d%H')
        path = path.strip()
        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists=os.path.exists(path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            print (u"偷偷新建了名字叫做",path,u'的文件夹')
            # 创建目录操作函数
            os.makedirs(path)
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print (u"名为",path,'的文件夹已经创建成功')
            return False


    #传入图片地址，文件名，保存单张图片
    def saveImg(self,imageURL, fileName):
        #self.mkdir(time.strftime('%Y%m%d%H'))
        soup = BeautifulSoup(str(imageURL), 'html.parser')
        img = soup.find('img')['src']

        number = 0
        splitPath = img.split('.')

        fTail = splitPath.pop()

        r1 = u'[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，\n。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'#用户也可以在此进行自定义过滤字符
        r2 = u'\s+;'

        fileName = re.sub(r1, '', fileName) #过滤内容中的各种标点符号
        if fileName is None:
            fileName = range(0, 100)
        fileName = time.strftime('%Y%m%d%H') + '/' + fileName + '.' + fTail
        u = urllib.request.urlopen(img)
        data = u.read()
        f = open(fileName, 'wb')
        f.write(data)
        print(u"正在悄悄保存她的一张图片为", fileName)
        f.close()


    def output_html(self):

        str = time.strftime('%Y%m%d%H%M%S') + '.html'
        fout = open(str, 'w', encoding="utf-8")
        fout.write("<html>")
        fout.write("<head><meta http-equiv=\"content-type\" content=\"text/html;charset=utf-8\"></head>")
        fout.write("<body>")
        fout.write("<table>")
        for dataddddd in self.datas:
            for data in dataddddd:
                self.saveImg(data['img'], data['title'])
                fout.write("<tr>")
                fout.write("<td>%s</td>" % data['url'])
                fout.write("<td><a href='%s'>%s</a></td>" % (data['url'], data['title']))
                fout.write("<td>%s</td>" % data['img'])
                fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")