#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/7
import uiautomator2 as u2
from time import sleep
from po import proxy
import pytest
import allure

class Test_aikan3():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        sleep(5)
        self.d.app_stop("com.chinamobile.cloudapp")

    @allure.step('爱看--阿里体育')
    def test_aikan_alitiyu(self):
        # 切换爱看tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_4").click(timeout=20)
        sleep(5)
        # 阿里体育
        self.d(text=u"阿里体育").click(timeout=20)
        sleep(5)
        # 篮球
        self.d(text=u"篮球").click(timeout=20)
        sleep(5)
        # 小组赛
        self.d(resourceId="com.chinamobile.cloudapp:id/image_mid").click(timeout=20)
        sleep(10)
        self.d.press("back")
        sleep(2)
        # 向上滑动
        self.d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)

        # 3X3联赛广州站
        self.d(resourceId="com.chinamobile.cloudapp:id/image_mid").click(timeout=20)
        sleep(10)
        self.d.press("back")
        sleep(2)

        # 向上滑动两次
        for i in range(4):
            self.d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
            sleep(1)

        sleep(5)
        self.d(text=u"拳击").click(timeout=5)
        self.d(text=u"健身").click(timeout=5)
        self.d(text=u"跑步").click(timeout=5)
        self.d(text=u"其他").click(timeout=5)




if __name__=="__main__":
    pytest.main("test_016_aikan_alitiyu.py")

