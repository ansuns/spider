#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import url_manager
import html_paser
import html_downloader
import html_outputer

__author__ = 'RoLiHop'

class Spider(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_paser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d : %s' %(count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parser(new_url, html_cont)
                self.urls.add_new_urls(new_urls)    #新的URL加入管理器
                self.outputer.collect_data(new_data)

                if count == 20 :
                    break
                count = count + 1
            except:
                print('craw failed')

        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "http://www.gamersky.com/ent/201709/962073.shtml"
    obj_spider = Spider()
    obj_spider.craw(root_url)
