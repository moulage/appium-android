# !usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui

import configparser
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class ConfigPhoneDevices(object):

    def __init__(self, config_name='configPhone.ini'):
        self.config = configparser.ConfigParser()
        self.path = os.path.join(BASE_DIR, config_name)
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
        try:
            return self.config.items(section)
        except Exception as e:
            print("不存在相对应的section: ", e)
            return None

    def get_section_password(self, section, option):
        """获取当前option对应的值"""
        try:
            return self.config.get(section, option)
        except Exception as e:
            return None

    def set_option(self, section, option, value):
        """写入option值"""
        self.config.set(section, option, value)
        try:
            with open(self.path, 'w+', encoding='utf-8') as f:
                self.config.write(f)
        except ImportError as e:
            print("修改设备状态错误", e)

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
    config = ConfigPhoneDevices()
    print(config.get_section_items('360N7'))
    print(config.get_section_password('360N7', 'platformVersion'))
    print(config.get_section_password('360N7', 'execution'))
    config.set_option('360N7', "execution", 'ing')
    print(config.get_section_password('360N7', 'execution'))


if __name__ == '__main__':
    main()
