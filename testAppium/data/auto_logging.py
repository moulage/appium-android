# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:auto_logging

import os
import logging
from testAppium.tool import ColorMe

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

"""
logger日志
"""

# logging.disable(logging.CRITICAL)  # 忽略日志等级，从那一级开始


def memo_log(logger_name='XZ-AN-LOG', log_file='AndroidAutoTest.log', level=logging.DEBUG):
    """log日志工具"""
    # 创建logger日志对象
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    # 创建控制台(将日志打印至控制台)
    ch = logging.StreamHandler()
    ch.setLevel(level)

    # 创建日志文件
    fh = logging.FileHandler(filename=log_file, encoding='utf-8')

    # 创建日志格式   参数可配置，命名取自文档固定的命名
    formatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)s] %(name)s %(levelname)s %(message)s')

    # 将格式加入控制台和日志文件
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # logger加入控制台和日志
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger


def main():
    # print("开始玩游戏")
    logger = memo_log(log_file='memo.log')
    logger.debug(ColorMe("debug message").blue())
    logger.info("info message")
    logger.warn("warning message")
    logger.error("error message")
    logger.critical("critical message")


if __name__ == "__main__":
    main()