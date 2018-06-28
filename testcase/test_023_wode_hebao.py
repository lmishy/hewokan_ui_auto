#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/8
import uiautomator2 as u2
from time import sleep
from po import proxy
import pytest
import allure

class Test_wode5():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        self.d.app_stop("com.chinamobile.cloudapp")

    @allure.step('我的--和包')
    def test_wode_hebao(self):

        # 切换我的tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
        sleep(2)
        # 和包
        self.d(resourceId="com.chinamobile.cloudapp:id/andpacket").click()
        sleep(6)
        assert self.d(text=u"和包").exists == True
        self.d.press("back")
        sleep(5)


if __name__ == "__main__":
    pytest.main("test_023_wode_hebao.py")

