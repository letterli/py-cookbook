#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
设置一个算法，将URL转换成5部分，分别为:schema、netloc、path、query_params、fragment

<schema>://<netloc>/<path>?<query_params>#<fragment>
"""

import re
# namedtuple是继承自tuple的子类。namedtuple创建一个和tuple类似的对象，而且对象拥有可访问的属性。
from collections import namedtuple

URL = namedtuple("URL", ["schema", "netloc", "path", "params", "fragment"])

def url_parse1(url):
    """ 使用字符串常用方法split find join lower 切片 """
    assert url.startswith("http"), "params must be a url"
    # 初始化每部分为空
    schema = netloc = path = params = fragment = None
    # 从 :// 切分url,前面部分是schema
    i = url.find("://")
    if i > 0:
        schema = url[:i]
        url = url[i + 3:]
        # 获取netloc
        for c in "/?#":
            a = url.find(c)
            if a > 0:
                netloc, url = url[0:a], url[a:]
                break
        else:
            netloc, url = url, ''

        # 获取path
        for c in "?#":
            a = url.find(c)
            if a > 0:
                path, url = url[0:a], url[a:]
                break
        else:
            path, url = url, ''

        if "#" in url:
            url, fragment = url.split("#", 1)
        if "?" in url:
            url, params = url.split("?", 1)
    return URL(schema=schema, netloc=netloc, path=path, params=_params_parse(params), fragment=fragment)

def url_parse2(url):
    """ 使用正则表达式 """
    rex = r'^(http[s]?):\/\/([^\/\s]+)([\/\w\-\.]+[^#?\s]*)?(\?([^#]*))?(#(.*))?$'
    schema = netloc = path = params = fragment = None

    pattern = re.compile(rex)
    match = pattern.match(url)

    if match:
        schema = match.group(1)
        netloc = match.group(2)
        path = match.group(3)
        params = match.group(5)
        fragment = match.group(7)

    return URL(schema=schema, netloc=netloc, path=path, params=_params_parse(params), fragment=fragment)

def _params_parse(params):
    if not params:
        return None
    pairs = [s for s in params.split('&')]
    param_dict = {}
    for pair in pairs:
        k, v = pair.split('=', 1)
        param_dict[k] = v
    return param_dict


url = "https://www.infzm.com/content/8000"

print url_parse2(url)
