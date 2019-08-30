# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:publish_units.py

import os
from time import sleep
from testAppium.unit.common import toolUnits

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

"""
注册登录测试用例集合
"""


def input_publish_activity(driver):
    """进入发布页面并且选择新地址"""
    # 进入选择地址页面
    driver.find_element_id_and_click_wait(driver.ele.FBXT_actionbarwidget_moreTextView)
    driver.find_element_class_name_and_click('位于新地址')
    driver.find_element_id_and_click_wait(driver.ele.FBXT_actionbarwidget_moreTextView)
    # 选择国家/城市/地区
    driver.find_element_id_and_click_wait(driver.ele.FBTX_view_nationAddress_addressCreate)
    driver.find_element_id_and_click_wait(driver.ele.FBXT_regions_name)
    driver.find_element_id_and_click_wait(driver.ele.FBXT_regions_name)
    driver.find_element_id_and_click_wait(driver.ele.FBXT_regions_name)
    driver.find_element_class_name_and_click('海淀区')
    # 填写地址详情
    driver.find_element_id_and_click_wait(driver.ele.FBXT_view_addressAddress_addressCreate)
    driver.find_element_id_and_send_keys(driver.ele.FBXT_et_inputBox_publishLuDescEdit, '紫竹院街道北京理工大学2号楼小猪短租')
    driver.find_element_id_and_click_wait(driver.ele.FBXT_actionbarwidget_moreTextView)
    driver.find_element_id_and_click_wait(driver.ele.FBXT_view_numberAddress_addressCreate)
    driver.find_element_id_and_send_keys(driver.ele.FBXT_et_inputBox_publishLuDescEdit, '201')
    driver.find_element_id_and_click_wait(driver.ele.FBXT_actionbarwidget_moreTextView)

    driver.find_element_id_and_click_wait(driver.ele.FBXT_view_locationAddress_addressCreate)
    driver.swipeDown(0.5, 0.6, 0.5)
    driver.find_element_id_and_click_wait(driver.ele.FBXT_actionbarwidget_moreTextView)
    driver.find_element_id_and_click_wait(driver.ele.FBXT_btn_submit_publishLuAddressCreate)


def select_house_type(driver):
    """选择房源类型"""
    driver.find_element_id_and_click_wait(driver.ele.FBXT_iv_lu_category_item_radio)
    driver.find_element_id_and_click_wait(driver.ele.FBXT_tv_lu_category_list_commit)


def select_rent_type(driver):
    """选择出租类型"""
    driver.find_element_id_and_click_wait(driver.ele.FBXT_me_Publish_Change_Rentaltype_TypeAllIcon)
    driver.find_element_id_and_click_wait(driver.ele.FBXT_me_Publish_Change_Rentaltype_Submit)


def input_basis_message(driver):
    """输入基本信息"""
    driver.find_element_class_name_and_click('基本信息')
    driver.find_element_id_and_click_wait(driver.ele.FBXT_phi_housetype)
    driver.find_element_id_and_click_wait(driver.ele.FBXT_actv_plus)
    # driver.find_element_id_and_click_wait(driver.ele.FBXT_actv_plus, 1)
    # driver.find_element_id_and_click_wait(driver.ele.FBXT_actv_plus, 2)
    # driver.find_element_id_and_click_wait(driver.ele.FBXT_actv_plus, 3)
    # driver.find_element_id_and_click_wait(driver.ele.FBXT_actv_plus, 4)
    driver.find_element_id_and_click_wait(driver.ele.actionbarwidget_moreTextView)

    driver.find_element_id_and_click_wait(driver.ele.FBXT_phi_area)
    driver.find_element_id_and_send_keys(driver.ele.FBXT_et_lease_area, 100)
    driver.find_element_id_and_click_wait(driver.ele.actionbarwidget_moreTextView)

    driver.find_element_id_and_click_wait(driver.ele.FBXT_phi_wc)
    driver.find_element_id_and_click_wait(driver.ele.FBXT_tv_pop_window_item_name)

    driver.find_element_id_and_click_wait(driver.ele.FBXT_phi_mannum)
    driver.find_element_id_and_send_keys(driver.ele.FBXT_et_livable_number, 3)
    driver.find_element_id_and_click_wait(driver.ele.actionbarwidget_moreTextView)

    driver.find_element_id_and_click_wait(driver.ele.actionbarwidget_back)


def input_bed_message(driver):
    """输入床铺信息"""
    driver.find_element_class_name_and_click('床铺信息')
    driver.find_element_class_name_and_click('添加床铺')
    driver.find_element_id_and_click_wait(driver.ele.FBXT_tv_title_publish_lu_bed_add_item)
    driver.find_element_id_and_click_wait(driver.ele.FBXT_btn_submit_publish_lu_bed_add)
    driver.find_element_id_and_click_wait(driver.ele.actionbarwidget_back)


