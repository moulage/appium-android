# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui

import os
import sys
import unittest
from appium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from testAppium.conf.getPhoneConfig import ConfigPhoneDevices
from testAppium.unit.element import AllElement
from testAppium.unit.common import toolUnits


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


"""
初始化测试用例
并且封装所有的公共方法
"""


class WebdriverUnit(unittest.TestCase):

    ele = AllElement()

    @classmethod
    def setUpClass(cls):
        """初始化获取的手机设备参数"""

        # cls.pName = sys.argv(1)
        cls.nameConfig = ConfigPhoneDevices()
        cls.phone_name = cls.nameConfig.get_section_password('EXECUTE', 'ing')
        cls.phoneConfig = cls.nameConfig.get_section_items(cls.phone_name)  # cls.pName
        cls.desired_caps = {'platformName': 'Android',
                            'platformVersion': cls.phoneConfig[0][1],
                            'deviceName': cls.phoneConfig[1][1],
                            'appPackage': 'com.xiaozhu.xzdz',
                            'appActivity': '.shell.XZLauncher_XZAlias0',
                            'noReset': 'True'
                            }

    def start_driver(self, need_login=True, userName=ele.tenant_user_name_online, **kwargs):
        """启动APP 定义driver"""
        self.driver = webdriver.Remote(self.phoneConfig[2][1], self.desired_caps)
        self.start_dispose()
        if need_login:
            '''需要登录'''
            if not self.judge_login(userName):
                '''判断登录信息是否正确， 正确--则继续执行  错误--检查是否已经登录'''
                if self.hasElement(self.ele.SY_HomepageNavTab):
                    '''已经登录，则退出重新登录'''
                    self.logout()
                self.login_tenant(**kwargs)
            self.find_element_id_and_click_wait(self.ele.SY_HomepageNavTab, -1)
            if not self.hasElement(self.ele.FKZX_tv_me_name_fk):
                '''确保切换至房客身份'''
                toolUnits.change_identity(self)
        else:
            '''不需要登录'''
            if self.hasElement(self.ele.SY_HomepageNavTab):
                '''已经登录，则退出重新登录'''
                self.logout()

    def start_dispose(self):
        """点击启动APP权限弹层"""
        sleep(1)
        for x in range(4, len(self.phoneConfig)):
            if self.hasElement(self.phoneConfig[x][1]):
                self.driver.find_element(By.ID, self.phoneConfig[x][1]).click()
                sleep(1)
        sleep(2)

    def getDriver(self):
        """返回一个driver对象"""
        return self.driver

    def judge_login(self, userName):
        """
        判断用户登录信息是否正确
        :param userName:  登录的用户名称
        :return: 登录状态
        """
        if self.hasElement(self.ele.SY_HomepageNavTab):
            self.find_element_id_and_click_wait(self.ele.SY_HomepageNavTab, -1)
            if self.get_text(self.ele.FKZX_tv_me_name_fk) == userName or self.get_text(
                    self.ele.FDZX_tv_me_name_fd) == userName:
                return True
        return False

    def open_lock(self):
        """打开屏幕"""
        self.driver.unlock()

    def close_lock(self):
        """关闭屏幕时长"""
        self.driver.lock(2)

    def background(self):
        """放置后台时长"""
        self.driver.background_app(2)

    def backlast(self, times=1):
        """返回上一页"""
        for i in range(times):
            if self.hasElement(self.ele.YD_standard_dialog_one_btn_right):
                self.find_element_id_and_click_wait(self.ele.YD_standard_dialog_one_btn_right)
            self.driver.back()

    def end_dispose(self):
        """进入首页需获取权限"""
        sleep(1)
        for x in range(3, len(self.phoneConfig)):
            if self.hasElement(self.phoneConfig[x][1]):
                self.driver.find_element(By.ID, self.phoneConfig[x][1]).click()
                sleep(1)

    def login_tenant(self, mobile=ele.tenant_user_mobile_online, password=ele.tenant_user_pass_word_online, home=1):
        """需要登录的用例执行"""
        if self.hasElement(self.ele.DL_login_quick):
            self.find_element_id_and_click_wait(self.ele.DL_login_quick)
            self.find_element_id_and_click_wait(self.ele.ZD_login_change)
            self.find_element_id_and_send_keys(self.ele.MM_login_text_edit, mobile)
            self.find_element_id_and_send_keys(self.ele.MM_login_text_edit, password, 1)
            if self.hasElement(self.ele.MM_login_text_image):
                self.find_element_id_and_send_keys(self.ele.MM_login_text_edit, toolUnits.login_image_verification_code(), 2)
            self.find_element_id_and_click_wait(self.ele.MM_login_btn)
            self.end_dispose()
            toolUnits.cancel_pop(self, 1)
            if home == 1:
                self.find_element_id_and_click_wait(self.ele.SY_HomepageNavTab)
                toolUnits.cancel_pop(self, 3)

    def logout(self):
        """（强制）退出登录"""
        for i in range(10):
            if self.hasElement(self.ele.SY_HomepageNavTab):
                break
            self.backlast()
        self.find_element_id_and_click_wait(self.ele.SY_HomepageNavTab, -1)
        if not self.hasElement(self.ele.FKGR_iv_me_setting):
            self.swipeUp(0.5, 0.1, 0.9)
        self.find_element_id_and_click_wait(self.ele.FKGR_iv_me_setting)
        self.find_element_id_and_click_wait(self.ele.SZ_my_exit)

    # def closeDriver(self):
    #     """关闭driver"""
    #     self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        """关闭driver"""
        pass

    # 元素操作部分
    def find_element_id_and_click_wait(self, by, index=0, timeout=2):
        """
        识别ID 并点击
        by: 元素坐标
        index: 元素位置
        """
        drive_item = self.driver.find_elements(By.ID, f"com.xiaozhu.xzdz:id/{by}")[index]
        drive_item.click()
        sleep(timeout)

    def find_element_id_and_equal_text_click(self, by, text, timeout=2):
        """
        获取ID组，点击元素text对应的元素
        :param by: 元素坐标
        :param text: 元素内容
        :param times: 时间
        :return:
        """
        drive_items = self.driver.find_elements(By.ID, f"com.xiaozhu.xzdz:id/{by}")
        for num, drive_item in enumerate(drive_items):
            if drive_item.text == text:
                drive_item.click()
                break
        sleep(timeout)

    def find_element_text_and_click_wait(self, text, index=0, timeout=2):
        """
        识别TAG_NAME 并点击
        text: 元素名称
        index: 元素位置
        """
        drive_item = self.driver.find_elements(By.NAME, text)[index]
        drive_item.click()
        sleep(timeout)

    def find_element_desc_click_wait(self, text, index=0, timeout=2):
        """
        识别TAG_NAME 并点击
        text: 元素名称
        index: 元素位置
        """
        drive_item = self.driver.find_elements_by_accessibility_id(text)[index]
        drive_item.click()
        sleep(timeout)

    def find_element_id_and_send_keys(self, by, send_key, index=0):
        """
        识别元素ID 并输入
        by: 元素坐标
        send_key: 输入内容
        index: 元素位置
        """
        drive_item = self.driver.find_elements(By.ID, f"com.xiaozhu.xzdz:id/{by}")[index]
        drive_item.send_keys(send_key)
        sleep(0.5)

    def find_element_class_name_and_click(self, text, times=3):
        """
        获取class_name对应的文本并且点击
        :text 文本内容
        """
        driver_item = self.driver.find_elements_by_class_name('android.widget.TextView')
        for index, name in enumerate(driver_item):
            if name.text == text:
                name.click()
                sleep(1)
                return
        if times != 0:
            self.swipeDown(0.5, 0.6, 0.2)
            self.find_element_class_name_and_click(text, times=times-1)

    def find_element_class_name_view_and_click(self, text, times=3):
        """
        获取class_name对应的文本并且点击
        :text 文本内容
        """
        driver_item = self.driver.find_elements_by_class_name('android.view.View')
        for index, name in enumerate(driver_item):
            if name.text == text:
                name.click()
                sleep(1)
                return
        if times != 0:
            self.swipeDown(0.5, 0.6, 0.2)
            self.find_element_class_name_and_click(text, times=times-1)

    def find_element_class_name_image_and_click(self, timeout=1):
        """
        获取class_name对应的image并且点击
        """
        driver_name = self.driver.find_elements_by_class_name('android.widget.ImageView')[0]
        driver_name.click()
        sleep(timeout)

    def click_centre(self, orgin_x=0.5, orgin_y=0.5, duration=100):
        """点击页面坐标"""
        le = self.driver.getsize()
        x = int(le[0] * orgin_x)  # 起始x坐标
        y = int(le[1] * orgin_y)  # 终点x坐标
        self.driver.tap([(x, y), (x, y)], duration)

    def has_class_name_and_click(self, text):
        """
        判断当前页面是否有此文本内容
        :text 文本内容
        """
        driver_item = self.driver.find_elements_by_class_name('android.widget.TextView')
        for index, name in enumerate(driver_item):
            if name.text == text:
                return True
        return False

    def get_text(self, by, index=0):
        """
        通过id获取元素的text
        :param element: 元素ID
        :return: text
        """
        if self.hasElement(by):
            text = self.driver.find_elements(By.ID, f"com.xiaozhu.xzdz:id/{by}")[index].text
            return text
        else:
            return None

    def with_id_and_text_get_index(self, by, text, swiptimes=3):
        """
        获取元素的text
        :param element: 元素ID
        :return: text
        """
        for i in range(swiptimes):
            driver_item = self.driver.find_elements(By.ID, f"com.xiaozhu.xzdz:id/{by}")
            for index, name in enumerate(driver_item):
                if name.text == text:
                    return index
            self.with_id_and_text_get_index(by, text, swiptimes=swiptimes-1)
        return None

    def hasElement(self, element):
        """判断元素是否存在"""
        source = self.driver.page_source
        if element in source:
            return True
        else:
            return False

    def swipe_to_text(self, text, times=3):
        """滑动至文本位置"""
        for i in range(times):
            if self.has_class_name_and_click(text):
                return True
            self.swipeDown(0.5, 0.8, 0.2)

    def swipe_to_id(self, by, times=3):
        """滑动至文本位置"""
        for i in range(times):
            if self.hasElement(by):
                return True
            self.swipeDown(0.5, 0.8, 0.2)

    def swipeUp(self, orgin_x=0.5, orgin_y=0.2, destination_y=0.8, t=2):
        """向上滑动页面"""
        le = self.driver.getsize()
        x1 = int(le[0] * orgin_x)  # 起始x坐标
        y1 = int(le[1] * orgin_y)  # 起始y坐标
        y2 = int(le[1] * destination_y)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, t * 1000)

    def swipeDown(self, orgin_x=0.5, orgin_y=0.8, destination_y=0.2, t=2):
        """向下滑动页面"""
        le = self.driver.getsize()
        x1 = int(le[0] * orgin_x)  # 起始x坐标
        y1 = int(le[1] * orgin_y)  # 起始y坐标
        y2 = int(le[1] * destination_y)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, t * 1000)

    def swipeLeft(self, orgin_x=0.9, destination_x=0.1, orgin_y=0.5, t=2):
        """向左滑动页面"""
        le = self.driver.getsize()
        x1 = int(le[0] * orgin_x)  # 起始x坐标
        x2 = int(le[0] * destination_x)  # 终点x坐标
        y1 = int(le[1] * orgin_y)  # 起始y坐标
        self.driver.swipe(x1, y1, x2, y1, t * 1000)

    def swipeRight(self, orgin_x=0.1, destination_x=0.9, orgin_y=0.5, t=2):
        """向右滑动页面"""
        le = self.driver.getsize()
        x1 = int(le[0] * orgin_x)  # 起始x坐标
        x2 = int(le[0] * destination_x)  # 终点x坐标
        y1 = int(le[1] * orgin_y)  # 起始y坐标
        self.driver.swipe(x1, y1, x2, y1, t * 1000)


if __name__ == "__main__":
    pass
