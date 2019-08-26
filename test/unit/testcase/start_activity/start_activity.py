# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui


import os
import unittest
from time import sleep
from test.unit.common.webdriverUnit import WebdriverUnit
from test.unit.common import toolUnits


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


"""
启动页面用例集
"""


class AA_StartAPPActivity(WebdriverUnit):

    def setUp(self):
        self.desired_caps['noReset'] = 'False'
        self.start_driver()
        print("开始执行--启动页面用例集")

    def test_01_start_app_00001(self):
        """点击APP跳过按钮"""
        toolUnits.wait(self.driver, self.ele.QD_splashActivity_passBtn)
        sleep(2)
        for i in range(3):
            self.swipeLeft(t=2)
            sleep(1)
        self.assertTrue(self.hasElement(self.ele.QD_splashActivity_startUseBtn), "没有滑动至启动页最后一页")
        self.swipeRight(t=2)

    # @unittest.skip('2')
    def test_01_start_app_00002(self):
        self.find_element_id_and_click_wait(self.ele.QD_splashActivity_passBtn)
        sleep(2)
        self.assertEqual(self.ele.DL_MainLoginActivity, self.driver.current_activity, '点击启动页跳过按钮没有进入登录页面')

    def tearDown(self):
        print("结束执行--启动页面用例集")
        self.driver.quit()


if __name__ == '__main__':
    print('111111111')
    suite1 = unittest.TestLoader().loadTestsFromTestCase(AA_StartAPPActivity)
    suite = unittest.TestSuite([suite1])
    unittest.TextTestRunner(verbosity=2).run(suite)


