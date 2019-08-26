# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:pay_activity.py

import os
from test.unit.common.webdriverUnit import WebdriverUnit
from test.unit.common import toolUnits, orderUnit, bookUnits

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

"""
支付测试用例集合
"""


class PayActivity(WebdriverUnit):

    def setUp(self):
        self.start_driver()
        bookUnits.cancelOrder(self)
        print('开始执行--支付--用例测试集')
        self.orderId = orderUnit.Place_order()
        # 判断是否下单成功
        if self.orderId == 2:
            return False

        # 房东接受订单
        self.login_tenant(mobile=self.ele.land_lard_mobile_online, password=self.ele.land_lard_pass_word_online, home=2)
        toolUnits.change_identity(self)
        toolUnits.cancel_pop(self)
        bookUnits.aeecptOrder(self)
        self.logout()

    def test_05_504_UseAlipay(self):
        """使用支付宝支付"""
        print('支付宝支付功能尚未开通')

    def test_05_505_UseWechatPay(self):
        """使用微信支付"""
        print('微信支付功能尚未开通')

    def tearDown(self):
        print('结束执行--支付--用例测试集')
        cancel = orderUnit.Cancellation_order()
        if cancel:
            print('取消订单成功')
        self.driver.quit()


if __name__ == '__main__':
    pass
