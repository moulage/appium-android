# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:monitor_suit.py


import os
import unittest
import sys
import time
import HTMLTestRunner_cn
from test.conf.getPhoneConfig import ConfigPhoneDevices

sys.path.append(os.path.abspath('{bastpath}{sep}..'.format(bastpath=sys.path[0], sep=os.path.sep)))

from test.functional.android import send_message
from test.unit.testcase.login_activity import PassWordLogin
from test.unit.testcase.homepage_activity import HomePageActivity
from test.unit.testcase.result_activity import ResultActivity
from test.unit.testcase.house_detail_activity import HouseDetailActivity
from test.unit.testcase.book_order_activity import BookOrderActivity
from test.unit.testcase.pay_activity import PayActivity
from test.unit.testcase.publish_process_activity import PublishActivity
from test.unit.testcase.comment_activity import TenantCommentDetailActivity
from test.unit.testcase.im_activity import TenantIMDetailActivity, LandLardDetailActivity
from test.unit.testcase.lock_activity import LockActivity
from test.unit.testcase.clean_activity import CleanActivity


cur_path = os.path.dirname(os.path.realpath(__file__))
os.putenv("PYTHONPATH", cur_path)

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class MonitorSuit(unittest.TestCase):

    def monitor_test(self):
        """监控用例"""
        suite = unittest.TestSuite()
        suite.addTests(map(HomePageActivity, ['test_02_79_020002_home_page_choose_domestic_hot_city_8888',
                                              'test_02_66_020046_HomePage_SwitchToOtherPage',
                                              'test_02_72_020050_SearchPage_InputCityAndSearch',
                                              'test_02_07_home_page_input_hot_house'
                                              ]))

        suite.addTests(map(PassWordLogin, ['test_01_01_pass_word_login']))

        suite.addTests(map(ResultActivity, ['test_03_109_030017_enter_lodge_unit_detail',
                                            'test_03_256_InputChinese_SearchInList',
                                            'test_03_272_030174_SearchInMap']))
        suite.addTests(map(HouseDetailActivity, ['test_04_241_040016_HouseDetailPage_ContactLandlord',
                                                 'test_04_242_040030_HouseDetailPage_ToBookPage']))

        suite.addTests(map(BookOrderActivity, ['test_06_498_060170_TenantBookPage_JumpToWaitToConfirmPage']))

        # suite.addTests(map(PayActivity, ['test_05_504_UseAlipay',
        #                                  'test_05_505_UseWechatPay']))

        suite.addTests(map(PublishActivity, ['test_07_ToRentCalendarPageAndChangePrice_8888',
                                             'test_07_ToRentCalendarPageAndChangeState_8888',
                                             'test_07_512_PublishSuccess_whole']))

        suite.addTests(map(TenantCommentDetailActivity, ['test_08_370_100303_TenantComment_WriteComment']))

        suite.addTests(map(TenantIMDetailActivity, ['test_09_145_080242_ReceiveMsgInBackground',
                                                    'test_09_137_080216_TenantDetailSendMsg']))

        suite.addTests(map(LandLardDetailActivity, ['test_18_137_080216_LandLardDetailSendMsg',
                                                    'test_18_145_080242_ReceiveMsgInBackground']))

        suite.addTests(map(LockActivity, ['test_11_01_input_lock_activity',
                                          'test_11_08_apply_for_lock']))

        suite.addTests(map(CleanActivity, ['test_12_01_input_clean',
                                           'test_12_02_submit_clean_order']))

        suite.addTests(map(PassWordLogin, ['test_01_01_pass_word_login']))

        tm = time.strftime("%m月%d日:%H点", time.localtime(time.time()))
        fp = open(os.path.dirname(__file__) + f'·autotest·{tm}.html', 'wb')
        runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp, title='Test Report', description=u'Result:', retry=2)
        send_message.DingTalkRobot().send_text('监控用例--开始执行')
        runner.run(suite)
        send_message.DingTalkRobot().send_text('监控用例--执行完毕')
        fp.close()


if __name__ == '__main__':
    nameConfig = ConfigPhoneDevices()
    execute_phone = sys.argv[1]
    nameConfig.set_option("EXECUTE", 'ing', execute_phone)
    nameConfig.set_option(execute_phone, "execution", "EXECUTION_ING")
    MonitorSuit().monitor_test()
    nameConfig.set_option(execute_phone, "execution", "wait")
