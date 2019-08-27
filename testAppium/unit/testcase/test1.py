# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:


import os
import sys
import time
from test.unit.common.webdriverUnit import WebdriverUnit
from test.conf.getStartActivityConfig import GetStartActivityConfig
import random

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
#
# print(random.randrange(1000, 9999))

sys.path.append("")

# class AutoCreateTest(object):
#
#     def prints(self):
#         self.config = GetStartActivityConfig()
#         print(' '.join({self.config.get_set_up()}))
#
#     def testAdd(self):
#         print(111)
#
#
# if __name__ == '__main__':
#     au = AutoCreateTest()
#     au.prints()


class test(object):

    def __init__(self):
        self.a = 10

    def test1(self):
        print(self.a)



def adds(s):

    change = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    add = list(s)

    nums = 0

    if len(add) == 0:
        return 0

    if len(add) < 2:
        return change[add[0]]

    for i ,p in enumerate(add):
        if (p=='I' and (add[i+1]=='V' or add[i+1]=='X')) or (p=='X' and (add[i+1]=='L' or add[i+1]=='C') or (p=='C' and (add[i+1]=='D' or add[i+1]=='M'))):
            nums = nums + change[add[i+1]]-change[p]
            add.remove(p)
        else:
            nums = nums+change[p]
        if i+2 == len(add):
            nums = nums + change[add[-1]]
            return nums
    return nums


def addss(s):
    d = {'I': 1, 'IV': 3, 'V': 5, 'IX': 8, 'X': 10, 'XL': 30, 'L': 50, 'XC': 80, 'C': 100, 'CD': 300, 'D': 500,
         'CM': 800, 'M': 1000}

    sum(d.get(s[max(i-1, 0):i+1],d[n]) for i, n in enumerate(s))

    for i, n in enumerate(s):
        print(s[max(i-1, 0)])
        print(d[n])
        print(d.get(s[max(i-1, 0)], d[n]))


def ints(x):
    """数据反转"""
    s = str(x)

    if s.startswith('-'):
        s = -int(s[::-1].rsplit('-')[0])
        if s < -2**31:
            return 0
        return s
    s = int(s[::-1].rsplit('-')[0])
    if s > 2**31 -1:
        return 0
    return s
    if x < 0:
        b = list(str(abs(x)))
        b.reverse()
        a = -int(''.join(b))
    else:
        b = list(str(abs(x)))
        b.reverse()
        a = int(''.join(b))

    if a < -2 ** 31 or a > 2 ** 31 - 1:
        a = 0

    return a


def rewen(i):

    s = str(i)
    print(int(len(s)/2))
    return len(s)


def together(lists:list):

    if len(lists) == 0:
        return None

    if len(lists) == 1:
        return lists[0]

    y = lists[0]
    x = ''
    lists.remove(y)
    for i, j in enumerate(lists):
        m = min(len(y), len(j))
        for u in range(m):
            if y[u] != j[u]:
                break
            else:
                x = x + y[u]
        y = x
        x = ''
    return y


def bbb(s):

    if s == "":
        return True
    if len(s) % 2 == 1:
        return False

    lists = ['()', '[]', '{}']

    for x in range(int(len(s)/2)):
        a = s
        for i, j in enumerate(lists):
            if j in s:
                s = s.replace(j, '')
        if s == '':
            return True
        if a == s:
            return False


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1 is None and l2 is None:
        return None
    new_list = ListNode(0)
    pre = new_list
    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            pre.next = l1
            l1 = l1.next
        else:
            pre.next = l2
            l2 = l2.next
        pre = pre.next
    if l1 is not None:
        pre.next = l1
    else:
        pre.next = l2
    return new_list.next


def maxs(nums):
    if len(nums) == 1:
        return nums[0]

    x = max(nums)
    a = len(nums)

    for j in range(a):
        y = 0
        for i in nums:
            i = i + y
            y = i
            x = max(i, x)
        nums.pop(0)

    return x

    for j in range(a):
        y = 0
        while len(nums) > 0 and nums[0] <= 0:
            nums.pop(0)

        for i in nums:
            i = i + y
            y = i
            x = max(i, x)
        if len(nums) != 0:
            nums.pop(0)
        else:
            return x
    return x


if __name__ == '__main__':
    # maxs([-2,1,-3,4,-1,2,1,-5,4])
    a = {1: [2,3,4], 2: [2,2,2]}
    for i in a.keys():
        for j in a.get(i):
            print(j)

