#coding=utf-8
from pages.base_page import BasePage
from pages.home_page import Home
from time import sleep
import time
import os
class Sidebar(BasePage):
    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def click_SIGN_IN(self):  # 侧边栏点击登录
        self.get_id("com.download.ytb:id/sign_in_layout").click()
        sleep(5)

    def click_setting(self):#点击设置
        sleep(2)
        self.get_id('com.download.ytb:id/my_res_title').click()
        sleep(2)

    def setting_task(self):#修改下载任务数量
        h=Home(self.driver)
        #点击setting按钮
        sleep(2)
        self.click_setting()
        sleep(2)
        self.click_xpath('//*[@text="Max download tasks"]').click()
        sleep(1)
        self.click_xpath('//*[@text="1"]').click()
        sleep(1)
        text=self.get_id('com.download.ytb:id/max_download_num').text
        print(type(text))
        text1=int(text)
        print(text1)
        sleep(2)
        if text1 == 1:
            print('---->更改成功----->')
        else:
            print('---->更改失败----->')

        #验证更改是否生效
        self.click_back()
        self.click_back()
        h.click_search()
        sleep(2)
        self.send_search('com.download.ytb:id/searchText','"2020 kkbox 一人一首成名曲 - 【抖音神曲2020】#抖音流行歌曲 2020-2020 新歌 & 排行榜歌曲 - 中文歌曲排行榜 2020TIK TOK抖音音樂熱門歌單 #76')
        sleep(3)
        #首次点击下载包括获取权限
        ids=self.get_ids('com.download.ytb:id/down')
        ids[0].click()
        self.get_id('android:id/button1').click()
        self.click_xpath('//*[@resource-id="com.android.packageinstaller:id/permission_allow_button"]').click()
        self.get_id('com.download.ytb:id/neg_btn').click()
        sleep(10)
        self.click_xpath('//*[@text="480P"]').click()
        self.get_id('com.download.ytb:id/down_btn').click()
        #再次点击下载
        self.click_xpath('//*[@text="480P"]').click()
        self.get_id('com.download.ytb:id/down_btn').click()
        self.get_id('om.download.ytb:id/downIcon').click()
        sleep(5)
        t=self.get_ids('com.download.ytb:id/video_download_speed').text
        sleep(1)
        if t == 'WAITING…':
            print('---->验证成功----->')
        else:
            print('---->验证失败----->')

    def clear_cache(self):#清除数据
        self.get_id('com.download.ytb:id/cache_num').click()
        c=self.get_id('com.download.ytb:id/cache_num').text
        if c == '0K':
            print('---->清除成功----->')
        else:
            print('---->清除失败----->')
        self.click_back()

    def click_share(self):#点击分享
        self.click_xpath('//*[@text="Share V2Mate"]').click()

    def share_whatsapp_apk(self):#分享apk
        self.click_xpath('//*[@text="WhatsApp"]').click()
        sleep(5)
        c=self.get_classes('android.widget.RelativeLayout')
        c[1].click()
        self.get_id('com.whatsapp:id/send').click()
        sleep(2)
        if  self.get_id('com.whatsapp:id/title').text == 'base.apk':
            print('---->分享成功1----->')
        elif self.get_ids('com.whatsapp:id/title').text[1] == 'base.apk':
            print('---->分享成功2----->')
        else:
            print('---->分享失败----->')

    def share_whatsapp_link(self):#分享链接
        sleep(1)
        self.get_id('com.download.ytb:id/share_line').click()
        self.click_xpath('//*[@text="WhatsApp"]').click()
        sleep(5)
        c=self.get_classes('android.widget.RelativeLayout')
        c[2].click()
        self.get_id('com.whatsapp:id/send').click()
        sleep(2)
        self.get_id('com.whatsapp:id/buttons').click()
        sleep(2)
        t='V2mate is the most powerful app to watch and download Videos & Music. You can download all Videos & Music you like. The download link is : http://v2mate.com/'
        print(self.get_id('com.whatsapp:id/message_text').text)
        if  self.get_id('com.whatsapp:id/message_text').text == t:
            print('---->分享成功1----->')
        elif self.get_ids('com.whatsapp:id/message_text').text[1] == t:
            print('---->分享成功2----->')
        else:
            print('---->分享失败----->')

    def setting_feedback(self): # 发送反馈邮件，只发送没有做数据库校验
        self.click_xpath('//*[@text="Help and feedback"]').click()
        sleep(1)
        self.click_xpath('//*[@text="Gmail"]').click()
        sleep(2)
        os.system('adb shell ime set com.sohu.inputmethod.sogou/.SogouIME')
        self.get_id('com.google.android.gm:id/subject').click()
        self.send_text('com.google.android.gm:id/subject','tests')
        sleep(1)
        self.get_id('com.google.android.gm:id/send').click()

    def privacy_policy(self):#隐私政策
        self.click_xpath('//*[@text="Privacy Policy"]').click()
        sleep(1)
        t=self.click_xpath('//*[@text="Privacy Policy"]').text
        if t == 'Privacy Policy':
            print('---->进入Privacy Policy页----->')
        else:
            print('---->没有进入Privacy Policy页----->')
        self.click_back()

    def click_about(self):#点击关于
        self.click_xpath('//*[@text="About"]').click()

    def about_upload(self):
        self.click_about()
        sleep(3)
        self.get_id('com.download.ytb:id/upload_btn').click()
        sleep(5)
        t=self.get_id('com.download.ytb:id/upload_desc').text
        if t == 'It is the latest version.':
            print('---->不需要更新----->')
        else:
            print('---->一会儿写升级的case----->')
        self.click_back()






