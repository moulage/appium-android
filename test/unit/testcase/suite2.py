# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:suite2.py

import os
import sys
import unittest
import HTMLTestRunner_cn
# from test.unit.common.suite_process import Suite
sys.path.append(os.path.abspath('{bastpath}{sep}..'.format(bastpath=sys.path[0], sep=os.path.sep)))


# 导入用例集
from test.unit.testcase.login_activity.password_login_activity import PassWordLogin
from test.unit.testcase.start_activity.start_activity import AA_StartAPPActivity
from test.unit.testcase.homepage_activity.home_page_activity import HomePageActivity
from test.unit.testcase.result_activity.result_activity import ResultActivity


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


"""
组件套
配置需执行的测试用例集
"""


class Suite2(unittest.TestCase):

    def run_all_test(self):
        """放置在套件里"""
        #######################################################################
        # 第一种添加用例类方式：
        # suite1 = unittest.TestLoader().loadTestsFromTestCase(AA_StartAPPActivity)
        # suite2 = unittest.TestLoader().loadTestsFromTestCase(HomePageActivity)
        # suite = unittest.TestSuite([suite1, suite2])
        # unittest.TextTestRunner(verbosity=2).run(suite)
        #######################################################################
        # 另一种添加用例套件方式：
        suite = unittest.TestSuite()
        suite.addTests(map(AA_StartAPPActivity, ['test_01_start_app_00001']))
        suite.addTest(PassWordLogin('testPassWordLogin'))
        # suites.addTests(map(PassWordLogin, ['testPassWordLogin']))
        # suites.addTests(map(HomePageActivity, ['test_02_app_79_020002_home_page_choose_domestic_hot_city_8888']))
        #######################################################################
        fp = open("AutoTesResult.html", 'wb')
        runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp, title='Test Report', description=u'Result:', retry=2)
        runner.run(suite)
        fp.close()


if __name__ == "__main__":
    Suite2().run_all_test()

