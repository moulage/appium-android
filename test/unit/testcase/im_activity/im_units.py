# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:im_units.py

import os
import random
from test.unit.common import toolUnits

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

"""
IM操作工具
"""


def get_code():
    val = random.randint(0x4e00, 0x9fbf)
    return chr(val)


code = get_code()
tenant_send_message = 'my name 小猪,how are you?' + code
landLard_send_message = 'my name 小猪房东,how are you?' + code
IMName = '房间标题整体出租'


def input_tenant_im_detail(driver, IMName='房间标题整体出租'):
    """进入IM详情页"""
    driver.find_element_class_name_and_click(IMName)
    if driver.hasElement(driver.ele.RL_select_day_clearBtn):
        today, newDay = toolUnits.calendar(2)
        driver.find_element_desc_click_wait(today)
        driver.find_element_desc_click_wait(newDay)
        driver.find_element_id_and_click_wait(driver.ele.RL_search_filter_more_confirm_button)
        toolUnits.wait(driver.driver, driver.ele.FKIM_ed_input)
    driver.assertEqual(driver.ele.FKIM_TenantChatMessageActivity, driver.driver.current_activity, '进入IM详情页失败')


def input_landlard_im_detail(driver, tenantName='小猪玩起来'):
    """进入IM详情页"""
    driver.find_element_class_name_and_click(tenantName)
    toolUnits.wait(driver.driver, driver.ele.FKIM_ed_input)
    driver.assertEqual(driver.ele.FDIM_LandLordChatMessageActivityy, driver.driver.current_activity, '进入IM详情页失败')


def send_content(driver, identity=1):
    """
    输入文本发送消息
    :param driver: 对象
    :param identity:  1 房客
                      2 房东
    """
    driver.find_element_id_and_click_wait(driver.ele.FKIM_ed_input)
    if identity == 1:
        driver.find_element_id_and_send_keys(driver.ele.FKIM_ed_input, tenant_send_message)
    else:
        driver.find_element_id_and_send_keys(driver.ele.FKIM_ed_input, landLard_send_message)
    driver.find_element_id_and_click_wait(driver.ele.FKIM_tv_send)


def assert_send_message(driver, identity=1):
    """
    判断发送信息是否正确
    :param driver: 对象
    :param identity:  1 房客
                      2 房东
    """
    if identity == 1:
        content = driver.get_text(driver.ele.FKIM_tv_chatText, -1)
        driver.assertEqual(tenant_send_message, content, '房客发送信息失败')
    else:
        content = driver.get_text(driver.ele.FKIM_tv_chatText, -1)
        driver.assertEqual(landLard_send_message, content, '房东发送IM失败')


def assert_send_success(driver):
    """
    判断发送信息是否成功
    :param driver: 对象
    """
    driver.find_element_id_and_click_wait(driver.ele.FKIM_iv_promotional_pop_window_back_button)
    content = driver.get_text(driver.ele.FKIM_tv_house_content)
    driver.assertEqual(IMName, content, '房客发送IM失败')
