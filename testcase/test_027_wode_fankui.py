#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/8
import uiautomator2 as u2
from time import sleep
from po import proxy
import pytest
import allure

class Test_wode9():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        sleep(5)
        self.d.app_stop("com.chinamobile.cloudapp")

    @allure.step('我的--反馈')
    def test_wode_fankui(self):

        # 切换我的tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
        sleep(2)
        # 向上滑动
        self.d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)

        # 设置
        self.d(text=u"意见反馈").click()
        sleep(2)
        assert self.d(text=u"意见反馈").exists 
        # 输入文字
        self.d(resourceId="com.chinamobile.cloudapp:id/editText").set_text("APP很好，就是有些慢")
        sleep(2)
        # 输入联系方式
        self.d(resourceId="com.chinamobile.cloudapp:id/editText2").set_text("546564565")
        sleep(2)
        self.d.press("back")
        sleep(2)
        self.d.press("back")
        sleep(5)



if __name__ == "__main__":
    pytest.main("test_027_wode_fankui.py")


