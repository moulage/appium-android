# !usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui

import configparser
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class ConfigPhoneDevices(object):

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.path = os.path.join(BASE_DIR, 'configPhone.ini')
        self.read_config()

    def read_config(self):
        """读取配置文件"""
        try:
            self.config.read(self.path)
        except Exception as e:
            print('手机配置文件不正确: ', e)
            return None

    def get_sections(self):
        """ 获取所有的section """
        return self.config.sections()

    def get_option(self, section):
        """获取当前section下的所有options"""
        return self.config.options(section)

    def get_section_items(self, section):
        """获取当前section下的所有键值对"""
        return self.config.items(section)

    def get_section_password(self, section, option):
        """获取当前option对应的值"""
        return self.config.get(section, option)

    def set_option(self, section, option, value):
        """写入option值"""
        self.config.set(section, option, value)
        try:
            with open(self.path, 'w+', encoding='utf-8') as f:
                self.config.write(f)
        except ImportError as e:
            print("修改设备状态错误", e)


def main():
    config = ConfigPhoneDevices()
    print(config.get_section_items('360N7'))
    print(config.get_section_password('360N7', 'platformVersion'))
    print(config.get_section_password('360N7', 'execution'))
    config.set_option('360N7', "execution", 'ing')
    print(config.get_section_password('360N7', 'execution'))


if __name__ == '__main__':
    main()
