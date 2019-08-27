# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui

"""
获取当前手机状态
1：传入手机名称
2：遍历判断手机是否使用
    判断adb是否连接
        否：3
        是
3：判断当前手机是否被标识为使用中
        是：2
        否：1
4：返回一个数组
"""

import os
import sys
from time import sleep

sys.path.append("D:\\appium-android1")

from subprocess import Popen, PIPE
from testAppium.conf.getPhoneConfig import ConfigPhoneDevices


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


devices_state = {}  # 保存查询结果,{device_name : state}

EXECUTION = 1  # 可执行
EXECUTION_ING = 2  # 执行中
BREAK_OFF = 3  # 已断开
NEED_ADD = 4  # 库存没有，需添加设备
WRONG = 5  # 传入错误的方式


config = ConfigPhoneDevices()


def get_phones(names):
    """
    获取传入的手机名称转为list
    :return: 手机名称列表
    """
    # if len(sys.argv) < 2:
    #     print("未传入手机设备名称，请检查后重试。。。")
    #     return WRONG
    #
    # phones_name = sys.argv[1]

    phones_name = names
    if not isinstance(phones_name, list):
        return WRONG

    all_state = get_device(phones_name)
    all_devices = get_adb_devices()

    for phone, devices in all_state.items():
        if devices[0] in all_devices:
            if all_state[phone][1] == 'EXECUTION_ING':
                devices_state[phone] = EXECUTION_ING
            else:
                devices_state[phone] = EXECUTION
        else:
            devices_state[phone] = BREAK_OFF
    return devices_state


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


def get_device(phones: list):
    """
    获取配置文件中的device_name
    :param phones: 需检查状态的电话名称
    :return: 配置文件中对应的devices
    """
    all_devices_name = {}
    for phone in phones:
        data = []
        data.append(config.get_section_password(phone, 'devicename'))
        data.append(config.get_section_password(phone, 'execution'))
        all_devices_name[phone] = data
    return all_devices_name


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


def get_adb_count(all_dicts: dict):
    """获取链接设备的个数"""
    adb_dicts = {}
    for (k, v) in all_dicts.items():
        if v == 1:
           adb_dicts[k] = v
    return adb_dicts


# 暂时不使用，判断较为慢
def service_part(device_name: str) -> dict:
    """判断当前设备是否使用中"""
    result = Popen(f"adb -s {device_name} shell ps", shell=True, stdout=PIPE, stderr=PIPE).stdout.readlines()
    for i, j in enumerate(result):
        name = str(j, encoding='utf-8')
        # print(name.split('R ')[-1])
        if 'com.xiaozhu.xzdz' in name:  # 判断小猪是否在线程中，存在设置状态为 执行中
            devices_state[device_name] = EXECUTION_ING
            return devices_state
        sleep(10)  # 睡眠10s，再次查询
        if 'com.xiaozhu.xzdz' in name:
            devices_state[device_name] = EXECUTION_ING
            return devices_state

    devices_state[device_name] = EXECUTION_ING  # 不存在设置状态为 可执行
    return devices_state


if __name__ == '__main__':
    argument = sys.argv
    if len(argument) == 2:
        phones = eval(argument[1])
        print(get_phones(phones))

