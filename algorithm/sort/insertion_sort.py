# -*- coding: utf-8 -*-

# 插入排序　时间复杂度O(n^2)

def insertion_sort(alist):
    for index in range(1, len(alist)):
        current_value = alist[index]
        location = index

        while location > 0 and alist[location-1] > current_value:
            alist[location] = alist[location-1]
            location -= 1

        alist[location] = current_value

alist = [54,26,93,17,77,31,44,55,20]
insertion_sort(alist)
print alist
