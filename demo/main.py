#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import url_manager
import html_paser
import html_downloader
import html_outputer
import time, os

__author__ = 'RoLiHop'

class Spider(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_paser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 0
        self.urls.add_new_url(root_url)
        self.mkdir(time.strftime('%Y%m%d%H'))
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d : %s' %(count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data, n = self.parser.parser(new_url, html_cont)

                if n > 1:
                    self.urls.add_new_urls(new_urls)    #新的URL加入管理器
                    self.outputer.collect_data(new_data)

                if count >= 520 :
                    break
                count = count + n
                print('当前数量 %d :' % count)
            except:
                print('craw failed')

        self.outputer.output_html()

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
            print (u"新建",path,u'文件夹')
            # 创建目录操作函数
            os.makedirs(path)
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print (u"名为",path,'的文件夹已经创建成功')
            return False


if __name__ == "__main__":
    root_url = "http://www.gamersky.com/ent/201709/962073.shtml"
    obj_spider = Spider()
    obj_spider.craw(root_url)
