#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
a = [24, 37, 18, 45, 60]
b = ['张三', '李四', '王五', '赵六', '孙七']
c = ['北京', '上海', '武汉', '深圳', '南京']

a, b, c 三个列表中的数据根据下标具有一一对应关系，根据a列表中的数值从小到大排序，
b和c列表中的元素根据a列表的排序也重新排。

"""

a = [24, 37, 18, 45, 60]
b = ['张三', '李四', '王五', '赵六', '孙七']
c = ['北京', '上海', '武汉', '深圳', '南京']

# zip(iterable, ...)
# zip()是Python内建函数，接受一系列可迭代的对象作为参数，将对象中对应的元素打包成一个个tuple，然后返回这些tuple组成的list。
# d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# zip(*d) => [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

d = zip(a, b, c)

# sorted(iterable, cmp=None, key=None, reverse=False)
# iterable: 待排序的可迭代类型的容器
# cmp: 用于比较的函数
# key: 用列表元素的某个已命名的属性或函数作为关键字，有默认值，迭代集合中的一项
# reverse: 排序规则
# 返回值: 一个经过排序的可迭代类型，与iterable一样

s = sorted(d, key=lambda x:x[0], reverse=False)


res_a = [v[0] for v in s]
res_b = [v[1] for v in s]
res_c = [v[2] for v in s]

