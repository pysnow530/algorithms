#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""排序算法"""


def straight_insertion_sort(lst):
    """直接插入排序
思想：将N个元素以此插入前N-1个已排好序的列表。
时间复杂度：N^2"""
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            itm = lst[i]
            j = i - 1
            while j >= 0 and itm < lst[j]:
                lst[j + 1] = lst[j]
                j -= 1
            lst[j + 1] = itm
        print lst[:i+1], '|', lst[i+1:]

    return lst


def _get_list_by_indexs(lst, idxs):
    return [lst[idx] for idx in idxs]


def _set_list_by_indexs(lst, idxs, vals):
    for i in range(len(idxs)):
        lst[idxs[i]] = vals[i]


def shell_sort(lst):
    """希尔排序
思想：对等间隔序列依次排序，间隔分别取n/2、n/4、n/8...1"""
    denominator = 2
    gap = len(lst) / denominator
    while gap:
        for i in range(0, gap):
            idxs = range(i, len(lst), gap)
            tmp_lst = _get_list_by_indexs(lst, idxs)
            tmp_lst = straight_insertion_sort(tmp_lst)
            _set_list_by_indexs(lst, idxs, tmp_lst)
        print lst

        denominator *= 2
        gap = len(lst) / denominator

    return lst


def simple_selection_sort(lst):
    """简单选择排序
算法思想：选出剩下的最小数字加入已排序列表
时间复杂度：N^2"""
    for i in range(len(lst) - 1):
        min_pos = i
        min_val = lst[i]
        for j in range(i+1, len(lst)):
            if min_val > lst[j]:
                min_pos, min_val = j, lst[j]
        lst[i], lst[min_pos] = lst[min_pos], lst[i]
        print lst[:i+1], '|', lst[i+1:]

    return lst


def bubble_sort(lst):
    """冒泡排序
算法思想：依次比较相邻两个数，每一趟会得到一个最右值
时间复杂度：N^2"""
    for i in range(len(lst)-2, -1, -1):
        for j in range(0, i+1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
        print lst[:i+1], '|', lst[i+1:]

    return lst


def quick_sort(lst):
    """快速排序
算法思想：递归算法
时间复杂度：Nlog2N"""
    if len(lst) == 0:
        return []
    else:
        return quick_sort([x for x in lst[1:] if x < lst[0]]) + [lst[0]] + quick_sort([x for x in lst[1:] if x > lst[0]])


# straight_insertion_sort(range(10)[::-1])
# shell_sort(range(10)[::-1])
# simple_selection_sort(range(10)[::-1])
# bubble_sort(range(10)[::-1])
print quick_sort(range(10)[::-1])
