# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:result_activity.py


import os
from time import sleep
from testAppium.unit.common.webdriverUnit import WebdriverUnit
from testAppium.unit.common import toolUnits
from testAppium.unit.testcase.result_activity import result_units


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class ResultActivity(WebdriverUnit):
    """结果页测试用例"""

    def setUp(self):
        self.start_driver()
        print('开始执行--结果页用例集')
        self.find_element_id_and_click_wait(self.ele.SY_HomepageNavTab)
        result_units.input_result(self)

    def test_03_109_030017_enter_lodge_unit_detail(self):
        """进入房源详情页"""
        self.find_element_id_and_click_wait(self.ele.SY_search_widget_btn_search)
        toolUnits.wait(self.driver, self.ele.JGY_tv_search_list_item_title, 5)
        house_name = self.get_text(self.ele.JGY_tv_search_list_item_title)
        self.find_element_id_and_click_wait(self.ele.JGY_iv_loop_image_item)
        self.assertEqual(house_name, self.get_text(self.ele.XQY_tv_lodge_detail_unit_name), '进入详情页失败')
        self.backlast(2)

    def test_03_256_InputChinese_SearchInList(self):
        """结果页添加地标位置推荐正常"""
        self.find_element_id_and_click_wait(self.ele.SY_search_widget_btn_search)
        toolUnits.wait(self.driver, self.ele.JGY_tv_search_list_item_title, 5)
        self.find_element_id_and_click_wait(self.ele.JGY_tv_result_page_input_box)
        localName = "天通苑"
        self.find_element_id_and_send_keys(self.ele.SS_et_search_input, localName)
        self.find_element_id_and_click_wait(self.ele.SS_pop_fxs_title)
        # self.find_element_text_and_click_wait('推荐排序')
        self.find_element_id_and_click_wait(self.ele.JGY_rl_indicator_check_time, -1)
        self.find_element_id_and_click_wait(self.ele.JGY_search_filter_orderBy_distance_tv)
        toolUnits.wait(self.driver, self.ele.JGY_tv_search_list_item_title, timeouts=3)
        houseName= self.get_text(self.ele.JGY_tv_search_list_item_title)
        # self.assertIn(localName, houseName, '输入地标位置搜索结果失败')
        self.find_element_id_and_click_wait(self.ele.JGY_iv_result_page_clear_input)
        self.assertIsNot(houseName, self.get_text(self.ele.JGY_tv_search_list_item_title))
        self.backlast(1)

    def test_03_272_030174_SearchInMap(self):
        """切换至地图页面操作"""
        self.find_element_id_and_click_wait(self.ele.SY_search_widget_btn_search)
        toolUnits.wait(self.driver, self.ele.JGY_iv_result_page_mod_switch, 5)
        self.find_element_id_and_click_wait(self.ele.JGY_iv_result_page_mod_switch)
        self.find_element_id_and_click_wait(self.ele.JGY_tv_result_page_input_box)
        localName = "天通苑"
        self.find_element_id_and_send_keys(self.ele.SS_et_search_input, localName)
        self.find_element_id_and_click_wait(self.ele.SS_pop_fxs_title, timeout=3)
        print(self.get_text(self.ele.JGY_map_address_background))
        self.assertEqual(localName, self.get_text(self.ele.JGY_map_address_background), '地图页输入地标搜索失败')
        self.backlast(1)

    def tearDown(self):
        print('结束执行--结果页用例集')
        self.driver.quit()


if __name__ == '__main__':
    pass

