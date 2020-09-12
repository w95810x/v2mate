# coding=utf-8
import HTMLTestRunner
from appium import webdriver
from unittest import defaultTestLoader
import time
from time import sleep
import unittest
import warnings
import os
import re
import logging
import warnings
from pages.sidebar_page import Sidebar
from pages.home_page import Home
case_path = r'E:\pyproject\v2matetest\test_case'

readDeviceId = list(os.popen('adb devices').readlines())
# 正则表达式匹配出 id 信息
deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]
# 读取设备系统版本号
deviceAndroidVersion = list(os.popen('adb shell getprop ro.build.version.release').readlines())


def android_driver():
    desired_caps = {'platformName': 'Android',
                    'platformVersion': deviceAndroidVersion,
                    'deviceName': deviceId,
                    'automationName': 'uiautomator2',
                    'unicodeKeyboard': 'true',
                    'resetKeyboard': 'true',
                    'appPackage': 'com.download.ytb',
                    'appActivity': 'com.download.ytb.start.LoadingActivity'}

    return desired_caps



class Case(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter('ignore',ResourceWarning)
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',android_driver())

    def test_setting_task(self):
        s = Sidebar(self.driver)
        h = Home(self.driver)
        sleep(3)
        h.click_menu()
        s.setting_task()

    def test_setting_clear_cache(self):
        s = Sidebar(self.driver)
        h = Home(self.driver)
        h.click_menu()
        s.click_setting()
        s.clear_cache()
    def test_setting_shareapp(self):
        s = Sidebar(self.driver)
        h = Home(self.driver)
        h.click_menu()
        s.click_share()
        s.share_whatsapp_apk()
    def test_setting_sharelink(self):
        s = Sidebar(self.driver)
        h = Home(self.driver)
        h.click_menu()
        s.click_share()
        s.share_whatsapp_link()

    def test_settint_feedback(self):
        s = Sidebar(self.driver)
        h = Home(self.driver)
        h.click_menu()
        s.setting_feedback()

    def test_Privacy_Policy(self):
        s = Sidebar(self.driver)
        h = Home(self.driver)
        h.click_menu()
        s.privacy_policy()

    def test_about_upload(self):
        s = Sidebar(self.driver)
        h = Home(self.driver)
        h.click_menu()
        s.about_upload()

    def tearDown(self):
        self.driver.quit()







if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(Case("test_setting_task"))
    suite.addTest(Case("test_setting_clear_cache"))
    suite.addTest(Case("test_setting_shareapp"))
    suite.addTest(Case("test_setting_sharelink"))
    suite.addTest(Case("settint_feedback"))
    suite.addTest(Case("test_Privacy_Policy"))
    suite.addTest(Case("test_about_upload"))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    filename =r'E:\pyproject\v2matetest\test_case\results' + now + '.html'  # 这个路径改成自己的目录路径
    fp = open(filename,'wb')
    #使用unttest运行无法生成测试报告，使用命令行运行生成测试报告
    runner =HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"v2mate测试报告", description=u"用例测试执行情况")
    runner.run(suite)
    fp.close()


