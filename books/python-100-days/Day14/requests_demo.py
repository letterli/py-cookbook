#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import time
from threading import Thread

import requests


class DownloadHandler(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        file_path = '/local/path/' + filename
        with open(file_path, 'wb') as f:
            f.write(resp.content)


def main():
    api_url = 'https://example.com/api'
    resp = requests.get(api_url)
    data_model = resp.json()

    for mm_dict in data_model['newslist']:
        url = mm_dictp['picUrl']
        DownloadHandler(url).start()


if __name__ == '__main__':
    main()


