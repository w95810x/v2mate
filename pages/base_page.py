#coding=utf-8

'''
po设计模式：page object 页面对象
所有用到的页面都定义成一个类，继承自基础的Page类
把页面中用到的元素定义成方法
把页面上一些操作定义成方法
'''
# 基础类 用于所有页面的继承
# coding=utf-8
from appium import webdriver
from time import sleep
import unittest
import warnings
import os
import re
import logging

from appium.webdriver.mobilecommand import MobileCommand


class BasePage():

    def __init__(self,driver):
        self.driver=driver


    def send_text(self,loc,text):
        element=self.get_id(loc)
        element.clear()
        element.send_keys(text)

    def click_keycode(self,loc):
        os.system('adb shell ime set com.sohu.inputmethod.sogou/.SogouIME')
        self.get_id(loc).click()
        sleep(1)
        self.driver.keyevent(66)
        sleep(1)
        os.system('adb shell ime set io.appium.settings/.UnicodeIME')

    def click_xpath(self,xpath):
        element=self.driver.find_element_by_xpath(xpath)
        return element

    def click_back(self):
        self.driver.keyevent(4)

    def send_search(self,loc,text):
        s=self.get_id(loc)
        s.click()
        s.send_keys(text)
        self.get_id('com.download.ytb:id/searchIcon').click()
        sleep(3)


    def get_id(self, id):
        element = self.driver.find_element_by_id(id)
        return element

    def get_name(self, name):
        element = self.driver.find_element_by_name(name)
        return element

    def over(self):
        element = self.driver.quit()
        return element

    def get_screen(self, path):
        self.driver.get_screenshot_as_file(path)

    def get_size(self):
        size = self.driver.get_window_size()
        return size

    def swipe_to_up(self):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 500)

    def swipe_to_down(self):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, 500)

    def swipe_to_left(self):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 4, height / 2, width * 3 / 4, height / 2, 500)

    def swipe_to_right(self):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width * 4 / 5, height / 2, width / 5, height / 2, 500)

    def back(self):
        self.driver.keyevent(4)

    def get_classes(self, classesname):
        elements = self.driver.find_elements_by_class_name(classesname)
        return elements

    def get_ids(self, ids):
        elements = self.driver.find_elements_by_id(ids)
        return elements

    def switch_h5(self):
        self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "WEBVIEW_com.weizq"})

    def switch_app(self):
        self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "NATIVE_APP"})


