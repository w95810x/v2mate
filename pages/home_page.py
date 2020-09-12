#coding=utf-8
from pages.base_page import BasePage
from time import sleep
class Home(BasePage):

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def click_menu(self):
        sleep(10)
        self.get_id('com.download.ytb:id/iv_menu').click()
        sleep(3)
    def click_search(self):
        self.get_id('com.download.ytb:id/tv_search').click()








