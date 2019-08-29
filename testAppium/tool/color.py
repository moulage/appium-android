# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:color.py

import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


__author__ = 'wanghui'


class ColorMe(object):
    """
    give me color see see...
    实际用起来很简单：
        ColorMe('somestr').blue()
    """
    def __init__(self, some_str):
        self.color_str = some_str

    def blue(self):
        str_list = ["\033[34;1m", self.color_str, "\033[0m"]
        return ''.join(str_list)  # "\033[34;1m" + self.color_str + "\033[0m"

    def green(self):
        str_list = ["\033[32;1m", self.color_str, "\033[0m"]
        return ''.join(str_list)  # "\033[34;1m" + self.color_str + "\033[0m"

    def yellow(self):
        str_list = ["\033[33;1m", self.color_str, "\033[0m"]
        return ''.join(str_list)  # "\033[34;1m" + self.color_str + "\033[0m"

    def red(self):
        str_list = ["\033[31;1m", self.color_str, "\033[0m"]
        return ''.join(str_list)  # "\033[34;1m" + self.color_str + "\033[0m"


def main():
    print(ColorMe('haojie').green())


if __name__ == '__main__':
    main()
