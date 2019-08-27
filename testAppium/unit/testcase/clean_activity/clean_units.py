# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:clean_units.py

import os
import unittest
import sys
from testAppium.unit.common.webdriverUnit import WebdriverUnit
from testAppium.unit.common import toolUnits

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

"""
保洁操作工具
"""


def select_address(driver):
    """保洁订单选择地址页面"""
    driver.find_element_id_and_click_wait(driver.ele.BJ_cleansys_homepager_bottomBtn)
    driver.find_element_id_and_click_wait(driver.ele.BJ_clean_sys_address)
    driver.find_element_id_and_click_wait(driver.ele.BJ_room_select_radio)
    driver.find_element_id_and_click_wait(driver.ele.actionbarwidget_moreTextView)
    
    
def select_order_detail(driver):
    """保洁订单选择详情页面"""
    driver.find_element_id_and_click_wait(driver.ele.BJ_clean_sys_booking_room_item)
    driver.find_element_id_and_click_wait(driver.ele.BJ_ht_sure)
    driver.find_element_id_and_click_wait(driver.ele.BJ_clean_sys_booking_area_item)
    driver.find_element_id_and_click_wait(driver.ele.BJ_fabu_houseArea_btn_right)
    driver.find_element_id_and_click_wait(driver.ele.BJ_clean_sys_booking_time_item)
    driver.find_element_id_and_click_wait(driver.ele.BJ_cleanSys_serviceDate_rl, 4)
    driver.find_element_id_and_click_wait(driver.ele.BJ_cleanSys_serviceTime_rl, -1)
    driver.find_element_id_and_click_wait(driver.ele.BJ_clean_sys_booking_type_item)
    driver.find_element_id_and_click_wait(driver.ele.actionbarwidget_moreTextView)
    driver.find_element_id_and_click_wait(driver.ele.BJ_clean_sys_booking_wash_tools_item)
    driver.find_element_id_and_click_wait(driver.ele.actionbarwidget_moreTextView)
    clean_order_detail = [driver.get_text(driver.ele.BJ_base_msg4_desc_tv, x) for x in range(4)]
    driver.find_element_id_and_click_wait(driver.ele.actionbarwidget_moreTextView)
    driver.find_element_class_name_and_click('预约')
    return clean_order_detail


def get_order_message(driver):
    """获取订单详情页信息"""
    time = driver.get_text(driver.ele.BJ_clean_sys_booking_base_time_tv)
    room = driver.get_text(driver.ele.BJ_clean_sys_booking_base_room_tv)
    type = driver.get_text(driver.ele.BJ_clean_sys_booking_base_type_tv)
    return [time, room, type]


def input_order_pay(driver):
    """跳转至支付页面"""
    driver.swipeDown(0.5, 0.8, 0.2)
    # driver.assertIn('委托服务协议', driver.get_text(driver.ele.))
    driver.find_element_id_and_click_wait(driver.ele.BJ_clean_sys_booking_next_step_tv)
    driver.find_element_id_and_click_wait(driver.ele.BJ_go_pay_text)


def judge_order_message(first, second):
    """判断订单信息是否正确"""
    if first[0] in second[1] and first[1].split(' ')[0] in second[1] and first[2].replace('.', '-').replace('(', '（').replace(')', '）') in second[0] and first[3] in second[2] :
        return True
    return False


def input_order_list(driver):
    """进入保洁订单列表"""
    if driver.hasElement(driver.ele.BJ_cleansys_homepager_order_ongoingly):
        driver.find_element_id_and_click_wait(driver.ele.BJ_cleansys_homepager_order_ongoingly)
        driver.assertEqual(driver.ele.BJ_CleanSys_OrderListActivity, driver.driver.current_activity, '进入保洁订单列表失败')


def input_order_detail(driver):
    """进入保洁订单详情"""
    driver.find_element_id_and_click_wait(driver.ele.BJ_rl_clean_sys_content)
    driver.assertEqual(driver.ele.BJ_CleanSys_OrderDetailActivity, driver.driver.current_activity, '进入保洁订单详情失败')


def cancel_order(driver):
    """取消订单"""
    driver.find_element_class_name_and_click('取消订单')
    driver.find_element_id_and_click_wait(driver.ele.BJ_clean_sys_cancel_reason_iv)
    driver.find_element_id_and_click_wait(driver.ele.actionbarwidget_moreTextView)
    # driver.assertEqual('您已取消订单，该订单已失效', driver.get_text(driver.ele.BJ_clean_sys_tip_text), '保洁订单取消失败')


if __name__ == '__main__':
    pass



