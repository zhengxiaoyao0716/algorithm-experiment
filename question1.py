#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
求N个数中选M个组合方案数
@author: zhengxiaoyao0716
"""


from util import read_inputs, IntValidator


def combinations(n, m):
    """求取组合方案"""
    if m == 1:
        return [[l] for l in range(1, n + 1)]
    if n == m:
        return [list(range(1, n + 1))]
    result = combinations(n - 1, m)
    for combination in combinations(n - 1, m - 1):
        combination.append(n)
        result.append(combination)
    return result


def main():
    """Entrypoint"""
    for _ in range(read_inputs('请输入正整数T (T <= 10): ', IntValidator(1, 11))):
        print(combinations(*read_inputs(
            '请输入2个正整数N, M (1 <= M <= N <= 30): ',
            IntValidator(1, 31), IntValidator(1, 31),
            validate=(lambda values: values[0] > values[1], 'N必须大于M')
        )))
    read_inputs('请按回车键退出', None)
if __name__ == '__main__':
    main()
