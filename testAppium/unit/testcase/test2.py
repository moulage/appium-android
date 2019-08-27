# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:test2.py

import os
import unittest
import sys
from test.unit.common.webdriverUnit import WebdriverUnit
from test.unit.common import toolUnits

from test.unit.testcase.start_activity import AA_StartAPPActivity

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

"""
注册登录测试用例集合
"""


def add_def_name():
    print(AA_StartAPPActivity().__doc__())


class Person(object):

    name = 'zhejiang'

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    pass


class Person(object):
    address = 'zhejiang'

    def __init__(self):
        self.name = "哈哈"

    def add(self):
        pass

    def gets(self):
        print(list(filter(lambda m: not m.startswith("__") and not m.endswith("__") and callable(getattr(self, m)),
                          dir(self))))

print(list(filter(lambda m: m.startswith("test") and callable(getattr(Person(), m)), dir(Person))))

print(Person().__getattribute__('add'))


