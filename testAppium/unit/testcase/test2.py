# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:test2.py

import os
import sys
from testAppium.unit.testcase.monitor_suit import MonitorSuit
from testAppium.conf.getPhoneConfig import ConfigPhoneDevices

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

"""
注册登录测试用例集合
"""

import datetime
from testAppium.data import auto_logging

class Person(object):

    name = 'zhejiang'

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':

    def f(s) -> int:
        a = list(s)
        a.sort()
        return s.count(a[0])

    queries = ["bba", "abaaaaaa", "aaaaaa", "bbabbabaab", "aba", "aa", "baab", "bbbbbb", "aab", "bbabbaabb"]
    words = ["aaabbb", "aab", "babbab", "babbbb", "b", "bbbbbbbbab", "a", "bbbbbbbbbb", "baaabbaab", "aa"]

    a = {1:['ad','asd','asdf'], 5:['adf','qwe','qwe'], 4:['fre','ewr','dasf']}

    b = sorted(a)

    print(b)




