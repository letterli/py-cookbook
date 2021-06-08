#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
统计一个文件中每个单词出现的次数，列出出现频率最多的5个单词。
"""

import re

class Counter:

    def __init__(self, path):
        """
        :param path: 文件路径
        """
        self.mapping = {}
        with open(path, 'r') as f:
            data = f.read()
            words = [word.lower() for word in re.findall(r'\w+', data)]
            for word in words:
                self.mapping[word] = self.mapping.get(word, 0) + 1

    def most_common(self, n):
        assert n > 0, "n should be large than 0"
        return sorted(self.mapping.items(), key=lambda item: item[1], reversed=True)

if __name__ == '__main__':
    most_common_5 = Counter().most_common(5)
    for item in most_common_5:
        print(item)

