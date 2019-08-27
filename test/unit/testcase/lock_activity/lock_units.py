# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:lock_units.py

import os
import unittest
import sys
from test.unit.common.webdriverUnit import WebdriverUnit
from test.unit.common import toolUnits

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

"""
门锁工具
"""


def input_apply_for_lock(driver):
    """进入门锁申请页面"""
    if driver.hasElement(driver.ele.WebView_TitleBar_Title):
        driver.assertEqual(driver.ele.MS_XZWebViewActivit, driver.driver.current_activity, '进入门锁介绍页失败')
        driver.find_element_desc_click_wait('申请门锁服务')
    else:
        driver.assertEqual(driver.ele.MS_Lock_ManageActivity, driver.driver.current_activity, '进入门锁管理页面失败')
        driver.find_element_id_and_click_wait(driver.ele.MS_lock_manager_passBtn)


def input_lock_management(driver, back=True):
    """
    进入门锁管理页面
    :param driver:
    :param back: 是否返回上一级页面
    :return:
    """
    if driver.get_text(driver.ele.MS_lock_manage_group_title) == '- 使用中的门锁 -':
        driver.find_element_id_and_click_wait(driver.ele.MS_lock_manage_using_lockName)
        toolUnits.wait(driver.driver, driver.ele.actionbarwidget_back, 3)
        driver.assertEqual(driver.ele.MS_Lock_PrivilegeManageActivity, driver.driver.current_activity, '进入开门权限设置页面失败')
        if back:
            driver.backlast(1)
            driver.assertEqual(driver.ele.MS_Lock_ManageActivity, driver.driver.current_activity, '门锁管理页面返回列表失败')
            driver.find_element_id_and_click_wait(driver.ele.MS_lock_manager_passBtn)


def input_lock_management(driver):
    """进入门锁管理模块"""
    if driver.get_text(driver.ele.MS_lock_manage_group_title) == '- 使用中的门锁 -':
        driver.find_element_id_and_click_wait(driver.ele.MS_lock_manage_using_lockName)
        driver.assertEqual(driver.ele.MS_Lock_PrivilegeManageActivity, driver.driver.current_activity, '进入开门权限设置页面失败')


def apply_for_lock(driver):
    """申请门锁"""
    driver.find_element_id_and_click_wait(driver.ele.MS_lock_apply_isSelectMarkImg)
    driver.find_element_id_and_click_wait(driver.ele.actionbarwidget_moreTextView)
    driver.find_element_id_and_click_wait(driver.ele.MS_radio_lock_item_point)
    driver.find_element_id_and_click_wait(driver.ele.actionbarwidget_moreTextView)
    for i in range(5):
        if not driver.has_class_name_and_click('上传图片'):
            driver.swipeDown(0.5, 0.6, 0.4)
        driver.find_element_class_name_and_click('上传图片')
        toolUnits.upload_picture(driver)
    driver.find_element_id_and_click_wait(driver.ele.actionbarwidget_moreTextView)
    

def delete_lock_apply(driver):
    """删除门锁"""
    driver.backlast(1)
    driver.swipeDown(0.5, 0.9, 0.1)
    driver.find_element_class_name_and_click('取消申请')
    driver.find_element_id_and_click_wait(driver.ele.standard_dialog_one_btn_right)

