# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:book_order_activity.py

import os
from time import sleep
from test.unit.common.webdriverUnit import WebdriverUnit
from test.unit.common import toolUnits, bookUnits

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

"""
预订测试用例集合
"""


class BookOrderActivity(WebdriverUnit):

    def setUp(self):
        self.start_driver()
        print('开始执行--订单--测试用例集')
        bookUnits.cancelOrder(self)
        bookUnits.input_house_detail(self)

    def test_06_498_060170_TenantBookPage_JumpToWaitToConfirmPage(self):
        """下订单成功跳转至待确定页面"""
        bookUnits.member_pop(self)
        toolUnits.wait(self.driver, self.ele.YD_tv_luBooking_luTitle)
        bookUnits.select_parent(self)
        bookUnits.submit_order(self)
        bookUnits.submit_pop(self)
        toolUnits.wait(self.driver, self.ele.YD_WebView_TitleBar_Title, 4)
        self.assertEqual(self.get_text(self.ele.YD_WebView_TitleBar_Title), '等待房东确认', '提交订单失败')

    def tearDown(self):
        print('结束执行--订单--测试用例集')
        bookUnits.cancelOrder(self)
        self.driver.quit()


if __name__ == '__main__':
    pass
