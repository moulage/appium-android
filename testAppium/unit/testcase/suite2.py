# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:suite2.py

import os
import unittest
import sys
import time
import HTMLTestRunner_cn
from testAppium.conf.getPhoneConfig import ConfigPhoneDevices

sys.path.append(os.path.abspath('{bastpath}{sep}..'.format(bastpath=sys.path[0], sep=os.path.sep)))

from testAppium.functional.android import send_message
from testAppium.unit.testcase.start_activity import AA_StartAPPActivity
from testAppium.unit.testcase.login_activity import PassWordLogin
from testAppium.unit.testcase.homepage_activity import HomePageActivity
from testAppium.unit.testcase.result_activity import ResultActivity
from testAppium.unit.testcase.house_detail_activity import HouseDetailActivity
from testAppium.unit.testcase.book_order_activity import BookOrderActivity
from testAppium.unit.testcase.pay_activity import PayActivity
from testAppium.unit.testcase.publish_process_activity import PublishActivity
from testAppium.unit.testcase.comment_activity import TenantCommentDetailActivity
from testAppium.unit.testcase.im_activity import TenantIMDetailActivity, LandLardDetailActivity
from testAppium.unit.testcase.lock_activity import LockActivity
from testAppium.unit.testcase.clean_activity import CleanActivity


cur_path = os.path.dirname(os.path.realpath(__file__))
os.putenv("PYTHONPATH", cur_path)

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

"""
组件套
配置需执行的测试用例集
"""


class Suite2(unittest.TestCase):

    cases = {1: PassWordLogin, 2: HomePageActivity, 3: ResultActivity, 4: HouseDetailActivity, 5: PayActivity,
             6: BookOrderActivity, 7: PublishActivity, 8: TenantCommentDetailActivity, 9: TenantIMDetailActivity,
             11: LockActivity, 12: CleanActivity, 18: LandLardDetailActivity}

    def run_all_test(self):
        """放置在套件里"""
        suite = unittest.TestSuite()
        chuanru = [3]
        activity_test = ConfigPhoneDevices('ActivityConfig.ini')

        for i in chuanru:
            case = []
            for j in activity_test.get_section_items(str(i)):
                case.append(j[1])
            try:
                suite.addTests(map(self.cases[i], case))
            except Exception as e:
                send_message.DingTalkRobot().send_text(f'对应类不存在,请确认后重试: {e}')
                send_message.DingTalkRobot().send_text('监控用例--启动失败')
                return None

        tm = time.strftime("%m月%d日:%H点", time.localtime(time.time()))
        fp = open(os.path.dirname(__file__) + f'·autotest·{tm}.html', 'wb')
        runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp, title='Test Report', description=u'Result:', retry=2)
        send_message.DingTalkRobot().send_text('监控用例--开始执行')
        runner.run(suite)
        send_message.DingTalkRobot().send_text('监控用例--执行完毕')
        fp.close()


if __name__ == "__main__":
    nameConfig = ConfigPhoneDevices()
    execute_phone = sys.argv[1]
    nameConfig.set_option("EXECUTE", 'ing', execute_phone)
    nameConfig.set_option(execute_phone, "execution", "EXECUTION_ING")
    Suite2().run_all_test()
    nameConfig.set_option(execute_phone, "execution", "EXECUTION")
    # Suite2().run_all_test()

