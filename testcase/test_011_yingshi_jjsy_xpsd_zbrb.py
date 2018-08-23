#!/usr/bin/python3
# -*- coding:utf-8 -*-
#@time: 2018/6/6

import uiautomator2 as u2
from time import sleep
from po import proxy
import pytest
import allure

class Test_yingshi2():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        sleep(5)
        self.d.app_stop("com.chinamobile.cloudapp")

    @pytest.mark.skip(resean= 'other')
    @allure.step('影视--即将上映')
    def test_yingshi_jjsy(self):
        # 切换影视tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_3").click()
        sleep(2)
        # 选择即将上映一个节目
        if (self.d(resourceId="com.chinamobile.cloudapp:id/title", text=u"即将上映").exists):
            self.d(resourceId="com.chinamobile.cloudapp:id/cover_pic").click()
            sleep(5)
            self.d(resourceId="com.chinamobile.cloudapp:id/video_collect_icon").click()
            sleep(2)
            assert self.d(resourceId="com.chinamobile.cloudapp:id/video_collect_icon").exists 
            self.d.press("back")

        else:
            raise Exception(u"没有这个分区！")

    @pytest.mark.skip(resean='other')
    @allure.step('影视--每日限免')
    def test_yingshi_mrxm(self):
        # 切换影视tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_3").click()
        sleep(2)
        # 向上滑动
        sleep(5)
        self.d.swipe(0.5, 0.7, 0.5, 0.3, 0.5)
        sleep(3)
        if (self.d(resourceId="com.chinamobile.cloudapp:id/title", text=u"每日限免").exists):
            self.d(resourceId="com.chinamobile.cloudapp:id/cover_pic", className="android.widget.ImageView", instance=3).click()
            sleep(3)
            self.d.press("back")

        else:
            raise Exception(u"没有这个分区！")


    @allure.step('影视--新片速递')
    def test_yingshi_xpsd(self):
        # 切换影视tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_3").click()
        sleep(2)
        # 向上滑动
        sleep(5)
        for i in range(2):
            self.d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
            sleep(1)

        self.d(resourceId="com.chinamobile.cloudapp:id/image", className="android.widget.ImageView", instance=3).click()
        sleep(6)
        self.d.press("back")
        self.d.press("back")
        sleep(2)
        # 换一换
        self.d(text=u"换一换").click()
        sleep(2)
        # 更多精彩
        self.d(text=u"更多精彩").click()
        sleep(5)
        assert self.d(text=u"电影").wait(exists=True,timeout=20)
        sleep(2)
        # 全部电影
        self.d(text=u"内地").click()
        sleep(2)
        self.d(text=u"美国").click()
        sleep(2)
        self.d(text=u"韩国").click()
        sleep(2)
        self.d(text=u"香港").click()
        sleep(2)
        self.d(text=u"剧情").click()
        sleep(2)
        self.d(text=u"爱情").click()
        sleep(2)
        self.d(text=u"喜剧").click()
        sleep(2)
        self.d(text=u"动作").click()
        sleep(2)
        self.d(text=u"2017").click()
        sleep(2)
        self.d(text=u"2016").click()
        sleep(2)
        self.d(text=u"2015").click()
        sleep(2)
        self.d(text=u"2014").click()
        sleep(2)
        self.d(text=u"VIP").click()
        sleep(3)
        self.d.press("back")

    @pytest.mark.skip(resean='other')
    @allure.step('影视--重磅热播')
    def test_yingshi_zbrb(self):
        # 切换影视tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_3").click()
        sleep(2)
        # 向上滑动
        sleep(5)
        for i in range(3):
            self.d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
            sleep(1)
        # 点击任意一个节目
        self.d(resourceId="com.chinamobile.cloudapp:id/image", className="android.widget.ImageView", instance=2).click()
        sleep(5)
        self.d.press("back")
        # 换一换
        sleep(5)
        self.d(text=u"换一换", className="android.widget.TextView", instance=1).click()
        # 更多精彩
        self.d(text=u"更多精彩", className="android.widget.TextView", instance=1).click()
        sleep(5)
        assert self.d(text=u"电视剧").wait(exists=True,timeout=20)
        self.d.press("back")





if __name__=="__main__":
    pytest.main("test_011_yingshi_jjsy_xpsd_zbrb.py")

