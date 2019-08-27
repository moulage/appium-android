# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:tenant_im_activity.py

import os
from test.unit.common.webdriverUnit import WebdriverUnit
from test.unit.testcase.im_activity import im_units
from test.unit.common import toolUnits

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

"""
房东IM测试用例集合
"""


class LandLardDetailActivity(WebdriverUnit):

    def setUp(self):
        self.start_driver(userName=self.ele.land_lard_name_online, mobile=self.ele.land_lard_mobile_online, password=self.ele.land_lard_pass_word_online)
        print('开始执行--房东IM--测试用例集')
        self.find_element_id_and_click_wait(self.ele.SY_HomepageNavTab, -1)
        toolUnits.change_identity(self)
        self.find_element_id_and_click_wait(self.ele.SY_HomepageNavTab, 3)

    def test_18_145_080242_ReceiveMsgInBackground(self):
        """房东后台收到房客消息"""
        pass

    def test_18_137_080216_LandLardDetailSendMsg(self):
        """房东详情页发送消息"""
        im_units.input_landlard_im_detail(self)
        im_units.send_content(self)
        im_units.assert_send_message(self)
        im_units.assert_send_success(self)

    def tearDown(self):
        print('结束执行--房东IM--测试用例集')
        self.driver.quit()


if __name__ == '__main__':
    pass

