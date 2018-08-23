#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/14
import uiautomator2 as u2
from time import sleep
from po import proxy
import pytest
import allure

class Test_xianmian():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        sleep(5)
        self.d.app_stop("com.chinamobile.cloudapp")

    @allure.step('热点--banner')
    def test_xianmian_banner(self):

        # 限免专区
        self.d(text=u"限免专区").click()
        sleep(5)
        assert self.d(text=u"限免专区").wait(exists=True,timeout=20)
        sleep(5)
        # 点击banner
        if (self.d(resourceId="com.chinamobile.cloudapp:id/image").exists):
            self.d(resourceId="com.chinamobile.cloudapp:id/image").click()
            sleep(5)
            self.d.press("back")
        else:
            raise Exception(u"页面请求时间过长，请检查！")

    @allure.step('热点--即将转免')
    def test_xianmian_jijian(self):
        # 限免专区
        self.d(text=u"限免专区").click()
        sleep(5)
        assert self.d(text=u"限免专区").wait(exists=True,timeout=20)
        sleep(5)
        # 即将限免的一部
        if (self.d(resourceId="com.chinamobile.cloudapp:id/cover_pic").exists):
            self.d(resourceId="com.chinamobile.cloudapp:id/cover_pic").click()
            sleep(5)
            self.d.press("back")
        else:
            raise Exception(u"找不到控件")

    @allure.step('热点--高分电影大放送')
    def test_xianmian_gaofeng(self):
        # 限免专区
        self.d(text=u"限免专区").click()
        sleep(5)
        assert self.d(text=u"限免专区").wait(exists=True,timeout=20)
        sleep(5)
        # 高分电影大放送
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/image", className="android.widget.ImageView", instance=1).click()
        sleep(5)
        self.d.press("back")
        sleep(2)
        self.d.press("back")
        sleep(5)
        assert self.d(text=u"热点").wait(exists=True,timeout=20)




if __name__=="__main__":
    pytest.main("test_031_xianmian.py")

