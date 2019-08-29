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


class Person(object):

    name = 'zhejiang'

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    nameConfig = ConfigPhoneDevices()
    execute_phone = sys.argv[1]
    nameConfig.set_option("EXECUTE", 'ing', execute_phone)
    nameConfig.set_option(execute_phone, "execution", "EXECUTION_ING")
    MonitorSuit().monitor_test()
    nameConfig.set_option(execute_phone, "execution", "EXECUTION")




