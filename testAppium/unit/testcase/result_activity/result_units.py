# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:result_units.py

import os
import unittest
import sys
from testAppium.unit.common.webdriverUnit import WebdriverUnit
from testAppium.unit.common import toolUnits

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

"""
结果页操作工具
"""


def input_result(driver):
    """进入结果页"""
    if driver.hasElement(driver.ele.SY_search_widget_if_clear):
        driver.find_element_id_and_click_wait(driver.ele.SY_search_widget_if_clear)
    driver.find_element_id_and_click_wait(driver.ele.SY_search_widget_tv_city)
    driver.find_element_id_and_click_wait(driver.ele.SS_wg_gv_itemtv, 1)


if __name__ == '__main__':
    pass
