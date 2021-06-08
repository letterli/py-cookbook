# _*_ coding: utf-8 _*_
# 快速排序法


def quick_sort(alist):
    if len(alist) < 2:
        return alist

    mid_position = len(alist) / 2
    mid_value = alist.pop(mid_position)
    left, right = [], []

    for value in alist:
        if value >= mid_value:
            right.append(value)
        else:
            left.append(value)

    return quick_sort(left) + [mid_value] + quick_sort(right)

alist = [54,26,93,17,77,31,44,55,20]
print(quick_sort(alist))
