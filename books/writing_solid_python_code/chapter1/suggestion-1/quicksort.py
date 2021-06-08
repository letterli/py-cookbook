#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version 2.7
# 快速排序算法实现

"""
快速排序算法：
通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。
"""


def quicksort(array):
    less = []
    greater = []

    if len(array) <= 1:
        return array
    pivot = array.pop()
    for n in array:
        if n < pivot:
            less.append(n)
        else:
            greater.append(n)
    return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    sort_list = [9, 8, 4, 45, 76, 334]
    print(quicksort(sort_list))
