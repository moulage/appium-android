# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:orderUnit.py

import os
import urllib
import time
import requests
from testAppium.unit.common import signUnit, toolUnits
from requests_toolbelt import MultipartEncoder

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

version = '5.4.00'
sessId = 'WyIyNTA5MDc0MzEwbWNIQyIseyJzc0lkIjoxMTE3OTQzOTExMDAsInNzVHlwZSI6InVzZXJuYW1lX3Bhc3N3b3JkIiwiZGF0YSI6ImM1MGJiNmU3MzhhNzRlMmFhZjk5NGY2ZDcxYjNmYmQ1IiwiZXhwaXJlIjoxNTc4Mjc1MDA1fSwiNDE4ODViZjAwODQ4NjllYjYxNjA4OTk3OTg2NTNiMTAiXQ%3D%3D&'
link = "https://securewireless-order.xiaozhu.com"


def Place_order(addDate=1, originalPrice='1', luId='31780836303', userId='7009149315'):
    """提交订单"""
    false = 'false'
    params_temp = \
        '_=1562724198854&' \
        'dispathChannel=xiaozhu&' \
        f'sessId={sessId}' \
        'uniqueId=869600040058817&' \
        f'userId={userId}&' \
        'xzsign=md5_3a9b46f1ae378a57c7521dd67adfa8bd'
    url = f'/app/xzfk/android/{version}/book/submit'

    # checkInDate, checkOutDate = toolUnits.calendar(addDate)
    checkInDate, checkOutDate = "2019-08-15", '2019-08-16'
    data = {"actualTotalPaidPrice": "0.95", "buyCarefreeInsurance": false, "checkInDate": checkInDate,
            "checkOutDate": checkOutDate, "coupon": {"useCouponIds": [], "usedCoupon": "0"},
            "invoiceInfo": {"needInvoice": false, "userRemark": false}, "isBuyVip": false, "isOrderUseVip": false,
            "luId": luId, "orderId": "", "originalPrice": originalPrice, "parentOrderId": "", "payType": "alipay",
            "roomNum": "1", "submitType": "createOrder", "tenantList": [
            {"IDCardNo": "610523199207102271", "birth": "1992-07-10", "id": "94514359100", "insurance": "no",
             "mobileNation": "0", "name": "\u6d4b\u8bd5", "nationId": "0", "oversea": "no", "passportNo": "",
             "sex": "man"}], "userId": "7009149315", "version": ""}

    # 格式化params
    params = urllib.parse.unquote(params_temp, 'utf-8')
    params = urllib.parse.parse_qs(params)
    for s in params.keys():
        params[s] = params.get(s)[0]
    # 计算小猪验签
    params_sign = signUnit.postforxzsign2(url, params, {"data": data})
    # 处理data内容，将单引号全部处理成双引号，将空格替换成没有
    m = MultipartEncoder(
        fields={"data": (None, str(data).replace("'", "\"").replace(" ", ""))}
    )
    # 增加headers
    headers = {
        'Content-Type': m.content_type
    }
    requests.packages.urllib3.disable_warnings()
    response = requests.post(link + url, params=params_sign, data=m, headers=headers, verify=False,
                             cert='../../conf/client.pem').json()
    try:
        order_id = response['content']['params']['orderId']
        assert order_id != None
        print("下单成功")
        return order_id
    except:
        errorMsg = response
        print(errorMsg)
        return 2


# 取消订单
def Cancellation_order(order_id, userId='7009149315'):
    time.sleep(2)
    url = '/app/xzfk/android/5.3.00/tenantOrder/cancel'
    link = "https://securewireless-order.xiaozhu.com"
    params_temp = \
        '_=1562724598939&' \
        'cancelReason=%E6%88%91%E7%9A%84%E8%A1%8C%E7%A8%8B%E6%9C%89%E5%8F%98&' \
        'cancelType=journeychange&' \
        'checkOutDayEarly=&' \
        'dispathChannel=xiaozhu&' \
        'orderId=' \
        + order_id + \
        f'&sessId={sessId}' \
        'uniqueId=869600040058817&' \
        f'userId={userId}&' \
        'xzsign=md5_ee0be649bd726879827585e059d1ece0'
    # 格式化params
    params = urllib.parse.unquote(params_temp, 'utf-8')
    params = urllib.parse.parse_qs(params)
    for s in params.keys():
        params[s] = params.get(s)[0]
    params_sign = signUnit.paramsforxzsign(url, params)

    start = time.time()
    requests.packages.urllib3.disable_warnings()
    response = requests.get(url=link + url, params=params_sign, verify=False, cert='../../conf/client.pem').json()

    try:
        assert response['status'] == 200
        print("取消订单成功")
        return True
    except:
        errorMsg = response
        print(errorMsg)
        return False


# 接受订单
def Accept_order(order_id, userId='6582705415'):
    if order_id == '':
        print('请传入订单ID')
        return False
    time.sleep(2)
    url = f'/app/xzfd/android/{version}/landlord/confirm'
    link = "https://securewireless-order.xiaozhu.com"
    params_temp = '_=1565146275916&' \
        'dispathChannel=huawei&' \
        'sessId=WyIyNjA1MDgxMjA4RFB1VyIseyJzc0lkIjoxMTcxMzQ2MTYxMDAsInNzVHlwZSI6InVzZXJuYW1lX3Bhc3N3b3JkIiwiZGF0YSI6IjNiOTU3ZDI3YTE4NTM3NDEzNzk4YTMxNDQ0N2VlNDVhIiwiZXhwaXJlIjoxNTgwODA3NTQ2fSwiNzEwZTZmOGZlM2FmNWVlYjkxMmZiNjc0ZmE4Yjg5YzciXQ%3D%3D' \
        'uniqueId=862788036258454&' \
        f'userId={userId}&' \
        'xzsign=md5_b5d710806ab7968a7694139fc6f29531'

    data = {'orderId': order_id, 'rentFee': ' ', 'version': ' ',
            'cashPledge': ' ', 'cleanFee': ' ', 'cashPledgeEditable': ' '}
    # data = {'oorderId': order_id, 'version': '1', 'cashPledgeEditable': False}

    # 格式化params
    params = urllib.parse.unquote(params_temp, 'utf-8')
    params = urllib.parse.parse_qs(params)
    for s in params.keys():
        params[s] = params.get(s)[0]
    # 计算小猪验签
    params_sign = signUnit.postforxzsign2(url, params, {"data": data})
    # 处理data内容，将单引号全部处理成双引号，将空格替换成没有
    m = MultipartEncoder(
        fields={"data": (None, str(data).replace("'", "\"").replace(" ", ""))}
    )
    # 增加headers
    headers = {
        'Content-Type': m.content_type
    }

    requests.packages.urllib3.disable_warnings()
    response = requests.post(link + url, params=params_sign, data=m, headers=headers, verify=False,
                             cert='../../conf/client.pem').json()

    try:
        assert response['status'] == 200
        print("房东接受订单成功")
    except:
        errorMsg = response
        print(errorMsg)


if __name__ == '__main__':
    # Place_order()
    # Cancellation_order('117133647300')
    Accept_order(order_id='117135303800')

