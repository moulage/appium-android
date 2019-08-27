# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:auto_logging

import os
import logging

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

"""
logger日志
"""


def log():
    logging.basicConfig(level=logging.DEBUG, format=f'')