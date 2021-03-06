#!/usr/bin/python3
# -*- coding:utf-8 -*-
#@time: 2018/6/6
import uiautomator2 as u2
from time import sleep
from po import proxy
import pytest
import allure

class Test_yingshi3():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        sleep(5)
        self.d.app_stop("com.chinamobile.cloudapp")

    @allure.step('影视--搜索--数字')
    def test_search_shuzi(self):
        # 切换影视tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_3").click(timeout=20)
        sleep(2)
        # 搜索功能-数字
        self.d(resourceId="com.chinamobile.cloudapp:id/home_cloud_title_right_search").click(timeout=20)
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/et_content").set_text(u"12")
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/title_right_img_2").click(timeout=20)
        sleep(5)
        assert self.d(text=u"12-喇叭花-伴奏").wait(exists=True, timeout=20)
        sleep(5)
        if (self.d(resourceId="com.chinamobile.cloudapp:id/more").exists):
            self.d(resourceId="com.chinamobile.cloudapp:id/more").click()
            sleep(2)
            self.d.press("back")
        else:
            pass
            print(u"页面加载过长！")
        sleep(2)
        self.d.press("back")
        sleep(2)

    @allure.step('影视--搜索--中文')
    def test_search_chinese(self):
        # 切换影视tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_3").click()
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/home_cloud_title_right_search").click()
        sleep(2)
        # 搜索功能-中文
        self.d(resourceId="com.chinamobile.cloudapp:id/et_content").set_text(u"萝莉")
        sleep(5)
        self.d(resourceId="com.chinamobile.cloudapp:id/title_right_img_2").click()
        sleep(5)
        assert self.d(text=u"摇滚萝莉").wait(exists=True, timeout=20)
        sleep(2)
        self.d.press("back")
        sleep(2)

    @allure.step('影视--搜索--英文')
    def test_search_english(self):
        # 切换影视tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_3").click()
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/home_cloud_title_right_search").click()
        sleep(2)
        # 搜索功能-英文
        self.d(resourceId="com.chinamobile.cloudapp:id/et_content").set_text(u"boy")
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/title_right_img_2").click()
        sleep(5)
        assert self.d(text=u"MES sentence chant boy").wait(exists=True, timeout=20)
        sleep(2)
        self.d.press("back")
        sleep(2)

    @allure.step('影视--搜索--推荐')
    def test_search_tuijian(self):
        # 切换影视tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_3").click()
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/home_cloud_title_right_search").click()
        sleep(2)
        # 搜索功能-推荐
        self.d(resourceId="com.chinamobile.cloudapp:id/textView", text=u"4.小猪佩奇").click()
        sleep(2)
        assert self.d(text=u"小猪佩奇第二季").wait(exists=True,timeout=20)
        sleep(2)
        self.d.press("back")
        sleep(2)
        self.d.press("back")
        sleep(5)



if __name__=="__main__":
    pytest.main("test_012_yingshi_search.py")

