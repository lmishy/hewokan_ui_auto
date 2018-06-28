#!/usr/bin/python3
# -*- coding:utf-8 -*-
#@time: 2018/6/6
import uiautomator2 as u2
from time import sleep
from po import proxy,ExcuteCase as E
import pytest
import allure

class Test_yingshi1():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        self.d.app_stop("com.chinamobile.cloudapp")

    @allure.step('影视--banner')
    def test_yingshi_banner(self):
        # 切换影视tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_3").click()
        sleep(2)
        # 播放其中一个视频
        self.d(resourceId="com.chinamobile.cloudapp:id/image").click()
        sleep(5)
        self.d(resourceId="com.chinamobile.cloudapp:id/video_collect_icon").click()
        sleep(2)
        self.d.press("back")
        sleep(2)

    @allure.step('影视--咪咕专区')
    def test_yingshi_migu(self):
        # 咪咕专区
        self.d(text=u"咪咕视频").click()
        sleep(5)
        self.d(text=u"咪咕专区").wait(timeout=10)
        assert self.d(text=u"咪咕专区").exists == True
        self.d.press("back")
        sleep(2)

    @allure.step('影视--芒果专区')
    def test_yingshi_manggo(self):
        # 芒果专区
        self.d(text=u"芒果TV").click()
        sleep(5)
        assert self.d(text=u"芒果TV-精选").exists == True
        self.d.press("back")
        sleep(2)

    @allure.step('影视--百视通专区')
    def test_yingshi_baishitong(self):
        # 百视通专区
        self.d(text=u"百视通").click()
        sleep(5)
        assert self.d(text=u"百视通").exists == True
        self.d.press("back")

    @allure.step('影视--凤凰网')
    def test_yingshi_fenghuang(self):
        # 凤凰网
        self.d(text=u"凤凰网").click()
        sleep(5)
        assert self.d(text=u"凤凰网专区").exists == True
        self.d.press("back")
        sleep(2)
        # #魔百盒
        # self.d(text=u"魔百盒").click()
        # sleep(2)
        # self.d.press("back")




if __name__=="__main__":
    pytest.main("test_010_yingshi_banner_dh.py")

