# -*- coding: utf-8 -*-

# 冒泡排序法 时间复杂度 O(n^2)

def bubble_sort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

alist = [5, 45, 233, 64, 98, 46]
bubble_sort(alist)
print alist

# 短冒泡排序法

def short_bubble_sort(alist):
    exchange = True
    passnum = len(alist)-1

    while passnum > 0 and exchange:
        exchange = False

        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchange = True
                alist[i], alist[i+1] = alist[i+1], alist[i]

        passnum -= 1


slist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
short_bubble_sort(slist)
print slist
