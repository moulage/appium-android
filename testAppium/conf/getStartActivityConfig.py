# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:getStartActivityConfig.py


import configparser
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class GetStartActivityConfig(object):

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.read_config()

    def read_config(self):
        """读取配置文件"""
        try:
            self.config.read(os.path.join(BASE_DIR, ''))
        except Exception as e:
            print(f'配置文件不正确: ', e)
            return None

    def get_set_up(self):
        """获取setUp的信息"""
        return self.config.items('SETUP')

    def get_tear_down(self):
        """获取setUp的信息"""
        return self.config.items('TEARDOWN')

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

    def check_config(self, *arg):
        """检查配置文件信息是否正确"""
        try:
            self.read_config()
            if len(arg) == 1:  # 判断是否有section
                return self.config.has_section(arg[0])
            elif len(arg) == 3:  # 判断section下 option是否正确
                if self.config[arg[0]][arg[1]] == arg[2]:
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            return False


def main():
    config = GetStartActivityConfig()
    print(config.get_set_up())
    # print(config.get_section_items('360'))
    # print(config.get_section_password('360', 'platformVersion'))


if __name__ == '__main__':
    main()
