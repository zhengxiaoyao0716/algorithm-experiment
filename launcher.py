#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
launcher
@author: zhengxiaoyao0716
"""


import sys
from importlib import import_module


def main():
    """Entrypoint"""
    file = sys.argv[1]
    if file.endswith('.py'):
        file = file[0:-3]
    module = import_module(file)
    module.main()

if __name__ == '__main__':
    main()
