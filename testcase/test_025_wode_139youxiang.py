#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/8
import uiautomator2 as u2
from time import sleep
from po import proxy
import pytest
import allure

class Test_wode7():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        sleep(5)
        self.d.app_stop("com.chinamobile.cloudapp")

    @allure.step('我的--139邮箱')
    def test_wode_139youxiang(self):
        
        # 切换我的tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
        sleep(2)
        # 向上滑动
        self.d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
        # 139邮箱
        self.d(text=u"139邮箱").click()
        sleep(6)
        assert self.d(text=u"139邮箱").exists 
        self.d.press("back")
        sleep(5)



if __name__ == "__main__":
    pytest.main("test_025_wode_139youxiang.py")

