# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui


import os, time
from testAppium.unit.common.webdriverUnit import WebdriverUnit
from testAppium.unit.common import toolUnits


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


"""
首页测试用例集
"""


class HomePageActivity(WebdriverUnit):

    def setUp(self):
        self.start_driver()
        self.find_element_id_and_click_wait(self.ele.SY_HomepageNavTab)
        print('开始执行--首页用例集')

    def test_02_01_home_page_input_action(self):
        """首页进入首页轮播图"""
        self.click_centre()
        self.assertEqual(True, self.hasElement(self.ele.SY_WebView_SucessLayout), '首页进入活动页面失败')
        self.backlast(2)
        self.assertEqual(self.ele.SY_HomepageActivity, self.driver.current_activity, '活动返回首页失败')

    def test_02_02_home_page_channel(self):
        """首页进入五大频道页面"""
        self.find_element_id_and_click_wait(self.ele.SY_home_page_entry_0)
        self.backlast(1)
        self.assertEqual(self.ele.SY_HomepageActivity, self.driver.current_activity, '频道一返回首页失败')
        self.find_element_id_and_click_wait(self.ele.SY_home_page_entry_1)
        self.backlast(1)
        self.assertEqual(self.ele.SY_HomepageActivity, self.driver.current_activity, '频道二返回首页失败')
        self.find_element_id_and_click_wait(self.ele.SY_home_page_entry_2)
        self.backlast(1)
        self.assertEqual(self.ele.SY_HomepageActivity, self.driver.current_activity, '频道三返回首页失败')
        self.find_element_id_and_click_wait(self.ele.SY_home_page_entry_3)
        self.backlast(1)
        self.assertEqual(self.ele.SY_HomepageActivity, self.driver.current_activity, '频道四返回首页失败')
        self.find_element_id_and_click_wait(self.ele.SY_home_page_entry_4)
        self.backlast(1)
        self.assertEqual(self.ele.SY_HomepageActivity, self.driver.current_activity, '频道五返回首页失败')

    def test_02_03_home_page_hot_city(self):
        """首页进入热门城市结果页"""
        self.swipe_to_id(self.ele.SY_tab_itemHomeV4HotCity)
        toolUnits.cancel_pop(self, 1)
        # self.find_element_id_and_click_wait(self.ele.SY_text1, 1)
        self.find_element_id_and_click_wait(self.ele.SY_rv_itemHomeV4HotCity)
        self.assertEqual(self.ele.JGY_SearchResulitActivity, self.driver.current_activity, '首页点击推荐城市进入结果页失败')
        self.backlast(1)
        self.assertEqual(self.ele.SY_HomepageActivity, self.driver.current_activity, '推荐城市结果页返回首页失败')

    def test_02_04_home_page_input_action(self):
        """首页进入中部运营活动位"""
        self.swipe_to_text('大 家 都 在 玩')
        self.find_element_id_and_click_wait(self.ele.SY_pager_itemOperationHomeV4)
        self.assertEqual(True, self.hasElement(self.ele.SY_WebView_SucessLayout), '首页进入中部运营活动页面失败')
        self.backlast(1)
        self.assertEqual(self.ele.SY_HomepageActivity, self.driver.current_activity, '中部运营活动返回首页失败')

    def test_02_05_home_page_input_operation(self):
        """首页进入中部运营位"""
        self.swipe_to_id(self.ele.SY_frame_container_itemHomeV4)
        self.find_element_class_name_and_click('商旅合作')
        self.assertEqual(True, self.hasElement(self.ele.SY_WebView_SucessLayout), '首页进入商旅合作失败')
        self.backlast(1)
        self.assertEqual(self.ele.SY_HomepageActivity, self.driver.current_activity, '商旅合作返回首页失败')

    def test_02_06_home_page_input_xzdz_story(self):
        """首页进入小猪故事"""
        self.swipe_to_text('小 猪 故 事')
        self.find_element_id_and_click_wait(self.ele.SY_img_itemHomeV4History)
        self.assertEqual('小猪故事', self.get_text(self.ele.actionbarwidget_title), '首页进入小猪故事页面失败')
        self.find_element_id_and_click_wait(self.ele.SY_iv_our_story_item_pic)
        self.swipeDown(0.5, 0.9, 0.1, 1)
        self.find_element_id_and_click_wait(self.ele.SY_iv_black_back)
        self.swipeDown(0.5, 0.9, 0.1, 1)
        self.backlast(1)
        self.assertEqual(self.ele.SY_HomepageActivity, self.driver.current_activity, '小猪故事返回首页失败')

    def test_02_07_home_page_input_hot_house(self):
        """首页进入热门房源"""
        for i in range(5):
            self.swipeDown(0.5, 0.8, 0.2)
        self.assertTrue(self.hasElement(self.ele.SY_tab_itemHomeV4HotRoom), '首页滑动至底部失败')
        self.find_element_id_and_click_wait(self.ele.SY_img_homeV4ItemHotCity)
        self.assertEqual(self.ele.XQY_NewLuDetailActivity, self.driver.current_activity, '首页进入热门房源失败')
        self.backlast(1)
        self.assertEqual(self.ele.SY_HomepageActivity, self.driver.current_activity, '热门房源返回首页失败')
        time.sleep(1)
        for i in range(5):
            self.swipeUp(0.5, 0.3, 0.8)
        self.assertTrue(self.hasElement(self.ele.SY_home_page_entry_0), '首页滑动至顶部失败')

    def test_02_79_020002_home_page_choose_domestic_hot_city_8888(self):
        """测试选择国内热门城市"""
        self.assertEqual(self.ele.SY_HomepageActivity, self.driver.current_activity, '进入首页失败')
        self.find_element_id_and_click_wait(self.ele.SY_search_widget_tv_city)
        toolUnits.wait(self.driver, self.ele.SS_rl_search_input_box_wrap)
        origin_text = self.get_text(self.ele.SS_wg_gv_itemtv, 2)
        self.find_element_id_and_click_wait(self.ele.SS_wg_gv_itemtv, 2)
        toolUnits.wait(self.driver, self.ele.SY_HomepageNavTab)
        self.find_element_id_and_click_wait(self.ele.SY_search_widget_tv_time)
        toolUnits.wait(self.driver, self.ele.RL_select_day_clearBtn)
        self.swipeDown(0.5, 0.5, 0.3)
        self.find_element_id_and_click_wait(self.ele.RL_select_day_clearBtn)
        today, newDay = toolUnits.calendar(2)
        self.find_element_desc_click_wait(today)
        self.find_element_desc_click_wait(newDay)
        self.find_element_id_and_click_wait(self.ele.RL_search_filter_more_confirm_button)
        toolUnits.wait(self.driver, self.ele.SY_HomepageNavTab)
        self.find_element_id_and_click_wait(self.ele.SY_search_widget_btn_search)
        self.assertEqual(self.ele.JGY_SearchResulitActivity, self.driver.current_activity, '进入结果页失败')
        address = self.get_text(self.ele.JGY_tv_result_page_city)
        self.assertEqual(origin_text, address, '城市跳转错误')
        self.assertIsNotNone(self.ele.JGY_iv_search_list_item_fav, '结果页没有加载出来房源信息')
        self.backlast()

    def test_02_66_020046_HomePage_SwitchToOtherPage(self):
        """切换房客端tab"""
        self.assertEqual(self.ele.SY_HomepageActivity, self.driver.current_activity, '切换至首图失败')
        self.find_element_id_and_click_wait(self.ele.SY_HomepageNavTab, 1)
        toolUnits.cancel_pop(self, 1)
        self.assertEqual(self.ele.SC_FavoriteGroupListActivity, self.driver.current_activity, '切换至收藏页失败')
        self.find_element_id_and_click_wait(self.ele.SY_HomepageNavTab, 2)
        toolUnits.cancel_pop(self, 1)
        self.assertEqual(self.ele.FKIM_TenantTalkPersonActivity, self.driver.current_activity, '切换至房客IM消息列表失败')
        self.find_element_id_and_click_wait(self.ele.SY_HomepageNavTab, 3)
        toolUnits.cancel_pop(self, 1)
        self.assertEqual(self.ele.FKGR_Me_MyselfActivityEx, self.driver.current_activity, '切换至个人中心页面失败')

    def test_02_72_020050_SearchPage_InputCityAndSearch(self):
        """输入城市名称出现正确的suggestion"""
        self.find_element_id_and_click_wait(self.ele.SY_search_widget_tv_city)
        inputName = "汉中"
        self.find_element_id_and_send_keys(self.ele.SS_et_search_input, inputName)
        cityName = self.get_text(self.ele.SS_pop_fxs_title)
        self.assertEqual(inputName, cityName, '搜索页输入城市名称未出现正确的suggestion')
        self.backlast(1)

    def tearDown(self):
        print('结束执行--首页用例集')
        self.driver.quit()


if __name__ == '__main__':
    pass
