# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui


import os
import unittest
import sys
from testAppium.unit.common.webdriverUnit import WebdriverUnit
from testAppium.unit.common import toolUnits
from testAppium.unit.testcase.login_activity import login_units

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class PassWordLogin(WebdriverUnit):
    """注册登录测试用例集"""

    def setUp(self):
        self.start_driver(need_login=False)
        print("开始执行--密码登录--测试用例集")
        self.assertEqual(self.ele.DL_MainLoginActivity, self.driver.current_activity, '点击启动页跳过按钮没有进入登录页面')
        self.find_element_id_and_click_wait(self.ele.DL_login_quick)

    def test_01_01_pass_word_login(self):
        """账号密码登录"""
        login_units.passWordLogin(self)
        self.find_element_id_and_click_wait(self.ele.MM_login_btn)
        toolUnits.cancel_pop(self)
        self.find_element_id_and_click_wait(self.ele.SY_HomepageNavTab, -1)
        toolUnits.cancel_pop(self)
        self.assertEqual(self.ele.FKGR_Me_MyselfActivityEx, self.driver.current_activity, "密码登录成功没有跳转页面失败")

    def test_01_02_verification_login(self):
        """验证码登录"""
        login_units.verificationLogin(self)
        self.find_element_id_and_click_wait(self.ele.MM_login_btn)
        toolUnits.cancel_pop(self)
        self.find_element_id_and_click_wait(self.ele.SY_HomepageNavTab, -1)
        toolUnits.cancel_pop(self)
        self.assertEqual(self.ele.FKGR_Me_MyselfActivityEx, self.driver.current_activity, "验证码登录成功没有跳转页面失败")

    def tearDown(self):
        print("结束执行--密码登录--测试用例集")
        self.driver.quit()


if __name__ == '__main__':
    result = unittest.TextTestResult(sys.stdout, 'test result', 1)
    suites = unittest.TestSuite()
    suites.addTest(PassWordLogin('testPassWord'))
    suites.run(result)
