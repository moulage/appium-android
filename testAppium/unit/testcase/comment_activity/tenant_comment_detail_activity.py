# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:tenant_comment_detail_activity

import os
from testAppium.unit.common.webdriverUnit import WebdriverUnit
from testAppium.unit.testcase.comment_activity import comment_units

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

"""
房客点评详情页测试用例集合
"""


class TenantCommentDetailActivity(WebdriverUnit):

    def setUp(self):
        self.start_driver()
        print("开始执行--房客点评详情页--测试用例集")
        self.find_element_id_and_click_wait(self.ele.SY_HomepageNavTab, 3)
        self.swipeDown(0.5, 0.6, 0.2)
        self.find_element_class_name_and_click('点评')
        self.find_element_id_and_click_wait(self.ele.FKDP_tv_fkCommentList_item_startDate)

    def test_08_370_100303_TenantComment_WriteComment(self):
        """房客点评流程"""
        action = comment_units.has_comment_action(self)
        if action == 1:
            self.swipeDown(0.5, 0.6, 0.4)
            comment_units.delete_common(self)
        comment_units.common_order(self)
        comment_units.assert_common(self)

    def tearDown(self):
        print("结束执行--房客点评详情页--测试用例集")
        comment_units.delete_common(self)
        self.driver.quit()


if __name__ == '__main__':
    pass
