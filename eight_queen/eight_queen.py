#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 八皇后问题（递归）
COL_FLAG    第n列是否已有皇后标志数组
GRAD1_FLAG  从右上到左下是否有皇后标志数组
GRAD2_FLAG  从左上到右下是否有皇后标志数组
"""
def calc_flag(solved_list, col_flag, grad1_flag, grad2_flag):
    """ 根据已有皇后填充flag数组"""
    for row, col in enumerate(solved_list):
        col_flag[col] = True
        grad1_flag[row + col] = True
        grad2_flag[7 + row - col] = True

    return


def hit_flag(row, col, col_flag, grad1_flag, grad2_flag):
    """判断一个位置是否与已有皇后冲突"""
    return col_flag[col] or grad1_flag[row + col] or \
            grad2_flag[7 + row - col]


def solve(solved_list):
    """求解个数"""
    nr_solve = 0

    if len(solved_list) == 8:
        return 1

    col_flag = [False] * 8
    grad1_flag = [False] * 16
    grad2_flag = [False] * 16
    calc_flag(solved_list, col_flag, grad1_flag, grad2_flag)

    row = len(solved_list)
    for col in range(0, 8):
        if not hit_flag(row, col, col_flag, grad1_flag, grad2_flag):
            nr_solve += solve(solved_list + [col])

    return nr_solve


print solve([0])
