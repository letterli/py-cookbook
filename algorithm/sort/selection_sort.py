# -*- coding: utf-8 -*-

# 选择排序　时间复杂度O(n^2)

def selection_sort(alist):
    for fillslot in range(len(alist)-1, 0, -1):
        position_of_max = 0
        for location in range(1, fillslot+1):
            if alist[location] > alist[position_of_max]:
                position_of_max = location

        alist[fillslot], alist[position_of_max] = alist[position_of_max], alist[fillslot]

alist = [54,26,93,17,77,31,44,55,20]
# selection_sort(alist)
print alist


