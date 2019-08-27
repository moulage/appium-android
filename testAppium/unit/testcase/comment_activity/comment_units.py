# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:comment_units.py

import os
from time import sleep
from testAppium.unit.common import toolUnits

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

"""
点评操作库
"""


text_content = "testNg 测试点评是否正常。。。 我感觉没有毛病，哥们"


def input_detail(driver):
    """点评进入详情页"""
    driver.find_element_id_and_click_wait(driver.ele.FKDP_tv_fkCommentList_item_startDate)


def has_comment_action(driver):
    """
    当前订单是否已经点评
    :param driver:
    :return: 0 未点评
             1 已点评
             2 已过期
    """
    if driver.hasElement(driver.ele.FKDP_tv_fkCommentDetail_noComment_tip):
        text = driver.get_text(driver.ele.FKDP_tv_fkCommentDetail_noComment_tip)
        if text == '已过点评有效期':
            return 2
        else:
            return 0
    return 1


def comment_action(driver):
    """
    查看订单状态
    :param driver:
    :return: 0 未点评
             1 已点评
             2 已过期
    """
    text = driver.get_text(driver.ele.FKDP_tv_fkCommentList_item_orderState)
    if text == '待点评':
        return 0
    elif text == '已点评':
        return 1
    elif text == '已过期':
        return 2
    else:
        return


def common_order(driver, photo=True):
    """房客填写点评内容"""
    driver.find_element_id_and_click_wait(driver.ele.FKDP_btn_fkCommentDetail_gotoWriteComment)
    driver.find_element_id_and_click_wait(driver.ele.FKDP_commitStart_start5)
    driver.find_element_id_and_click_wait(driver.ele.FKDP_commitStart_start4, 1)
    driver.find_element_id_and_click_wait(driver.ele.FKDP_commitStart_start3, 2)
    driver.find_element_id_and_click_wait(driver.ele.FKDP_commitStart_start2, 3)
    driver.find_element_id_and_click_wait(driver.ele.FKDP_commitStart_start1, 4)
    driver.find_element_id_and_send_keys(driver.ele.FKDP_et_fkCommentPublish_contentInput, text_content)
    if photo:
        common_photo(driver)
    driver.find_element_id_and_click_wait(driver.ele.actionbarwidget_moreTextView)
    if driver.hasElement(driver.ele.FKDP_firsttip_go_refuse):
        driver.find_element_id_and_click_wait(driver.ele.FKDP_firsttip_go_refuse)
    if driver.hasElement(driver.ele.FKDP_feedback_coupon):
        driver.find_element_id_and_click_wait(driver.ele.WebView_TitleBar_BackImg)


def common_photo(driver):
    """点评添加图片"""
    if driver.hasElement(driver.ele.FKDP_iv_commentPublish_picture):
        driver.find_element_id_and_click_wait(driver.ele.FKDP_iv_commentPublish_picture, -1)
    else:
        driver.find_element_id_and_click_wait(driver.ele.FKDP_tv_fkCommentPublish_addPicture_tip)
    driver.find_element_id_and_click_wait(driver.ele.FKDP_rl_pop_window_item)
    driver.find_element_class_name_and_click('xzdzimages', 5)
    driver.find_element_id_and_click_wait(driver.ele.FBXT_iv_unselected)
    driver.find_element_id_and_click_wait(driver.ele.FBXT_comment_photos_sure)
    driver.swipeDown(0.5, 0.6, 0.4, 4)


def assert_common(driver):
    """判断点评内容是否正确"""
    driver.assertEqual("整洁卫生    5分", driver.get_text(driver.ele.FKDP_tv_fkCommentDetail_sanitationScore), '点评整洁卫生错误')
    driver.assertEqual("交通位置    3分", driver.get_text(driver.ele.FKDP_tv_fkCommentDetail_locationScore), '点评整洁卫生错误')
    driver.assertEqual("性价比空    1分", driver.get_text(driver.ele.FKDP_tv_fkCommentDetail_performanceScore), '点评整洁卫生错误')
    driver.assertEqual("安全程度    4分", driver.get_text(driver.ele.FKDP_tv_fkCommentDetail_securityScore), '点评整洁卫生错误')
    driver.assertEqual("描述相符    2分", driver.get_text(driver.ele.FKDP_tv_fkCommentDetail_descriptionScore), '点评整洁卫生错误')
    driver.assertEqual("描述相符    2分", driver.get_text(driver.ele.FKDP_tv_fkCommentDetail_descriptionScore), '点评整洁卫生错误')
    driver.assertEqual(text_content, driver.get_text(driver.ele.FKDP_tv_fkCommentDetail_fkCommentContent), '点评整洁卫生错误')


def delete_common(driver):
    """删除点评"""
    if driver.hasElement(driver.ele.FKDP_tv_fkCommentDetail_fkCommentDel):
        driver.find_element_id_and_click_wait(driver.ele.FKDP_tv_fkCommentDetail_fkCommentDel)
        driver.find_element_id_and_click_wait(driver.ele.standard_dialog_one_btn_right)

