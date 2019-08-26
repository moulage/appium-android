# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:house_detail_units.py

import os
from time import sleep

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

"""
房源详情页测试小工具
"""


def checkInDetail(driver):
    """首页--进入房源详情页"""
    if driver.hasElement(driver.ele.SY_search_widget_if_clear):
        driver.find_element_id_and_click_wait(driver.ele.SY_search_widget_if_clear)
    driver.find_element_id_and_click_wait(driver.ele.SY_search_widget_tv_city)
    driver.find_element_id_and_click_wait(driver.ele.SS_wg_gv_itemtv, 1)
    driver.find_element_id_and_click_wait(driver.ele.SY_search_widget_btn_search)
    sleep(1)
    driver.find_element_id_and_click_wait(driver.ele.JGY_iv_loop_image_item)
    sleep(1)


if __name__ == '__main__':
    pass
