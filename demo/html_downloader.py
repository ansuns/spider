#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'RoLiHop'

import requests

#python3中是用urllib.request.urlopen()
class HtmlDownloader(object):
    def download(self, new_url):
        if new_url is None:
            return None
        response = requests.get(new_url)
        if response.status_code != 200:
            return None
        return response.text

