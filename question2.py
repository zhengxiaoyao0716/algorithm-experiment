#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
给出n，计算递归函数Succ(n);的值，给出调用次数
@author: zhengxiaoyao0716
"""


from functools import wraps

from util import read_inputs, NumValidator


def counter(func):
    """计数装饰器"""
    counter.count = counter.count if 'count' in counter.__dict__ else {}
    counter.count[func] = 0

    @wraps(func)
    def _wrapper(*args, **kwargs):
        counter.count[func] += 1
        return func(*args, **kwargs)
    return _wrapper


@counter
def succ(n):
    """递归函数"""
    if n <= 100:
        return succ(succ(n + 11))
    if n >= 101:
        return n - 10


def main():
    """Entrypoint"""
    print(succ(read_inputs('请给出n：', NumValidator())))
    print('调用次数：' + str(counter.count))
    read_inputs('请按回车键退出', None)
if __name__ == '__main__':
    main()
