# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:toolUnits.py

import time
import datetime
import hashlib
from selenium.webdriver.support.ui import WebDriverWait


def login_image_verification_code():
    """配置图片验证码"""
    times = "TESTAPP&&**)%" + time.strftime('%Y-%m-%d',  time.localtime())
    md5 = hashlib.md5()
    md5.update(times.encode('utf-8'))
    code = md5.hexdigest()
    return code[-4:-1] + code[-1]


def wait(drivers, element, timeouts=3):
    """等待元素出现再操作"""
    WebDriverWait(drivers, timeouts).until(lambda driver: driver.find_element_by_id(element))


def wait_text(drivers, text, timeouts=3):
    """等待元素出现再操作"""
    WebDriverWait(drivers, timeouts).until(lambda driver: driver.find_element_by_class_name(text))


def calendar(*args):
    """获取当前日历和设置添加的日历信息"""
    today = datetime.datetime.now()
    today_ = today.strftime('%Y-%m-%d')
    if len(args) == 0:
        return today_
    if len(args) == 1:
        newday = datetime.timedelta(days=args[0])
        newday_ = (today + newday).strftime('%Y-%m-%d')
        return today_, newday_
    else:
        newday = datetime.timedelta(days=args[0])
        newday_ = (today+newday).strftime('%Y-%m-%d')
        newday2 = datetime.timedelta(days=args[1])
        newday2_ = (newday + newday2).strftime('%Y-%m-%d')
        return newday_, newday2_


def change_identity(driver):
    """切换用户身份"""
    driver.find_element_id_and_click_wait(driver.ele.SY_HomepageNavTab, -1)
    driver.swipeDown(0.5, 0.9, 0.2)
    driver.find_element_id_and_click_wait(driver.ele.FKZX_tv_want2be_landlord)
    driver.swipeDown(0.5, 0.2, 0.9)


def cancel_pop(driver, times=3):
    """关闭弹层"""
    for i in range(times):
        if driver.hasElement(driver.ele.TC_fontViewContent):
            driver.find_element_id_and_click_wait(driver.ele.TC_fontViewContent)
    if driver.hasElement(driver.ele.TC_ll_global_notice_wrap):
        driver.find_element_id_and_click_wait(driver.ele.TC_fontViewContent2)


def upload_picture(driver, counts=1):
    """上传照片"""
    driver.find_element_id_and_click_wait(driver.ele.FBXT_tv_pop_window_item_name)
    driver.find_element_class_name_and_click('xzdzimages', 5)
    for i in range(counts):
        driver.find_element_id_and_click_wait(driver.ele.FBXT_iv_unselected)
    driver.find_element_id_and_click_wait(driver.ele.FBXT_comment_photos_sure)


def pay(driver):
    """支付"""
    driver.find_element_class_name_and_click('支付宝钱包支付')
    driver.assertEqual(driver.ele.ZF_ZHIFUBAO, driver.driver.current_activity, '进入支付宝支付页面失败')
    driver.backlast()
    driver.find_element_class_name_and_click('微信支付')
    driver.assertEqual(driver.ele.ZF_WEIXIN, driver.driver.current_activity, '进入微信页面失败')
    driver.backlast()


if __name__ == '__main__':
    print(login_image_verification_code())
