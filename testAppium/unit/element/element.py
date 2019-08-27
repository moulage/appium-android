# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:element.py


"""存储所有的元素"""


class AllElement(object):

    """全局变量"""
    tenant_user_name_online = "小猪玩起来"
    tenant_user_mobile_online = "17610893392"
    tenant_user_pass_word_online = "wh123456"
    land_lard_name_online = "小糖豆豆"
    land_lard_mobile_online = "18710463392"
    land_lard_pass_word_online = "jiehui89."

    """全局按钮"""
    actionbarwidget_back = "actionbarwidget_back"  # 返回按钮
    WebView_TitleBar_BackImg = "WebView_TitleBar_BackImg"  # H5页面返回按钮
    actionbarwidget_title = "actionbarwidget_title"  # 页面标题
    WebView_TitleBar_Title = "WebView_TitleBar_Title"  # H5页面标题
    actionbarwidget_moreTextView = "actionbarwidget_moreTextView"  # 确认按钮
    WebView_TitleBar_More = "WebView_TitleBar_More"  # H5页面右上角按钮
    standard_dialog_one_btn_right = "standard_dialog_one_btn_right"  # 弹层右边按钮
    standard_dialog_one_btn_left = "standard_dialog_one_btn_left"  # 弹层左边按钮

    """账号信息"""
    Tenant_Mobile = "17610893392"  # 房客账号
    Tenant_PassWord = "wh123456"  # 房客密码
    Landlord_Mobile = "18710463392"  # 房东账号
    Landlord_PassWord = "jiehui89."  # 房东密码

    """启动页面"""
    QD_splashActivity_passBtn = "splashActivity_passBtn"   # 跳过
    QD_splashActivity_startUseBtn = "splashActivity_startUseBtn"  # 进入小猪
    QD_splashActivity_passBtn = "splashActivity_passBtn"   # 启动页

    """登录首页"""
    DL_MainLoginActivity = ".main.MainLoginActivity"  # 登录首页
    DL_login_quick = "login_quick"  # 手机登录选择按钮

    """注册/快捷登录页面"""
    ZD_back_img = "back_img"  # 返回按钮
    ZD_login_change = "login_change"  # 账号密码登录按钮
    ZD_login_text_content= "login_text_edit"  # 输入手机号码框/短信验证码输入框
    ZD_login_text_country = "login_text_country"  # 国家国旗位置
    ZD_login_text_text = "login_text_text"  # 获取验证码按钮
    ZD_login_btn = "login_btn"  # 注册/登录按钮
    ZD_login_qq = "login_qq"  # QQ登录按钮
    ZD_login_weixin = "login_weixin"  # 微信登录按钮
    ZD_login_weibo = "login_weibo"  # 微博登录按钮

    """账号密码登录页面"""
    MM_actionbarwidget_back = "actionbarwidget_back"  # 返回按钮
    MM_login_text_edit = "login_text_edit"  # 账号输入
    MM_login_text_country = "login_text_country"  # 国家国旗位置
    MM_login_text_content = "login_text_edit"  # 密码输入
    MM_login_btn = "login_btn"  # 登录按钮
    MM_login_change = "login_change"  # 忘记密码
    MM_login_qq = "login_qq"  # QQ登录按钮
    MM_login_weixin = "login_weixin"  # 微信登录按钮
    MM_login_weibo = "login_weibo"  # 微博登录按钮
    MM_login_text_image = "login_text_image"  # 登录验证码

    """找回密码页面"""

    """弹层"""
    TC_ll_global_notice_wrap = "ll_global_notice_wrap"  # 通知设置弹层
    TC_fontViewContent = "webview_close_button"  # 弹层关闭按钮
    TC_fontViewContent2 = "fontViewContent"  # 弹层关闭小按钮

    """首页"""
    SY_HomepageActivity = ".find.pagehomeV4.HomepageActivityV4"  # 首页
    SY_HomepageNavTab = "iv_main_nav_icon"  # 导航按钮
    SY_search_widget_tv_city = "search_widget_tv_city"  # 城市输入框
    SY_search_widget_tv_time = "search_widget_tv_time"  # 日期选择框
    SY_search_widget_if_clear = "search_widget_if_clear"  # 地标关闭按钮
    SY_search_widget_btn_search = "search_widget_btn_search"  # 搜索按钮
    SY_WebView_SucessLayout = "WebView_SucessLayout"  # H5活动页面内容
    SY_home_page_entry_0 = "home_page_entry_0"  # 五大导航模块1
    SY_home_page_entry_1 = "home_page_entry_1"  # 五大导航模块2
    SY_home_page_entry_2 = "home_page_entry_2"  # 五大导航模块3
    SY_home_page_entry_3 = "home_page_entry_3"  # 五大导航模块4
    SY_home_page_entry_4 = "home_page_entry_4"  # 五大导航模块5
    SY_tab_itemHomeV4HotCity = "tab_itemHomeV4HotCity"  # 热门城市模块
    SY_text1 = "text1"  # 热门城市标题
    SY_rv_itemHomeV4HotCity = "rv_itemHomeV4HotCity"  # 热门城市按钮
    SY_tv_title_itemHomeV4 = "tv_title_itemHomeV4"  # 中部运营活动位
    SY_pager_itemOperationHomeV4 = "pager_itemOperationHomeV4"  # 中部运营位活动图片
    SY_frame_container_itemHomeV4 = "frame_container_itemHomeV4"  # 中部运营位
    SY_img_itemHomeV4History = "img_itemHomeV4History"  # 小猪故事运营位
    SY_iv_our_story_item_pic = "iv_our_story_item_pic"  # 小猪故事--列表模块
    SY_iv_black_back = "iv_black_back"  # 故事详情-返回按钮
    SY_tab_itemHomeV4HotRoom = "tab_itemHomeV4HotRoom"  # 热门房源模块标题
    SY_img_homeV4ItemHotCity = "img_homeV4ItemHotCity"  # 热门房源图片
    SY_tv_id = 'tv_id' # 热门房源处-热门城市
    # SY_
    # SY_
    # SY_
    # SY_
    # SY_

    """搜索页面"""
    SS_rl_search_input_box_wrap = "rl_search_input_box_wrap"  # 搜索城市输入栏
    SS_wg_gv_itemtv = "wg_gv_itemtv"  # 搜索城市名称按钮
    SS_et_search_input = "et_search_input"  # 搜索城市位置
    SS_pop_fxs_title = "pop_fxs_title"  # 搜索输入城市推荐列表城市名称
    SS_iv_search_history_clear = "iv_search_history_clear"  # 清除历史按钮

    """日历选择页"""
    RL_icon_font_select_day_close_button = "icon_font_select_day_close_button"  # 关闭页面按钮
    RL_select_day_clearBtn = "select_day_clearBtn"  # 清空日历按钮
    RL_search_filter_more_confirm_button = "search_filter_more_confirm_button"  # 确认日历选择按钮

    """结果页"""
    JGY_SearchResulitActivity = ".find.activity.Find_SearchResultListActivity"  # 结果页
    JGY_iv_result_page_back = "iv_result_page_back"  # 结果页返回按钮
    JGY_tv_result_page_city = "tv_result_page_city"  # 结果页城市名称
    JGY_rl_search_result_input_box_wrap = "rl_search_result_input_box_wrap"  # 位置输入框（同下）
    JGY_tv_result_page_input_box = "tv_result_page_input_box"  # 结果页位置
    JGY_iv_result_page_clear_input = "iv_result_page_clear_input"  # 清空位置按钮
    JGY_iv_result_page_mod_switch = "iv_result_page_mod_switch"  # 切换地图按钮
    JGY_map_address_background = "map_address_background"  # 地图页输入坐标名称
    JGY_rl_indicator_check_time = "rl_indicator_check_time"  # 结果页导航筛选标签
    JGY_search_filter_tag_tv = "search_filter_tag_tv"  # 结果页二级筛选标签
    JGY_fontViewContent = "fontViewContent"  # 推荐关闭按钮
    JGY_search_filter_orderBy_recommend = "search_filter_orderBy_recommend"  # 推荐排序按钮
    JGY_search_filter_orderBy_commentH2L = "search_filter_orderBy_commentH2L"  # 好评排序
    JGY_search_filter_orderBy_priceH2L_tv = "search_filter_orderBy_priceH2L_tv"  # 价格高-低
    JGY_search_filter_orderBy_priceL2H_tv = "search_filter_orderBy_priceL2H_tv"  # 价格低-高
    JGY_search_filter_orderBy_distance_tv = "search_filter_orderBy_distance_tv"  # 距离近-远
    JGY_tv_search_filter_tag_ensure = "tv_search_filter_tag_ensure"  # 结果页三级标签确认按钮
    JGY_iv_loop_image_item = "iv_loop_image_item"  # 结果页房源图片
    JGY_iv_search_list_item_fav = "iv_search_list_item_fav"  # 房源收藏按钮
    JGY_tv_search_list_item_title = "tv_search_list_item_title"  # 结果页房源名称

    """详情页"""
    XQY_NewLuDetailActivity = ".find.detail.ui.NewLuDetailActivity"  # 房源详情页页面
    XQY_luDetail_navigationBar_backBtn = "luDetail_navigationBar_backBtn"  # 返回按钮
    XQY_luDetail_navigationBar_shareBtn = "luDetail_navigationBar_shareBtn"  # 分享按钮
    XQY_luDetail_navigationBar_favoriteBtn = "luDetail_navigationBar_favoriteBtn"  # 收藏按钮
    XQY_iv_loop_image_item = "iv_loop_image_item"  # 房源图片
    XQY_tv_lodge_detail_unit_name = "tv_lodge_detail_unit_name"  # 详情页房源名称
    XQY_iv_lu_detail_promotion = "iv_lu_detail_promotion"  # 活动领券按钮
    XQY_tv_lodge_detail_view_rent_style = "tv_lodge_detail_view_rent_style"  # 房源信息（出租类型、宜住人数、床铺）
    XQY_tv_lodge_detail_landlord_nickname = "tv_lodge_detail_landlord_nickname"  # 房东名称
    XQY_tv_lodge_detail_all_comment = "tv_lodge_detail_all_comment"  # 更多点评
    XQY_layout_location_map_wrap = "layout_location_map_wrap"  # 地图
    XQY_fy_newcalendar_left_iv = "fy_newcalendar_left_iv"  # 日历上一月
    XQY_fy_newcalendar_month_tv = "fy_newcalendar_month_tv"  # 日历
    XQY_fontViewContent = "fy_newcalendar_right_iv"  # 日历下一月
    XQY_ludetaillayout_facility_title = "ludetaillayout_facility_title"  # 配套设施
    XQY_rl_lodge_detail_book_type_wrap = "rl_lodge_detail_book_type_wrap"  # 预订方式
    XQY_detail_deposit_des = "detail_deposit_des"  # 押金金额
    XQY_detail_rule_show_more_tip = "detail_rule_show_more_tip"  # 预订须知更多
    XQY_tv_unsubscribe_rule_detail = "tv_unsubscribe_rule_detail"  # 退订规则更多
    XQY_detail_recommend_bigimg_wrap = "detail_recommend_bigimg_wrap"  # 推荐房源图片
    XQY_detail_chat_layout = "detail_chat_layout"  # IM聊天按钮
    XQY_ludetaillayout_price_text = "ludetaillayout_price_text"  # 详情页房租金额
    XQY_ludetaillayout_booking_btn = "ludetaillayout_booking_btn"  # 详情页立即预定按钮

    """预订页面"""
    YD_LuBookingActivity = ".orderV2.ui.activity.LuBookingActivity"  # 预订页面
    YD_standard_dialog_one_message = "standard_dialog_one_message"  # 会员开通弹层
    YD_standard_dialog_one_btn_left = "standard_dialog_one_btn_left"  # 会员再想想按钮/预订日期被选中
    YD_actionbarwidget_back = "actionbarwidget_back"  # 返回按钮
    YD_tv_luBooking_luTitle = "tv_luBooking_luTitle"  # 房源标题
    YD_rl_luBooking_checkInDays = "rl_luBooking_checkInDays"  # 进入日期按钮
    YD_btn_luBooking_addTenants = "btn_luBooking_addTenants"  # 添加入住人按钮
    YD_btn_luBooking_submitOrder_1 = "btn_luBooking_submitOrder_1"  # 提交订单按钮
    YD_btn_dialog_bookTenantTip_ok = "btn_dialog_bookTenantTip_ok"  # 海外和未成年人弹层提示
    YD_OrderWebPageActivity = ".orderV2.ui.activity.OrderWebPageActivity"  # 提交订单完成页面
    YD_WebView_TitleBar_Title = "WebView_TitleBar_Title"  # 提交成功标题
    YD_standard_dialog_one_btn_right = "standard_dialog_one_btn_right"  # 返回弹层按钮

    """添加入住人页面"""
    RZR_PickTenantActivity = ".orderV2.ui.activity.PickTenantActivity"  # 添加入住人页面
    RZR_actionbarwidget_back = "actionbarwidget_back"  # 返回按钮
    RZR_actionbarwidget_moreTextView = "actionbarwidget_moreTextView"  # 完成按钮
    RZR_ll_pickTenant_addDomesticTenant = "ll_pickTenant_addDomesticTenant"  # 添加入住人按钮
    RZR_ll_pickTenant_addOverseaTenant = "ll_pickTenant_addOverseaTenant"  # 添加海外入住人按钮
    RZR_iv_pickTenant_pickCheckBox = "iv_pickTenant_pickCheckBox"  # 选择入住人按钮
    RZR_tv_pickTenant_name = "tv_pickTenant_name"  # 入住人名称
    RZR_iv_pickTenant_doModify = "iv_pickTenant_doModify"  # 进入入住人详情页面
    RZR_dialog_selectTenantTip_leftBtn = "dialog_selectTenantTip_leftBtn"  # 入住人未填写手机号码弹层

    """收藏页面"""
    SC_FavoriteGroupListActivity = ".collection.ui.activity.FavoriteGroupListActivity"  # 收藏页面
    SC_actionbarwidget_moreTextView = "actionbarwidget_moreTextView"  # 新建分组按钮
    SC_item_favorite_group_main_pic_iv = "item_favorite_group_main_pic_iv"  # 收藏列表分组模块按钮
    SC_item_favorite_group_title_iv = "item_favorite_group_title_iv"  # 分组名称

    """收藏二级页面"""
    SCE_FavoriteGroupDetailActivity = ".collection.ui.activity.FavoriteGroupDetailActivity"  # 收藏二级主页面
    SCE_WebView_TitleBar_BackImg = "WebView_TitleBar_BackImg"  # 返回按钮
    SCE_WebView_TitleBar_Share = "WebView_TitleBar_Share"  # 分享按钮
    SCE_WebView_TitleBar_More = "WebView_TitleBar_More"  # 更多按钮
    SCE_iv_loop_image_item = "iv_loop_image_item"  # 房源图片
    SCE_tv_fav_detail_lu_item_title = "tv_fav_detail_lu_item_title"  # 房源名称

    """房客IM"""
    FKIM_TenantTalkPersonActivity = ".imV2.activity.TenantTalkPersonActivity"  # 房客IM列表页面
    FKIM_TenantChatMessageActivity = ".imV2.activity.TenantChatMessageActivity"  # 房客IM详情页面
    FKIM_SystemAppMessageActivity = ".support.activity.SystemAppMessageActivity"  # 系统消息页面
    FKIM_actionbarwidget_moreImg = "actionbarwidget_moreImg"  # 房客屏蔽icon
    FKIM_tv_name = "tv_name"  # 列表-IM房东名称
    FKIM_tv_house_content = "tv_house_content"  # 列表-房源名称
    FKIM_tv_new_msg_cnt = "tv_new_msg_cnt"  # 列表-IM未读数量
    FKIM_tv_content = "tv_content"  # 列表-IM最后一条消息内容
    FKIM_tv_skip = "tv_skip"  # 系统消息--点击查看详情
    FKIM_iv_promotional_pop_window_back_button = "iv_promotional_pop_window_back_button"  # 详情页--返回按钮
    FKIM_tv_title = "tv_title"  # 详情页-房东名称
    FKIM_iv_house_detail = "iv_house_detail"  # 详情页-房源按钮
    FKIM_iv_order = "iv_order"  # 详情页-房东个人信息
    FKIM_iv_head = "iv_head"  # 详情页-房东头像
    FKIM_iv_head_me = "iv_head_me"  # 详情页-房客头像
    FKIM_tv_chatText = "tv_chatText"  # 详情页-房客话术
    FKIM_im_msg_right_text = "im_msg_right_text"  # 详情页-房东话术
    FKIM_ed_input = "ed_input"  # 详情页-输入框
    FKIM_iv_emoji = "iv_emoji"  # 详情页-表情icon
    FKIM_iv_more = "iv_more"  # 详情页-更多
    FKIM_im_chat_more_complaints = "im_chat_more_complaints"  # 详情页-房客投诉按钮
    FKIM_im_chat_more_shield = "im_chat_more_shield"  # 详情页-房客屏蔽房东按钮
    FKIM_tv_send = "tv_send"  # 详情页-发送
    # FKIM_
    # FKIM_
    # FKIM_
    # FKIM_
    # FKIM_
    # FKIM_
    # FKIM_
    # FKIM_
    # FKIM_
    # FKIM_
    # FKIM_
    # FKIM_
    # FKIM_
    # FKIM_
    # FKIM_

    """房东IM"""
    FDIM_TenantTalkPersonActivity = ".imV2.activity.TenantTalkPersonActivity"  # 房客IM列表页面
    FDIM_LandLordChatMessageActivityy = ".imV2.activity.LandLordChatMessageActivity"  # 房客IM详情页面
    FDIM_SystemAppMessageActivity = ".support.activity.SystemAppMessageActivity"  # 系统消息页面
    FDIM_actionbarwidget_moreImg = "actionbarwidget_moreImg"  # 房客屏蔽icon

    """个人中心"""
    FKGR_Me_MyselfActivityEx = ".personal.activity.Me_MyselfActivityEx"  # 个人中心页面
    FKGR_iv_me_setting = "iv_me_setting"  # 房客个人中心设置按钮
    FKZX_layout_myself_normal_item_icon = "layout_myself_normal_item_icon"  # 模块图标
    FKZX_tv_myself_normal_item_title = "tv_myself_normal_item_title"  # 模块名称
    FKZX_tv_want2be_landlord = "tv_want2be_landlord"  # 切换用户身份
    FKZX_tv_me_name_fk = "tv_me_name_fk"  # 用户名称

    """房东个人中心"""
    FDZX_tv_me_name_fd = "tv_me_name_fd"  # 用户名称

    """房客订单列表"""
    FKDD_TenantOrderListActivity = ".orderV2.ui.activity.TenantOrderListActivity"  # 房客订单列表页面
    FKDD_actionbarwidget_back = "actionbarwidget_back"  # 返回按钮
    FKDD_tv_orderListTab_title = "tv_orderListTab_title"  # 订单状态切换按钮
    FKDD_tv_first = "tv_first"  # 无订单展示话术（您暂时还没有相关的订单）
    FKDD_tv_tenantOrderListItem_state = "tv_tenantOrderListItem_state"  # 订单状态
    FKDD_lodge_unit_title = "lodge_unit_title"  # 订单房源标题
    FKDD_right_button_layout = "right_button_layout"  # 操作按钮
    FKDD_button_text = "button_text"  # 操作按钮（包含二级操作）

    """取消订单选择页面"""
    QQDD_advance_check_out_next = "advance_check_out_next"  # 取消订单下一步按钮
    QQDD_order_cancel_reason_isSelected = "order_cancel_reason_isSelected"  # 选择取消订单原因

    """设置页面"""
    SZ_my_exit = "my_exit"  # 退出登录按钮

    """发布系统"""
    FBXT_PublishListingActivity = ".publish.activity.PublishListingActivity"  # 发布系统页面
    FBXT_actionbarwidget_moreTextView = "actionbarwidget_moreTextView"  # 发布房源按钮/经营管理/选择地址下一步/详细地址确认/预览/删除房源下一步
    FBXT_orderlist_onging_num = "orderlist_onging_num"  # 标签切换按钮
    FBXT_tv_address_content = "tv_address_content"  # 房源地址
    FBXT_fangyuan_item_change_address_tv = "fangyuan_item_change_address_tv"  # 修改地址按钮
    FBXT_tv_fy_title = "tv_fy_title"  # 房源名称
    FBXT_tv_fy_desc = "tv_fy_desc"  # 房源状态
    FBXT_fangyuan_list_bottom_btn = "fangyuan_list_bottom_btn"  # 房源操作按钮
    FBXT_tv_landlord_calendar_price = "tv_landlord_calendar_price"  # 日历房价信息
    FBXT_xztv_input_price = "xztv_input_price"  # 日历设置修改价格输入框
    FBXT_xztv_input_btn_right = "xztv_input_btn_right"  # 日历设置修改价格确认
    FBXT_xztv_input_btn_left = "xztv_input_btn_left"  # 日历设置修改价格取消
    FBXT_tv_hire_yes = "tv_hire"  # 日历设为可租
    FBXT_tv_hire_no = "tv_hire_no"  # 日历设为不可租
    FBXT_tv_type_canael = "tv_type_canael"  # 取消设置房态按钮
    FBXT_fabu_address_item_detail_new = "fabu_address_item_detail_new"  # 选择发布位置名称
    FBTX_view_nationAddress_addressCreate = "view_nationAddress_addressCreate"  # 地址选择国家
    FBXT_view_addressAddress_addressCreate = "view_addressAddress_addressCreate"  # 地址详细地址
    FBXT_view_numberAddress_addressCreate = "view_numberAddress_addressCreate"  # 地址门牌号
    FBXT_view_locationAddress_addressCreate = "view_locationAddress_addressCreate"  # 地址地图选择
    FBXT_btn_submit_publishLuAddressCreate = "btn_submit_publishLuAddressCreate"  # 地址确认按钮
    FBXT_regions_name = "regions_name"  # 热门城市名称列表/热门地址列表/热门地址/热门地址
    FBXT_et_inputBox_publishLuDescEdit = "et_inputBox_publishLuDescEdit"  # 详细地址输入框/门牌号输入框
    FBXT_iv_lu_category_item_radio = "iv_lu_category_item_radio"  # 房源类型
    FBXT_tv_lu_category_list_commit = "tv_lu_category_list_commit"  # 房源类型确认按钮
    FBXT_me_Publish_Change_Rentaltype_TypeAllIcon = "me_Publish_Change_Rentaltype_TypeAllIcon"  # 出租类型选择
    FBXT_me_Publish_Change_Rentaltype_Submit = "me_Publish_Change_Rentaltype_Submit"  # 出租类型确认按钮
    FBXT_tv_statement_publishLuMainNormalItem = "tv_statement_publishLuMainNormalItem"  # 基本信息
    FBXT_btn_addLuPic_publishLuMainPicItem = "btn_addLuPic_publishLuMainPicItem"  # 发布房源添加图片
    FBXT_switch_publishLuMainItem = "switch_publishLuMainItem"  # 勾选同意挟制
    FBXT_btn_submit_publish_lu_main = "btn_submit_publish_lu_main"  # 马上发布按钮
    FBXT_tv_deleteLu_publishLuMainItem = "tv_deleteLu_publishLuMainItem"  # 删除房源按钮
    FBXT_iv_delete_house_reason = "iv_delete_house_reason"  # 删除原因选择
    FBXT_bt_delete = "bt_delete"  # 确认删除按钮
    FBXT_bt_delete_house_detail = "bt_delete_house_detail"  # 删除页面修改房源信息
    FBXT_phi_housetype = "myself_combine_rl"  # 基本信息-房屋户型
    FBXT_phi_area = "phi_area"  # 基本信息-出租面积
    FBXT_phi_wc = "phi_wc"  # 基本信息-卫生间类型
    FBXT_phi_mannum = "phi_mannum"  # 基本信息-宜住人数
    FBXT_myself_house_information = "myself_house_information"  # 基本信息-填写内容
    FBXT_actv_plus = "actv_plus"  # 基本信息-房屋户型-增加按钮
    FBXT_actv_reduce = "actv_reduce"  # 基本信息-房屋户型-减少按钮
    FBXT_et_lease_area = "et_lease_area"  # 基本信息-出租面积-填写面积
    FBXT_tv_pop_window_item_name = "tv_pop_window_item_name"  # 基本信息-卫生间类型-独立卫生间/房源照片-选择相册
    FBXT_et_livable_number = "et_livable_number"  # 基本信息-宜住人数-填写
    FBXT_tv_title_publish_lu_bed_add_item = "tv_title_publish_lu_bed_add_item"  # 添加床铺-选择床铺类型
    FBXT_btn_submit_publish_lu_bed_add = "btn_submit_publish_lu_bed_add"  # 添加床铺-确认添加成功按钮
    FBXT_tv_caption_publishLuDescListItem = "tv_caption_publishLuDescListItem"  # 房源描述-分模块标题
    FBXT_et_inputBox_publishLuDescEdit = "et_inputBox_publishLuDescEdit"  # 房源描述-输入内容框
    FBXT_cb_status = "cb_status"  # 配套设施-选择按钮
    FBXT_tv_title = "tv_title"  # 价格策略-列表标签名
    FBXT_et_day_price = "et_day_price"  # 价格策略-日价输入框
    FBXT_lu_image_add = "lu_image_add"  # 房源照片-添加照片按钮
    FBXT_tv_pop_window_item_name = "tv_pop_window_item_name"  # 房源照片-选择相册
    FBXT_iv_unselected = "iv_unselected"  # 相册选择相片
    FBXT_comment_photos_sure = "comment_photos_sure"  # 房源照片-选择照片-上传按钮
    FBXT_standard_dialog_two_btn_left = "standard_dialog_two_btn_left"  # 房源照片-返回弹层
    # FBXT_
    # FBXT_
    # FBXT_
    # FBXT_
    # FBXT_
    # FBXT_
    # FBXT_
    # FBXT_
    # FBXT_
    # FBXT_
    # FBXT_
    # FBXT_
    # FBXT_
    # FBXT_
    # FBXT_

    """点评"""
    FKDP_TenantCommentsListActivity = ".comment.ui.activity.TenantCommentsListActivity"  # 房客点评列表页面
    FKDP_tv_fkCommentList_item_orderState = "tv_fkCommentList_item_orderState"  # 列表状态
    FKDP_tv_fkCommentList_item_startDate = "tv_fkCommentList_item_startDate"  # 列表日期
    FKDP_tv_fkCommentDetail_noComment_tip = "tv_fkCommentDetail_noComment_tip"  # 详情页-未写点评话术-快写下您的入住体验
    FKDP_btn_fkCommentDetail_gotoWriteComment = "btn_fkCommentDetail_gotoWriteComment"  # 详情页-去点评按钮
    FKDP_fkCommentDetail_bindOrderContainer = "fkCommentDetail_bindOrderContainer"  # 详情页-订单信息
    FKDP_tv_fkCommentDetail_fdName = "tv_fkCommentDetail_fdName"  # 房东名称
    FKDP_tv_fkCommentDetail_fdCommentDetail = "tv_fkCommentDetail_fdCommentDetail"  # 房东点评内容
    FKDP_commitStart_textview = "commitStart_textview"  # 评分名称
    FKDP_commitStart_start1 = "commitStart_start1"  # 一颗星
    FKDP_commitStart_start2 = "commitStart_start2"  # 两颗星
    FKDP_commitStart_start3 = "commitStart_start3"  # 三颗星
    FKDP_commitStart_start4 = "commitStart_start4"  # 四颗星
    FKDP_commitStart_start5 = "commitStart_start5"  # 五颗星
    FKDP_et_fkCommentPublish_contentInput = "et_fkCommentPublish_contentInput"  # 点评内容输入框
    FKDP_iv_commentPublish_picture = "iv_commentPublish_picture"  # 添加照片-已有照片
    FKDP_tv_fkCommentPublish_addPicture_tip = "tv_fkCommentPublish_addPicture_tip"  # 添加照片-无照片
    FKDP_rl_pop_window_item = "rl_pop_window_item"  # 选择相册
    FKDP_tv_pop_window_item_name = "tv_pop_window_item_name"  # 选择拍照
    FKDP_firsttip_go_refuse = "firsttip_go_refuse"  # 点评完成页面--残忍拒绝
    FKDP_firsttip_later = "firsttip_later"  # 点评完成页面--稍后再说
    FKDP_feedback_coupon = "feedback_coupon"  # 非五分点评填写意见反馈页面
    FKDP_tv_fkCommentDetail_fkName = "FKDP_tv_fkCommentDetail_fkName"  # 详情页-房客名称
    FKDP_tv_fkCommentDetail_sanitationScore = "tv_fkCommentDetail_sanitationScore"  # 详情页-整洁卫生 5分
    FKDP_tv_fkCommentDetail_locationScore = "tv_fkCommentDetail_locationScore"  # 详情页-交通位置 4分
    FKDP_tv_fkCommentDetail_performanceScore = "tv_fkCommentDetail_performanceScore"  # 详情页-性价比空 5分
    FKDP_tv_fkCommentDetail_securityScore = "tv_fkCommentDetail_securityScore"  # 详情页-安全程度 4分
    FKDP_tv_fkCommentDetail_descriptionScore = "tv_fkCommentDetail_descriptionScore"  # 详情页-描述相符 5分
    FKDP_tv_fkCommentDetail_fkCommentContent = "tv_fkCommentDetail_fkCommentContent"  # 详情页-文本内容
    FKDP_tv_fkCommentDetail_fkCommentDel = "tv_fkCommentDetail_fkCommentDel"  # 详情页-删除

    """服务中心"""
    FWZX_LandlordCenterServiceActivity = ".servicecenter.activity.LandlordCenterServiceActivity"  # 服务中心页面
    FWZX_tv_mall_home_tile = "tv_mall_home_tile"  # 服务中心名称
    FWZX_icon_lock_view = "icon_lock_view"  # 门锁icon
    FWZX_tv_service_lock_subtitle = "tv_service_lock_subtitle"  # 门锁话术
    FWZX_icon_clean_view = "icon_clean_view"  # 保洁icon
    FWZX_tv_service_clean_subtitle = "tv_service_clean_subtitle"  # 保洁话术
    FWZX_icon_photograph_view = "icon_photograph_view"  # 小猪实拍icon
    FWZX_tv_service_photography_subtitle = "tv_service_photography_subtitle"  # 小猪实拍话术
    FWZX_icon_softWear_view = "icon_softWear_view"  # 软装icon
    FWZX_tv_service_softWear_subtitle = "tv_service_softWear_subtitle"  # 软装话术
    FWZX_tv_nav_tab_name = "tv_nav_tab_name"  # 商品tab切换
    FWZX_iv_good_picture = "iv_good_picture"  # 商品图片
    FWZX_tv_good_name = "tv_good_name"  # 商品标题
    FWZX_tv_good_price = "tv_good_price"  # 商品价格
    FWZX_fl_mall_home_bottom_btn_order = "fl_mall_home_bottom_btn_order"  # 商城订单按钮
    FWZX_fl_mall_home_bottom_btn_shop_cart = "fl_mall_home_bottom_btn_shop_cart"  # 商城购物车按钮
    # FWZX_
    # FWZX_
    # FWZX_
    # FWZX_
    # FWZX_

    """智能门锁页面"""
    MS_XZWebViewActivit = ".support.activity.XZWebViewActivity"  # 门锁介绍页面
    MS_Lock_ManageActivity = ".lock.activity.Lock_ManageActivity"  # 门锁管理页面
    MS_Lock_ApplyForChoiceAddr_Activity = ".lock.activity.Lock_ApplyForChoiceAddr_Activity"  # 申请门锁地址选择页面
    MS_Lock_PrivilegeManageActivity = ".lock.activity.Lock_PrivilegeManageActivity"  # 开门权限管理页面
    MS_Lock_OrderDetailPayActivity = ".lock.activity.Lock_OrderDetailPayActivity"  # 支付页面
    MS_lock_manager_passBtn = "lock_manager_passBtn"  # 申请智能门锁按钮
    MS_lock_apply_isSelectMarkImg = "lock_apply_isSelectMarkImg"  # 申请门锁地址选择
    MS_lock_manage_group_title = "lock_manage_group_title"  # 使用中的门锁话术
    MS_lock_manage_using_lockName = "lock_manage_using_lockName"  # 门锁管理-门锁地址
    MS_radio_lock_item_point = "radio_lock_item_point"  # 门锁申请-选择门锁
    MS_lock_applyFor_actualPictureContainer = "lock_applyFor_actualPictureContainer"  # 门锁申请-上传照片
    # MS_
    # MS_
    # MS_
    # MS_
    # MS_
    # MS_
    # MS_

    """保洁服务"""
    BJ_CleanSys_HomePagerActivity = ".cleaning.activity.CleanSys_HomePagerActivity"  # 保洁页面
    BJ_CleanSys_OrderListActivity = ".cleaning.activity.CleanSys_OrderListActivity"  # 保洁订单列表页面
    BJ_CleanSys_OrderDetailActivity = ".cleaning.activity.CleanSys_OrderDetailActivity"  # 保洁订单详情页面
    BJ_CleanSys_ChoiceAddressActivity = ".cleaning.activity.CleanSys_ChoiceAddressActivity"  # 保洁选择地址页面
    BJ_cleansys_homepage_banner_slogan_iv = "cleansys_homepage_banner_slogan_iv"  # 保洁介绍页面
    BJ_applyCleanService = "applyCleanService"  # 保洁介绍页面--申请保洁按钮
    BJ_clean_banner_text = "clean_banner_text"  # 新人体验保洁
    BJ_cleansys_homepager_order_ongoingly = "cleansys_homepager_order_ongoingly"  # 进行中订单
    BJ_cleansys_homepager_order_waitCommently = "cleansys_homepager_order_waitCommently"  # 待点评订单
    BJ_cleansys_homepager_order_closely = "cleansys_homepager_order_closely"  # 已结束订单
    BJ_cleansys_homepager_voucherhint = "cleansys_homepager_voucherhint"  # 保洁代金券
    BJ_cleansys_homepager_bottomBtn = "cleansys_homepager_bottomBtn"  # 立即申请保洁按钮
    BJ_clean_sys_address = "clean_sys_address"  # 地址选择
    BJ_room_select_radio = "room_select_radio"  # 房源选择
    BJ_clean_sys_booking_room_item = "clean_sys_booking_room_item"  # 服务房间
    BJ_ht_sure = "ht_sure"  # 服务房间--确认按钮
    BJ_ht_cancle = "ht_cancle"  # 服务房间--取消按钮
    BJ_clean_sys_booking_area_item = "clean_sys_booking_area_item"  # 服务面积
    BJ_fabu_input_houseArea = "fabu_input_houseArea"  # 服务面积--输入框
    BJ_fabu_houseArea_btn_right = "fabu_houseArea_btn_right"  # 服务面积--输入框--确认按钮
    BJ_clean_sys_booking_time_item = "clean_sys_booking_time_item"  # 服务时间
    BJ_clean_sys_booking_time_item = "clean_sys_booking_time_item"  # 服务时间
    BJ_cleanSys_serviceDate_rl = "cleanSys_serviceDate_rl"  # 服务时间--日期
    BJ_cleanSys_serviceTime_rl = "cleanSys_serviceTime_rl"  # 服务时间--时刻
    BJ_clean_sys_booking_type_item = "clean_sys_booking_type_item"  # 厨房保洁类型
    BJ_clean_sys_booking_wash_tools_item = "clean_sys_booking_wash_tools_item"  # 洗漱用品选择
    BJ_amount_picker_decrease_tv = "amount_picker_decrease_tv"  # 洗漱用品选择--减少类型
    BJ_amount_picker_increase_tv = "amount_picker_increase_tv"  # 洗漱用品选择--添加类型
    BJ_base_msg4_desc_tv = "base_msg4_desc_tv"  # 保洁填写订单详情信息
    BJ_clean_sys_cleaner_list_order_tv = "clean_sys_cleaner_list_order_tv"  # 预约按钮
    BJ_cleanSys_booking_agree_iv = "cleanSys_booking_agree_iv"  # 保洁协议按钮
    BJ_clean_sys_booking_base_time_tv = "clean_sys_booking_base_time_tv"  # 保洁详情页服务时间
    BJ_clean_sys_booking_base_room_tv = "clean_sys_booking_base_room_tv"  # 保洁详情页服务房间信息
    BJ_clean_sys_booking_base_type_tv = "clean_sys_booking_base_type_tv"  # 保洁详情页服务厨房类型
    BJ_tv_clean_sys_booking_original_price = "tv_clean_sys_booking_original_price"  # 保洁价格
    BJ_clean_sys_booking_next_step_tv = "clean_sys_booking_next_step_tv"  # 立即预订按钮
    BJ_go_pay_text = "go_pay_text"  # 去支付按钮
    BJ_tv_id = "tv_id"  # 代金券选择
    BJ_pay_jiantou_btn = "pay_jiantou_btn"  # 选择支付方式
    BJ_rl_clean_sys_ongoing = "rl_clean_sys_ongoing"  # 订单列表--进行中
    BJ_rl_clean_sys_comment = "rl_clean_sys_comment"  # 订单列表--待点评
    BJ_rl_clean_sys_closed = "rl_clean_sys_closed"  # 订单列表--已结束
    BJ_rl_clean_make_order = "rl_clean_make_order"  # 订单列表--申请保洁
    BJ_rl_clean_sys_content = "rl_clean_sys_content"  # 列表订单
    BJ_clean_sys_cancel_reason_iv = "clean_sys_cancel_reason_iv"  # 取消订单原因
    BJ_clean_sys_tip_text = "clean_sys_tip_text"  # 订单详情页状态话术
    # BJ_
    # BJ_
    # BJ_
    # BJ_
    # BJ_
    # BJ_
    # BJ_

    """支付"""
    ZF_ZHIFUBAO = "com.alipay.mobile.security.login.ui.AlipayUserLoginActivity"  # 支付宝页面
    ZF_WEIXIN = ".plugin.account.ui.SimpleLoginUI"  # 微信页面


if __name__ == '__main__':
    pass
