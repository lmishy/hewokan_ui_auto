#!/usr/bin/python3
# -*- coding:utf-8 -*-
#@time: 2018/6/6
import uiautomator2 as u2
from time import sleep
from po import proxy
import pytest
import allure

class Test_yingshi1():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        sleep(5)
        self.d.app_stop("com.chinamobile.cloudapp")

    @allure.step('影视--banner')
    def test_yingshi_banner(self):
        # 切换影视tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_3").click(timeout=20)
        sleep(2)
        # 播放其中一个视频
        self.d(resourceId="com.chinamobile.cloudapp:id/image").click(timeout=20)
        sleep(5)
        if (self.d(resourceId="com.chinamobile.cloudapp:id/video_collect_icon").exists):
            self.d(resourceId="com.chinamobile.cloudapp:id/video_collect_icon").click(timeout=20)
        else:
            assert self.d(resourceId="com.chinamobile.cloudapp:id/iv_share").wait(exists=True,timeout=20)
        sleep(2)
        self.d.press("back")
        sleep(5)

    @allure.step('影视--咪咕专区')
    def test_yingshi_migu(self):

        # 切换影视tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_3").click(timeout=20)
        sleep(2)
        # 咪咕专区
        self.d(text=u"咪咕视频").click(timeout=20)
        sleep(5)
        self.d(text=u"咪咕专区").wait(timeout=10)
        assert self.d(text=u"咪咕专区").wait(exists=True,timeout=20)
        self.d.press("back")


    @allure.step('影视--芒果专区')
    def test_yingshi_manggo(self):
        # 切换影视tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_3").click(timeout=20)
        sleep(2)
        # 芒果专区
        self.d(text=u"芒果TV").click(timeout=20)
        sleep(5)
        assert self.d(text=u"芒果TV-精选").wait(exists=True,timeout=20)
        self.d.press("back")


    @allure.step('影视--百视通专区')
    def test_yingshi_baishitong(self):
        # 切换影视tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_3").click(timeout=20)
        sleep(2)
        # 百视通专区
        self.d(text=u"百视通").click(timeout=20)
        sleep(5)
        assert self.d(text=u"百视通").wait(exists=True,timeout=20)
        sleep(5)
        self.d(text=u"首页").click(timeout=20)
        sleep(5)
        self.d(text=u"电影").click()
        sleep(5)
        self.d(text=u"电视剧").click()
        sleep(5)
        self.d(text=u"动漫").click()
        sleep(5)
        self.d(text=u"综艺").click()
        sleep(5)
        self.d(text=u"BBKING").click()
        sleep(5)
        self.d.press("back")
        sleep(5)

    @allure.step('影视--凤凰网')
    def test_yingshi_fenghuang(self):
        # 切换影视tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_3").click()
        sleep(2)
        # 凤凰网
        self.d(text=u"凤凰网").click(timeout=20)
        sleep(5)
        assert self.d(text=u"凤凰网专区").wait(exists=True,timeout=20)
        self.d.press("back")





if __name__=="__main__":
    pytest.main("test_010_yingshi_banner_dh.py")

