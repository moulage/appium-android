# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:loginUnit.py


import os
from time import sleep
from functools import wraps
from testAppium.unit.common.webdriverUnit import WebdriverUnit
from testAppium.unit.element import AllElement


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


"""
登录/(退出)装饰器
"""


# driver = WebdriverUnit()
# ele = AllElement()
#
#
# def login(func):
#     @wraps(func)
#     def wrapper(*args):
#         driver.driver.find_element_id_and_click_wait(ele.QD_splashActivity_passBtn)
#         driver.find_element_id_and_click_wait(ele.DL_login_quick)
#         driver.find_element_id_and_click_wait(ele.ZD_login_change)
#         driver.find_element_id_and_send_keys(ele.MM_login_text_edit, args[0])
#         driver.find_element_id_and_send_keys(ele.MM_login_text_edit, args[1], 1)
#         if driver.driver.hasElement(ele.MM_login_text_image):
#             driver.find_element_id_and_send_keys(ele.MM_login_text_edit, "5db4", 2)
#         driver.find_element_id_and_click_wait(ele.MM_login_btn)
#         driver.assertEqual(driver.ele.SY_HomepageActivity, driver.driver.current_activity, "登录成功进入首页失败")
#         driver.find_element_id_and_click_wait(ele.TC_fontViewContent)
#     return wrapper


class Login(WebdriverUnit):

    def __init__(self, func):
        self.ele = AllElement()
        self.func = func
        # self.driver = WebdriverUnit().driver

    def __call__(self, *args):
        @wraps(self.func)
        def wrapper():
            self.find_element_id_and_click_wait(self.ele.QD_splashActivity_passBtn)
            self.find_element_id_and_click_wait(self.ele.DL_login_quick)
            self.find_element_id_and_click_wait(self.ele.ZD_login_change)
            self.find_element_id_and_send_keys(self.ele.MM_login_text_edit, args[0])
            self.find_element_id_and_send_keys(self.ele.MM_login_text_edit, args[1], 1)
            if self.driver.hasElement(self.ele.MM_login_text_image):
                self.find_element_id_and_send_keys(self.ele.MM_login_text_edit, "5db4", 2)
            self.find_element_id_and_click_wait(self.ele.MM_login_btn)
            self.assertEqual(self.ele.SY_HomepageActivity, self.driver.current_activity, "登录成功进入首页失败")
            self.find_element_id_and_click_wait(self.ele.TC_fontViewContent)
            self.func()

        return wrapper

    # def login(self, driver, login_mobile, login_password):
    #     driver.find_element_id_and_click_wait(self.ele.DL_login_quick)
    #     driver.find_element_id_and_click_wait(self.ele.ZD_login_change)
    #     driver.find_element_id_and_send_keys(self.ele.MM_login_text_edit, login_mobile)
    #     driver.find_element_id_and_send_keys(self.ele.MM_login_text_edit, login_password, 1)





