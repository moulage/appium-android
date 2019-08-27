# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:tenant_im_activity.py

import os
from testAppium.unit.common.webdriverUnit import WebdriverUnit
from testAppium.unit.testcase.im_activity import im_units

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

"""
房客IM测试用例集合
"""


class TenantIMDetailActivity(WebdriverUnit):

    def setUp(self):
        self.start_driver()
        print('开始执行--房客IM--测试用例集')
        self.find_element_id_and_click_wait(self.ele.SY_HomepageNavTab, 2)

    def test_09_145_080242_ReceiveMsgInBackground(self):
        """房客后台收到房东消息"""
        pass

    def test_09_137_080216_TenantDetailSendMsg(self):
        """房客详情页发送消息"""
        im_units.input_tenant_im_detail(self)
        im_units.send_content(self)
        im_units.assert_send_message(self)
        im_units.assert_send_success(self)

    def tearDown(self):
        print('结束执行--房客IM--测试用例集')
        self.driver.quit()


if __name__ == '__main__':
    pass

