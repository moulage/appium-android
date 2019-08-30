# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:publish_process_activity

import os, time
from time import sleep
from testAppium.unit.common.webdriverUnit import WebdriverUnit
from testAppium.unit.common import toolUnits
from testAppium.unit.testcase.publish_process_activity import publish_units

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class PublishActivity(WebdriverUnit):
    """发布测试用例集"""

    def setUp(self):
        self.start_driver()
        print("开始执行--发布系统--测试用例集")
        today = toolUnits.calendar()
        print(today)
        self.find_element_id_and_click_wait(self.ele.SY_HomepageNavTab, -1)
        self.swipeDown(0.5, 0.9, 0.1)
        self.find_element_id_and_click_wait(self.ele.FKZX_tv_want2be_landlord)
        self.find_element_id_and_click_wait(self.ele.SY_HomepageNavTab, 1)
        self.assertEqual(self.ele.FBXT_PublishListingActivity, self.driver.current_activity, '进入发布房源列表页面错误')

    def test_07_ToRentCalendarPageAndChangePrice_8888(self):
        """修改日历价格"""
        self.find_element_class_name_and_click('出租日历')
        self.swipeDown(0.5, 0.6, 0.4)
        today = toolUnits.calendar()
        print(today)
        self.find_element_desc_click_wait(today)
        if '￥' not in self.get_text(self.ele.FBXT_tv_landlord_calendar_price):
            self.find_element_id_and_click_wait(today, 1)
            self.find_element_class_name_and_click('修改房态')
            self.find_element_id_and_click_wait(self.ele.FBXT_tv_hire)
            self.find_element_desc_click_wait(today)
        self.find_element_class_name_and_click('修改价格')
        sleep(1)
        self.find_element_id_and_send_keys(self.ele.FBXT_xztv_input_price, send_key=10)
        self.find_element_id_and_click_wait(self.ele.FBXT_xztv_input_btn_right)
        self.assertEqual('￥10', self.get_text(self.ele.FBXT_tv_landlord_calendar_price), '修改日历日价失败')

        self.find_element_desc_click_wait(today)
        self.find_element_class_name_and_click('修改价格')
        self.find_element_id_and_send_keys(self.ele.FBXT_xztv_input_price, send_key=1)
        self.find_element_id_and_click_wait(self.ele.FBXT_xztv_input_btn_right)
        self.assertEqual('￥1', self.get_text(self.ele.FBXT_tv_landlord_calendar_price), '修改日历日价失败')

    def test_07_ToRentCalendarPageAndChangeState_8888(self):
        """修改日历状态"""
        self.find_element_class_name_and_click('出租日历')
        self.swipeDown(0.5, 0.6, 0.4)
        today = toolUnits.calendar()
        self.find_element_desc_click_wait(today)
        self.find_element_class_name_and_click('修改房态')
        sleep(1)
        self.find_element_id_and_click_wait(self.ele.FBXT_tv_hire_no)
        toolUnits.wait(self.driver, self.ele.FBXT_tv_landlord_calendar_price)
        self.assertNotIn("￥", self.get_text(self.ele.FBXT_tv_landlord_calendar_price), '修改关闭日历房态失败')
        self.find_element_desc_click_wait(today)
        self.find_element_class_name_and_click('修改房态')
        sleep(1)
        self.find_element_id_and_click_wait(self.ele.FBXT_tv_hire_yes)
        self.assertIn("￥", self.get_text(self.ele.FBXT_tv_landlord_calendar_price), '修改打开日历房态失败')

    def test_07_512_PublishSuccess_whole(self):
        """发布房源"""
        publish_units.input_publish_activity(self)
        publish_units.select_house_type(self)
        publish_units.select_rent_type(self)
        publish_units.input_basis_message(self)
        publish_units.input_bed_message(self)
        publish_units.input_house_describe(self)
        publish_units.select_facility(self)
        publish_units.input_money(self)
        publish_units.add_house_photo(self)
        publish_units.select_publish_sure(self)

        publish_units.delete_house_message(self)

    def test_07_delete_house(self):
        """删除房源"""
        if self.has_class_name_and_click('继续发布'):
            self.find_element_class_name_and_click('继续发布')
            publish_units.delete_house_message(self)
            self.test_07_delete_house()

    def tearDown(self):
        print("结束执行--发布系统--测试用例集")
        self.driver.quit()


if __name__ == '__main__':
    pass
