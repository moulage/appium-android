# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:bookUnits.py

import os
import unittest
import sys
from time import sleep
from test.unit.common.webdriverUnit import WebdriverUnit
from test.unit.common import toolUnits

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def cancelOrder(driver):
    """取消订单"""
    for i in range(10):
        driver.backlast()
        if driver.hasElement(driver.ele.SY_HomepageNavTab):
            break
    driver.find_element_id_and_click_wait(driver.ele.SY_HomepageNavTab, 3)
    driver.find_element_id_and_equal_text_click(driver.ele.FKZX_tv_myself_normal_item_title, '全部订单')
    if driver.hasElement(driver.ele.FKDD_tv_first):
        driver.backlast(1)
        return
    toolUnits.wait(driver.driver, driver.ele.FKDD_tv_tenantOrderListItem_state, 5)
    driver.find_element_id_and_equal_text_click(driver.ele.FKDD_button_text, '操作订单')
    driver.find_element_id_and_equal_text_click(driver.ele.FKDD_button_text, '取消订单')
    driver.find_element_id_and_click_wait(driver.ele.QQDD_order_cancel_reason_isSelected)
    driver.find_element_id_and_click_wait(driver.ele.QQDD_advance_check_out_next)
    toolUnits.wait(driver.driver, driver.ele.FKDD_tv_orderListTab_title, 5)
    driver.backlast(1)


def aeecptOrder(driver):
    """接受订单"""
    driver.find_element_id_and_click_wait(driver.ele.SY_HomepageNavTab)
    driver.find_element_id_and_equal_text_click(driver.ele.FKDD_button_text, '接受订单')

    
def input_house_detail(driver):
    """进入房源预订页面"""
    driver.find_element_id_and_click_wait(driver.ele.SY_HomepageNavTab, 1)
    driver.find_element_id_and_equal_text_click(driver.ele.SC_item_favorite_group_title_iv, '我喜欢的房源')
    count = driver.with_id_and_text_get_index(driver.ele.SCE_tv_fav_detail_lu_item_title, '房间标题整体出租')
    driver.find_element_id_and_click_wait(driver.ele.SCE_iv_loop_image_item, count)
    driver.find_element_id_and_click_wait(driver.ele.XQY_ludetaillayout_booking_btn)
    has_date(driver)


def has_date(driver):
    """判断进入预订是否填写日期"""
    if driver.hasElement(driver.ele.RL_select_day_clearBtn):
        driver.swipeDown(0.5, 0.5, 0.3)
        today, newDay = toolUnits.calendar(1)
        driver.find_element_desc_click_wait(today)
        driver.find_element_desc_click_wait(newDay)
        driver.find_element_id_and_click_wait(driver.ele.RL_search_filter_more_confirm_button)


def member_pop(driver):
    """会员弹层处理"""
    if driver.hasElement(driver.ele.YD_standard_dialog_one_btn_left):
        driver.find_element_id_and_click_wait(driver.ele.YD_standard_dialog_one_btn_left)


def select_date(driver):
    """选择预订日期"""
    driver.find_element_id_and_click_wait(driver.ele.YD_rl_luBooking_checkInDays)
    driver.swipeDown(0.5, 0.5, 0.3)
    today, newDay = toolUnits.calendar(1)
    driver.find_element_desc_click_wait(today)
    driver.find_element_desc_click_wait(newDay)
    driver.find_element_id_and_click_wait(driver.ele.RL_search_filter_more_confirm_button)


def select_parent(driver):
    """选择入住人"""
    driver.find_element_id_and_click_wait(driver.ele.YD_btn_luBooking_addTenants)
    if driver.hasElement(driver.ele.RZR_iv_pickTenant_pickCheckBox):
        count = driver.with_id_and_text_get_index(driver.ele.RZR_tv_pickTenant_name, '测试')
        driver.find_element_id_and_click_wait(driver.ele.RZR_iv_pickTenant_pickCheckBox, count)
    else:
        driver.find_element_id_and_click_wait(driver.ele.RZR_ll_pickTenant_addDomesticTenant)
        add_tenant(driver)
    driver.find_element_id_and_click_wait(driver.ele.RZR_actionbarwidget_moreTextView)
    if driver.hasElement(driver.ele.RZR_dialog_selectTenantTip_leftBtn):
        driver.find_element_id_and_click_wait(driver.ele.RZR_dialog_selectTenantTip_leftBtn)
        driver.find_element_id_and_click_wait(driver.ele.RZR_actionbarwidget_moreTextView)


def add_tenant(driver):
    """添加入住人"""
    pass


def delete_tenant(driver):
    """删除入住人"""
    pass


def submit_order(driver):
    """提交订单"""
    driver.find_element_id_and_click_wait(driver.ele.YD_btn_luBooking_submitOrder_1)


def submit_pop(driver):
    """提交订单弹层处理"""
    if driver.hasElement(driver.ele.YD_btn_dialog_bookTenantTip_ok):
        driver.find_element_id_and_click_wait(driver.ele.YD_btn_dialog_bookTenantTip_ok)


if __name__ == '__main__':
    pass
