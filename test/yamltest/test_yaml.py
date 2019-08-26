# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:test_yaml.py

import os
import unittest
import sys
from test.unit.common.webdriverUnit import WebdriverUnit
from test.unit.common import toolUnits

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

import yaml


def get_yaml_data(yaml_file):
    """打开yaml文件"""
    file = open(yaml_file, 'r', encoding='utf-8')
    file_data = file.read()
    file.close()

    data = yaml.load(file_data)
    print(data)


if __name__ == '__main__':
    get_yaml_data('config.yaml')