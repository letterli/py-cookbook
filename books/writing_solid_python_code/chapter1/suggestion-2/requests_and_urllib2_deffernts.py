#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version python 2.7

"""
requests 与　urllib2 通过http/https协议获取网络资源复杂度对比.

使用Pythonic的程序库可以简化很多工作量。
"""


import requests
import urllib2


def use_requests():
    response = requests.get('https://www.infzm.com')
    print(response.status_code)
    print(response.headers['content-type'])


def use_urllib2():
    source_url = 'https://api.github.com'
    request = urllib2.Request(source_url)
    response = urllib2.urlopen(request)
    print(response.getcode())
    print(response.headers.getheader('content-type'))


if __name__ == '__main__':
    use_requests()
    use_urllib2()
