# !/usr/bin/env python
# -*- coding = utf-8 -*-
# @Author:wanghui
# @Time:
# @File:send_message.py

import os, time
import paramiko
from dingtalkchatbot.chatbot import DingtalkChatbot


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

"""
发送短信操作
"""


class SendMessage(object):
    def __init__(self, testName):
        self.ssh_host = '10.0.0.221'
        self.ssh_port = 22
        self.username = 'xztest'
        self.password = '7c5cb6e5320e6c47f227841c'
        self.phone_number = ["13691422660", "18710463392", "15810216327", "15933678685", "18301448312", "18500361743",
                             "13436961715", "18844195352", "13910725671", "18210023150", "15810501841", "17744408687",
                             "15311809338", "15600655599"]
        self.phone_number = ['17610893392']
        self.content = testName

    def connectxztest(self):
        connection = paramiko.Transport((self.ssh_host, self.ssh_port))
        connection.connect(username=self.username, password=self.password)
        ssh = paramiko.SSHClient()
        ssh._transport = connection
        return ssh

    def sendmessage(self):
        ssh = SendMessage.connectxztest(self)
        for i in range(len(self.phone_number)):
            stdin, stdout, stderr = ssh.exec_command(
                "php /var/lib/jenkins/workspace/test-remindclient-00/script/test/testSMS.php" + ' ' + self.phone_number[i] + ' ' + self.content)
            print(stdout.read().decode())
            time.sleep(3)


class Robot:
    def __init__(self):
        pass

    def send_text(self, msg):
        raise NotImplementedError


class DingTalkRobot(Robot):

    webhook_before = 'https://oapi.dingtalk.com/robot/send?access_token='

    def __init__(self, webhook=webhook_before+'042d9b5897561cc592236e158ac729b0f735ae9770673af0417b7f34009950b7'):
        self.bot = DingtalkChatbot(webhook)
        super().__init__()

    def send_text(self, msg):
        self.bot.send_text(msg, is_at_all=True)


if __name__ == '__main__':
    DingTalkRobot().send_text("111")

