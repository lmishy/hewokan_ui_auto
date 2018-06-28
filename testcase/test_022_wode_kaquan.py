#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/7
import uiautomator2 as u2
from time import sleep
from po import proxy
import pytest
import allure

class Test_wode4():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        self.d.app_stop("com.chinamobile.cloudapp")

    @allure.step('我的--我的卡券')
    def test_wode_kaquan(self):
        # 切换我的tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
        sleep(2)
        # 我的卡劵
        self.self.d(text=u"我的卡劵").click()
        sleep(5)
        self.d(description=u"已使用").click()
        sleep(2)
        self.d(description=u"已过期").click()
        sleep(2)
        self.d(description=u"未使用").click()
        assert self.d(description=u"未使用").exists == True
        self.d.press("back")
        sleep(5)





if __name__ == "__main__":
    pytest.main("test_022_wode_kaquan.py")

