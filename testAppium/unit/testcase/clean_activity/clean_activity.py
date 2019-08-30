# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:clean_activity.py

import os
from testAppium.unit.common.webdriverUnit import WebdriverUnit
from testAppium.unit.common import toolUnits
from testAppium.unit.testcase.clean_activity import clean_units

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class CleanActivity(WebdriverUnit):
    """保洁测试用例集"""

    def setUp(self):
        self.start_driver(userName=self.ele.land_lard_name_online, mobile=self.ele.land_lard_mobile_online,
                          password=self.ele.land_lard_pass_word_online)
        print('开始执行--保洁--测试用例集')
        self.find_element_id_and_click_wait(self.ele.SY_HomepageNavTab, -1)
        toolUnits.change_identity(self)
        self.find_element_id_and_click_wait(self.ele.SY_HomepageNavTab, 2)
        self.assertEqual(self.ele.FWZX_LandlordCenterServiceActivity, self.driver.current_activity, '进入服务中心页面失败')
        self.find_element_id_and_click_wait(self.ele.FWZX_icon_clean_view)
        clean_units.input_order_list(self)
        if self.has_class_name_and_click('取消订单'):
            clean_units.cancel_order(self)
        self.backlast(1)

    def test_12_01_input_clean(self):
        """进入保洁介绍页面"""
        self.find_element_id_and_click_wait(self.ele.BJ_cleansys_homepage_banner_slogan_iv)
        self.assertEqual('小猪管家', self.get_text(self.ele.WebView_TitleBar_Title), '进入小猪管家H5介绍页面')
        for i in range(5):
            self.swipeDown(0.5, 0.9, 0.1)
        self.find_element_class_name_view_and_click('立即申请小猪管家服务')
        self.assertEqual(self.ele.BJ_CleanSys_ChoiceAddressActivity, self.driver.current_activity, 'H5申请保洁进入地址')

    def test_12_02_submit_clean_order(self):
        """提交保洁订单"""
        clean_units.select_address(self)
        clean_order_detail = clean_units.select_order_detail(self)
        order_detail = clean_units.get_order_message(self)
        clean_units.judge_order_message(clean_order_detail, order_detail)
        clean_units.input_order_pay(self)
        # toolUnits.pay(self)
        self.backlast(1)
        clean_units.input_order_list(self)
        clean_units.input_order_detail(self)
        ongoing_detail = clean_units.get_order_message(self)
        ongoing_detail[0] = ongoing_detail[0].replace('.', '-')
        self.assertEqual(order_detail, ongoing_detail)
        self.backlast()
        if self.hasElement(self.ele.standard_dialog_one_btn_right):
            self.find_element_id_and_click_wait(self.ele.standard_dialog_one_btn_right)
        clean_units.cancel_order(self)

    def test_12_03_cancel_clean_order(self):
        """取消保洁订单"""
        clean_units.input_order_list(self)

    def tearDown(self):
        print('结束执行--保洁--测试用例集')
        self.driver.quit()


if __name__ == '__main__':
    pass
