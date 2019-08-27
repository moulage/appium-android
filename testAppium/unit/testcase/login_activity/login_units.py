# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:login_units.py

import os
from testAppium.unit.common import toolUnits, url_request

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

"""
注册登录工具
"""


def passWordLogin(driver):
    """账号密码登录"""
    driver.find_element_id_and_click_wait(driver.ele.ZD_login_change)
    driver.find_element_id_and_send_keys(driver.ele.MM_login_text_edit, "18710463392")
    driver.find_element_id_and_send_keys(driver.ele.MM_login_text_edit, "jiehui89.", 1)
    if driver.hasElement(driver.ele.MM_login_text_image):
        driver.find_element_id_and_send_keys(driver.ele.MM_login_text_edit, toolUnits.login_image_verification_code(), 2)


def verificationLogin(driver):
    """验证码登录"""
    mobile = '17610893392'
    driver.find_element_id_and_send_keys(driver.ele.ZD_login_text_content, mobile)
    code = url_request.get_mobile_verification_code(mobile)
    if isinstance(code, bool):
        if driver.get_text(driver.ele.ZD_login_text_text) == '获取验证码':
            driver.find_element_id_and_click_wait(driver.ele.ZD_login_text_text)
        code = url_request.get_mobile_verification_code(mobile)
    driver.find_element_id_and_send_keys(driver.ele.ZD_login_text_content, code, 1)


if __name__ == '__main__':
    pass
