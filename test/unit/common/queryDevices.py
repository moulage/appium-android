# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui

"""
获取当前手机状态
1：传入手机名称
2：判断当前手机是否被标识为使用中
3：是：直接返回--> EXECUTION_ING   否：获取手机对应的devices
4：检查device是否连接服务器
"""

import os
import sys
from subprocess import Popen, PIPE
from time import sleep
from multiprocessing.pool import ThreadPool
from test.conf.getPhoneConfig import ConfigPhoneDevices


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


devices_state = {}  # 保存查询结果,{device_name : state}

EXECUTION = 1  # 可执行
EXECUTION_ING = 2  # 执行中
BREAK_OFF = 3  # 已断开


config = ConfigPhoneDevices()


def get_phones():
    """
    获取传入的手机名称转为list
    :return: 手机名称列表
    """
    if len(sys.argv) < 2:
        print("未传入手机设备名称，请检查后重试。。。")
        return None
    phones_name = sys.argv[1]
    if ',' not in phones_name:
        phones = [phones_name]
    else:
        phones = phones_name.split(',')
    return phones


def get_device(phones):
    """
    获取配置文件中的device_name
    :param phones: 需检查状态的电话名称
    :return: 配置文件中对应的devices
    """
    all_devices_name = {}
    for phone in phones:
        all_devices_name[phone] = config.get_section_password(phone, 'deviceName')
    return all_devices_name


def get_adb_devices():
    """
    获取所有devices
    :return: 所有的设备devices
    """
    result = Popen("adb devices", shell=True, stdout=PIPE, stderr=PIPE).stdout.readlines()
    devices_name = []
    for item in result:
        t = item.decode().split("\tdevice")
        if len(t) >= 2:
            devices_name.append(t[0])
    return devices_name


def judge_devices(devices_list: dict, adb_list: list):
    """
    判断传入的phone名称是否连接电脑
    :param devices_list: devices名称列表
    :param adb_list: adb与服务器链接列表
    :return:
    """
    for i, j in devices_list.items():
        if j not in adb_list:
            devices_state[i] = BREAK_OFF
        else:
            devices_state[i] = EXECUTION
    return devices_state


def judge_phone_ing():
    """
    获取手机是否为运行中状态
    :return: 手机当前运行状态
    """
    for i, j in devices_state.items():
        if j == 1:
            execution = config.get_section_password(i[0], 'execution')
            if execution == "execution_ing":
                devices_state[i] = EXECUTION_ING
    return devices_state


# def thread_pools(counts, adb_devices):
#     """开启多线程"""
#     pool = ThreadPool(processes=counts)
#     pool.map(service_part, (device_name for device_name in adb_devices))
#     pool.close()


# def get_adb_count(all_dicts: dict):
#     """获取链接设备的个数"""
#     adb_dicts = {}
#     for (k, v) in all_dicts.items():
#         if v == 1:
#            adb_dicts[k] = v
#     return adb_dicts


# 暂时不使用，判断较为慢
# def service_part(device_name: str) -> dict:
#     """判断当前设备是否使用中"""
#     result = Popen(f"adb -s {device_name} shell ps", shell=True, stdout=PIPE, stderr=PIPE).stdout.readlines()
#     for i, j in enumerate(result):
#         name = str(j, encoding='utf-8')
#         # print(name.split('R ')[-1])
#         if 'com.xiaozhu.xzdz' in name:  # 判断小猪是否在线程中，存在设置状态为 执行中
#             devices_state[device_name] = EXECUTION_ING
#             return devices_state
#         sleep(10)  # 睡眠10s，再次查询
#         if 'com.xiaozhu.xzdz' in name:
#             devices_state[device_name] = EXECUTION_ING
#             return devices_state
#
#     devices_state[device_name] = EXECUTION_ING  # 不存在设置状态为 可执行
#     return devices_state


if __name__ == '__main__':

    phone_list = get_phones()

    all_devices_dict = get_device(phone_list)

    adb_device_list = get_adb_devices()

    all_dicts = judge_devices(all_devices_dict, adb_device_list)

    # adb_device_dicts = get_adb_count(all_dicts)

    count = len(adb_device_list)

    # thread_pools(count)

