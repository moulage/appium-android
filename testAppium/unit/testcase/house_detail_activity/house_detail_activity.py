# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:house_detail_activity


import os
import unittest
import sys
from time import sleep
from testAppium.unit.common.webdriverUnit import WebdriverUnit
from testAppium.unit.common import bookUnits
from testAppium.unit.testcase.house_detail_activity import house_detail_units
from testAppium.unit.common import toolUnits


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class HouseDetailActivity(WebdriverUnit):
    """房源详情页测试用例集"""

    def setUp(self):
        self.start_driver()
        print('开始执行--房源详情页--测试用例集')
        self.find_element_id_and_click_wait(self.ele.SY_HomepageNavTab)
        house_detail_units.checkInDetail(self)

    def test_04_241_040016_HouseDetailPage_ContactLandlord(self):
        """进入房源详情页，点击IM聊天按钮"""
        self.find_element_id_and_click_wait(self.ele.XQY_detail_chat_layout)
        self.assertEqual(self.ele.FKIM_TenantChatMessageActivity, self.driver.current_activity, '详情页进入IM失败')
        self.backlast(1)

    def test_04_242_040030_HouseDetailPage_ToBookPage(self):
        """进入房源详情页，点击立即预定按钮"""
        self.find_element_id_and_click_wait(self.ele.XQY_ludetaillayout_booking_btn)
        bookUnits.member_pop(self)
        self.assertEqual(self.ele.YD_LuBookingActivity, self.driver.current_activity, '详情页进入预定页面失败')
        self.backlast(1)

    def tearDown(self):
        print('结束执行--房源详情页--测试用例集')
        self.driver.quit()


if __name__ == '__main__':
    # HouseDetailActivity()
    pass
