#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/8
import uiautomator2 as u2
from time import sleep
from po import proxy
import pytest
import allure

class Test_wode6():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        sleep(5)
        self.d.app_stop("com.chinamobile.cloudapp")

    @allure.step('我的--和彩云')
    def test_wode_hecaiyun(self):
        
        # 切换我的tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
        sleep(2)
        # 和彩云
        self.d(text=u"和彩云").click()
        sleep(2)
        self.d.press("back")
        sleep(2)
        self.d.press("back")
        sleep(2)
        self.d.press("back")
        sleep(5)
        self.d.press("back")
        sleep(5)



if __name__ == "__main__":
    pytest.main("test_024_wode_hecaiyun.py")

