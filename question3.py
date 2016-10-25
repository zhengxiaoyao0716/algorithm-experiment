#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
输油管道
@author: zhengxiaoyao0716
"""

from pylab import mpl
import matplotlib.pyplot as plt

from util import read_inputs, NumValidator, IntValidator


def calculate_pipe(wells):
    """计算管道位置"""

    def is_smaller(self, other):
        """是否小于"""
        return self[1] < other[1]

    def quicksort(arr, left, right):
        """快速排序"""
        if left >= right:
            return

        pivot = arr[left]
        cursor = left + 1 if is_smaller(arr[left + 1], pivot) else left
        for i in range(left + 2, right + 1):
            if is_smaller(arr[i], pivot):
                cursor += 1
                arr[cursor], arr[i] = arr[i], arr[cursor]
        arr[left], arr[cursor] = arr[cursor], arr[left]

        quicksort(arr, left, cursor - 1)
        quicksort(arr, cursor + 1, right)

    end_index = len(wells) - 1
    quicksort(wells, 0, end_index)
    print(wells)
    return wells[end_index >> 1][1]


def draw(wells, pipe):
    """绘制图像"""
    # 基本配置
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    plt.xlabel('东西')
    plt.ylabel('南北')
    # 绘制图像
    for well_x, well_y in wells:
        plt.plot(well_x, well_y, 'or')
        plt.plot((well_x, well_x), (well_y, pipe), 'g')
    plt.expand_limit = lambda l_min, l_max, value=0.1: (
        l_min - value * (l_max - l_min),
        l_max + value * (l_max - l_min),
    )
    xlim = plt.expand_limit(*plt.xlim())
    plt.plot(xlim, (pipe, pipe), 'b')
    # 显示图像
    plt.xlim(xlim)
    plt.ylim(plt.expand_limit(*plt.ylim()))
    plt.show()

if __name__ == '__main__':
    # 数据读取处理
    WELLS = []
    for index in range(read_inputs('请输入油井总数n（正整数）：', IntValidator(1))):
        WELLS.append(read_inputs(
            '请输入第%d口井坐标（x、y，逗号分隔）：' % (1 + index),
            NumValidator(), NumValidator()
        ))
    draw(WELLS, calculate_pipe(WELLS))
