# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:__init__.py

import os
import unittest
import sys
from test.unit.common.webdriverUnit import WebdriverUnit
from test.unit.common import toolUnits

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

"""
注册登录测试用例集合
"""