# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:signUnit.py

"""
Author: sunshicheng
DataTime : 2019-04-28 09:33
File : xz_sign.py
"""
import hashlib
import urllib
from urllib import parse
import requests
import json
from requests_toolbelt import MultipartEncoder


def md5_key(arg):
    hash = hashlib.md5()
    hash.update(arg.encode("utf-8"))
    return hash.hexdigest()


def get_xzsign(url):
    url = str(url)
    path = str(url.split('.com')[1]).split('?')[0]  # 目前只能解析.com类型的 可优化此逻辑为 if .com in ....
    try:
        jzd = url.split('?')[1].split('&')
    except:
        jzd = ''
    for i in range(len(jzd)):
        jzd[i] = jzd[i].split('=')
        for j in range(len(jzd[i]) - 2):
            jzd[i][1] += '='
            del jzd[i][-1]
    try:
        if jzd[-1][0] == 'xzsign':
            del jzd[-1]
    except Exception as e:
        print('无xzsign' + str(e))
    for i in range(len(jzd) - 1):
        for j in range(len(jzd) - i - 1):
            if jzd[j][0] > jzd[j + 1][0]:
                jzd[j], jzd[j + 1] = jzd[j + 1], jzd[j]
    for i in range(len(jzd)):
        jzd[i] = '|'.join(jzd[i])
    jzd = '|' + '|'.join(jzd) + '|'
    endstr = path + jzd + '2016v001'
    endstr = urllib.parse.unquote(endstr)
    newlen = len(urllib.parse.quote(endstr, 'utf-8').replace('%20', ' '))
    for i in range(newlen % 5 + 2):
        hash = hashlib.md5()
        hash.update(endstr.encode('utf-8'))
        endstr = hash.hexdigest()
    xzsign = 'md5_' + endstr
    return xzsign


def paramsforxzsign(url, params=None):
    try:
        if params.get("xzsign") is not None:
            del params['xzsign']
        if params.get('req_op') is not None:
            del params['req_op']
    except Exception as e:
        print('出错', e)
    ss = sorted(params.keys())
    paramslist = []

    for s in ss:
        paramsstr = s + "|" + str(params.get(s))
        paramslist.append(paramsstr)

    paramslist = '|' + "|".join(paramslist) + '|'
    endstr = url + paramslist + '2016v001'
    endstr = urllib.parse.unquote(endstr)
    newlen = len(urllib.parse.quote_plus(endstr, 'utf-8'))

    for i in range(newlen % 5 + 2):
        endstr = md5_key(endstr)
    params['xzsign'] = 'md5_' + endstr
    return params


def postforxzsign(url, params, body):
    try:
        if params.get('xzsign') is not None:
            del params['xzsign']
        if params.get('req_op') is not None:
            del params['req_op']
    except Exception as e:
        print('出错', e)
    paramsnew = params
    if type(body) == dict:
        params.update(body)
    else:
        print('错误')
        return '出错'
    paramslist = []
    ss = sorted(params.keys())

    for s in ss:
        paramsstr = s + "|" + str(params.get(s))
        paramslist.append(paramsstr)

    paramslist = '|' + "|".join(paramslist) + '|'
    endstr = url + paramslist + '2016v001'
    endstr = urllib.parse.unquote(endstr)
    newlen = len(urllib.parse.quote_plus(endstr, 'utf-8'))

    for i in range(newlen % 5 + 2):
        endstr = md5_key(endstr)
    params['xzsign'] = 'md5_' + endstr
    return params


def postforxzsign2(url, params, body):
    try:
        if params.get("xzsign") is not None:
            del params["xzsign"]
        if params.get("xzsign") is not None:
            del params["xzsign"]
    except Exception as e:
        print("出错!")
    paramsnew = []
    for key in params.keys():
        paramsnew.append(key)
    paramsnew.append("xzsign")
    if type(body) == dict:
        params.update(body)
    else:
        print("出错!")
        return "错误"
    ss = sorted(params.keys())

    paramslist = []

    for s in ss:
        paramsstr = s + "|" + str(params.get(s)).replace("'", "\"").replace(" ", "")
        paramslist.append(paramsstr)

    paramslist = '|' + "|".join(paramslist) + '|'
    endstr = url + paramslist + '2016v001'

    endstr = urllib.parse.unquote(endstr)

    newlen = len(urllib.parse.quote_plus(endstr, 'utf-8'))

    for i in range(newlen % 5 + 2):
        endstr = md5_key(endstr)
    params["xzsign"] = 'md5_' + endstr

    query = dict([(key, params[key]) for key in paramsnew])
    return query


if __name__ == '__main__':
    pass

