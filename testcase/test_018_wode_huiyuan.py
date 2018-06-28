#!/usr/bin/python3
# -*- coding:utf-8 -*-
#@time: 2018/6/7
import uiautomator2 as u2
from time import sleep
from po import proxy
import pytest
import allure

class Test_wode():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        self.d.app_stop("com.chinamobile.cloudapp")

    @allure.step('我的--会员')
    def test_huiyuan_xieyi(self):

        # 切换我的tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
        sleep(2)
        # 会员中心
        self.d(resourceId="com.chinamobile.cloudapp:id/member_area").click()
        sleep(2)
        # 查看用户协议
        self.d(resourceId="com.chinamobile.cloudapp:id/tv_user_agreement").click()
        sleep(6)
        # 向上滑动六次
        for i in range(6):
            self.d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
            sleep(1)
        self.d.press("back")
        sleep(2)

    @allure.step('我的--芒果VIP')
    def test_huiyuan_manggo(self):
        # 切换我的tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
        sleep(2)
        # 会员中心
        self.d(resourceId="com.chinamobile.cloudapp:id/member_area").click()
        sleep(2)
        # 芒果TV
        self.d(resourceId="com.chinamobile.cloudapp:id/iv_logo", className="android.widget.ImageView", instance=1).click()
        sleep(2)
        self.d(className="com.tencent.smtt.webkit.WebView").click()
        sleep(2)
        self.d.press("back")
        self.d.press("back")

    @allure.step('我的--百视通VIP')
    def test_huiyuan_baishitong(self):
        # 切换我的tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
        sleep(2)
        # 会员中心
        self.d(resourceId="com.chinamobile.cloudapp:id/member_area").click()
        sleep(2)
        # 百视通VIP
        self.d(resourceId="com.chinamobile.cloudapp:id/iv_logo", className="android.widget.ImageView", instance=2).click()
        sleep(2)
        self.d(className="com.tencent.smtt.webkit.WebView").click()
        sleep(2)
        self.d.press("back")
        self.d.press("back")

    @allure.step('我的--咪咕会员VIP')
    def test_huiyuan_migu(self):
        # 咪咕会员VIP
        self.d(resourceId="com.chinamobile.cloudapp:id/iv_logo").click()
        self.d.press("back")
        self.d.press("back")






if __name__ == "__main__":
    pytest.main("test_018_wode_huiyuan.py")
