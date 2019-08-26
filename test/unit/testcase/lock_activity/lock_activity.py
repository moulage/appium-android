# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:lock_activity.py

import os
import unittest
import sys
from test.unit.common.webdriverUnit import WebdriverUnit
from test.unit.common import toolUnits
from test.unit.testcase.lock_activity import lock_units

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

"""
门锁测试用例集合
"""


class LockActivity(WebdriverUnit):

    def setUp(self):
        self.start_driver(userName=self.ele.land_lard_name_online, mobile=self.ele.land_lard_mobile_online, password=self.ele.land_lard_pass_word_online)
        print('开始执行--门锁--测试用例集')
        self.find_element_id_and_click_wait(self.ele.SY_HomepageNavTab, -1)
        toolUnits.change_identity(self)
        self.find_element_id_and_click_wait(self.ele.SY_HomepageNavTab, 2)
        self.assertEqual(self.ele.FWZX_LandlordCenterServiceActivity, self.driver.current_activity, '进入服务中心页面失败')
        self.find_element_id_and_click_wait(self.ele.FWZX_icon_lock_view)

    def test_11_01_input_lock_activity(self):
        """进入门锁页面正常"""
        lock_units.input_apply_for_lock(self)

    def test_11_08_apply_for_lock(self):
        """申请智能门锁"""
        lock_units.input_apply_for_lock(self)
        lock_units.apply_for_lock(self)
        self.assertEqual(self.ele.MS_Lock_OrderDetailPayActivity, self.driver.current_activity, '申请门锁没有进入支付页面')
        self.find_element_id_and_click_wait(self.ele.actionbarwidget_back)

    def test_01_18_delete_apply_for_lock(self):
        """删除门锁申请"""
        lock_units.input_apply_for_lock(self)
        lock_units.delete_lock_apply(self)

    def tearDown(self):
        print('结束执行--门锁--测试用例集')
        self.driver.quit()