def input_house_describe(driver):
    """输入房源描述"""
    driver.find_element_class_name_and_click('房源描述')
    driver.find_element_id_and_click_wait(driver.ele.FBXT_tv_caption_publishLuDescListItem)
    driver.find_element_id_and_send_keys(driver.ele.FBXT_et_inputBox_publishLuDescEdit, '北京理工大学小猪短租房源测试')
    driver.find_element_id_and_click_wait(driver.ele.actionbarwidget_moreTextView)

    driver.find_element_id_and_click_wait(driver.ele.FBXT_tv_caption_publishLuDescListItem, 1)
    driver.find_element_id_and_send_keys(driver.ele.FBXT_et_inputBox_publishLuDescEdit, '你将结实一个热情、爱分享、爱读书、喜欢音乐和下厨的IT男生')
    driver.find_element_id_and_click_wait(driver.ele.actionbarwidget_moreTextView)

    driver.find_element_id_and_click_wait(driver.ele.FBXT_tv_caption_publishLuDescListItem, 2)
    driver.find_element_id_and_send_keys(driver.ele.FBXT_et_inputBox_publishLuDescEdit, '现在装饰的房间,给你不一样的感觉,让你有一种在家的温馨感受')
    driver.find_element_id_and_click_wait(driver.ele.actionbarwidget_moreTextView)

    driver.find_element_id_and_click_wait(driver.ele.FBXT_tv_caption_publishLuDescListItem, 3)
    driver.find_element_id_and_send_keys(driver.ele.FBXT_et_inputBox_publishLuDescEdit, '位于地铁口,出门就是公交站牌,方便快捷')
    driver.find_element_id_and_click_wait(driver.ele.actionbarwidget_moreTextView)

    driver.find_element_id_and_click_wait(driver.ele.FBXT_tv_caption_publishLuDescListItem, 4)
    driver.find_element_id_and_send_keys(driver.ele.FBXT_et_inputBox_publishLuDescEdit, '想玩、想吃、想喝、想蹦迪,都没有~ 哈哈哈')
    driver.find_element_id_and_click_wait(driver.ele.actionbarwidget_moreTextView)

    driver.find_element_id_and_click_wait(driver.ele.actionbarwidget_back)


def select_facility(driver):
    """选择配套设施"""
    driver.find_element_class_name_and_click('配套设施')
    driver.find_element_id_and_click_wait(driver.ele.FBXT_cb_status)
    driver.find_element_id_and_click_wait(driver.ele.FBXT_cb_status, 1)
    driver.find_element_id_and_click_wait(driver.ele.FBXT_cb_status, 2)
    driver.find_element_id_and_click_wait(driver.ele.actionbarwidget_moreTextView)


def input_money(driver):
    """输入价格规则"""
    driver.find_element_class_name_and_click('价格规则')
    driver.find_element_id_and_click_wait(driver.ele.FBXT_tv_title)
    driver.find_element_id_and_send_keys(driver.ele.FBXT_et_day_price, 10)
    driver.find_element_id_and_click_wait(driver.ele.actionbarwidget_moreTextView)
    driver.swipeDown(0.5, 0.9, 0.1)

    driver.find_element_id_and_click_wait(driver.ele.actionbarwidget_back)


def add_house_photo(driver):
    """添加房源照片"""
    driver.find_element_id_and_click_wait(driver.ele.FBXT_btn_addLuPic_publishLuMainPicItem)

    driver.find_element_id_and_click_wait(driver.ele.FBXT_lu_image_add)
    toolUnits.upload_picture(driver, 1)
    driver.swipeDown(0.5, 0.9, 0.1, 5)
    # driver.find_element_id_and_click_wait(driver.ele.FBXT_lu_image_add, -3)
    # toolUnits.upload_picture(driver, 1)
    # driver.swipeDown(0.5, 0.9, 0.1, 5)
    # driver.find_element_id_and_click_wait(driver.ele.FBXT_lu_image_add, -1)
    # toolUnits.upload_picture(driver, 5)
    # driver.swipeDown(0.5, 0.9, 0.1, 5)
    driver.find_element_id_and_click_wait(driver.ele.actionbarwidget_back)

    if driver.hasElement(driver.ele.FBXT_standard_dialog_two_btn_left):
        driver.find_element_id_and_click_wait(driver.ele.FBXT_standard_dialog_two_btn_left)


def select_home_type(driver):
    """发布页面修改房源类型"""
    driver.swipeDown(0.5, 0.7, 0.3)


def select_rent_out_type(driver):
    """发布页面修改出租类型"""
    driver.swipeDown(0.5, 0.7, 0.3)


def select_house_address(driver):
    """发布页面修改地址"""
    driver.swipeDown(0.5, 0.7, 0.3)


def select_publish_sure(driver):
    """同意发布房源"""
    driver.swipeDown(0.5, 0.7, 0.3)
    driver.find_element_id_and_click_wait(driver.ele.FBXT_switch_publishLuMainItem)
    # driver.find_element_id_and_click_wait(driver.ele.FBXT_btn_submit_publish_lu_main)


def delete_house_message(driver):
    """删除房源信息"""
    driver.swipeDown(t=1)
    driver.swipeDown()
    driver.find_element_id_and_click_wait(driver.ele.FBXT_tv_deleteLu_publishLuMainItem)
    driver.find_element_id_and_click_wait(driver.ele.FBXT_iv_delete_house_reason)
    driver.find_element_id_and_click_wait(driver.ele.FBXT_actionbarwidget_moreTextView)
    driver.find_element_id_and_click_wait(driver.ele.FBXT_bt_delete)

