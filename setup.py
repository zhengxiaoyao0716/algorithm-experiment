#!/bin/python
# -*- coding: utf-8 -*-

"""
algorithm-experiment
@author: zhengxiaoyao0716
"""

from cx_Freeze import setup, Executable


setup(
    name='algorithm-experiment',
    version='1.0',
    description='algorithm-experiment',
    options={
        "build_exe": {
            "packages": ["matplotlib"]
        }
    },
    executables=[Executable(
        'launcher.py',
        targetName='launcher.exe',
        compress=True
    )]
)
