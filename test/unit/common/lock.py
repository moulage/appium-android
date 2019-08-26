# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:lock.py

"""
处理屏幕开启问题  APPIUM有一套解锁流程
"""

from subprocess import Popen, PIPE


def isAwaked(deviceid=''):
    """
    判断的依据是'mAwaked = filae\n'
    :param deviceid:
    :return:
    """
    if deviceid == '':
        cmd = "adb shell dumpsys window policy"
    else:
        cmd = f"adb -s {deviceid} shell dumpsys window policy"

    awake = "b'    mAwake=false\n'"
    showing = "b'        mIsShowing=false\n'"

    all = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE).stdout.readlines()
    if awake in all:
        print("11111" + all)
        return True
    else:
        print("22222" + all)
        return False


if __name__ == '__main__':
    pass
