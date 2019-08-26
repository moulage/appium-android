# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:url_request.py

import os
import requests
import json


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

"""
接口请求数据集合
"""


dingpa_online = "dingpa.xiaozhu.com"
username = "wanghui"
password = "w12345678."
cert = '/Users/xiaozhuduanzu/Desktop/AutoAndroidTest/python-client-master/test/unit/certificate/dingpa.pem'


def dingpa_login_online():
    """钉耙线上登录"""
    s = requests.session()
    s.keep_alive = False
    url_login = f"https://{dingpa_online}/xzrake/CheckPassword?username={username}&password={password}&timestamp=1551678648542&"
    try:
        # requests.packages.urllib3.disable_warnings()
        a = s.get(url_login, verify=False, cert=cert)
    except Exception as e:
        print(e)
    finally:
        return s


def get_mobile_verification_code(mobile='17610893392'):
    """获取手机验证码"""
    s = dingpa_login_online()
    url_sk = f"https://{dingpa_online}/xzrake/XZVerificationCodeSearchSub?mobile={mobile}&mobileAreaCode=86&codetype=selectCode&timestamp=1565924232314&"
    try:
        # requests.packages.urllib3.disable_warnings()
        res_sk = s.get(url_sk, verify=False)
        verification = json.loads(json.loads(str(res_sk.text).encode('utf-8'))['content'])['phoneCode']
    except Exception as e:
        print(e)
    finally:
        return verification


if __name__ == '__main__':
    # dingpa_login_online()
    # get_mobile_verification_code()
    pass

