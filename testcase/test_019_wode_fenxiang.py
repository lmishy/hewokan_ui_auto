#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/7

import uiautomator2 as u2
from time import sleep
from po import proxy
import pytest
import allure

class Test_wode1():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        sleep(5)
        self.d.app_stop("com.chinamobile.cloudapp")

    @allure.step('我的--分享')
    def test_wode_fenxiang(self):
        # 切换我的tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
        sleep(2)
        # 分享有奖
        self.d(resourceId="com.chinamobile.cloudapp:id/welfare_area").click()
        sleep(5)
        # 邀请记录
        self.d(resourceId="btn1").click()
        sleep(5)
        assert self.d(description=u"用户名").wait(exists=True,timeout=20)
        self.d.press("back")
        sleep(2)
        # 分享邀请好友
        self.d(resourceId="inviteBtn").click()
        sleep(5)
        self.d(resourceId="com.chinamobile.cloudapp:id/btn_share_weChat").click()
        sleep(2)
        self.d.press("back")
        self.d.press("back")
        self.d.press("back")
        sleep(5)



if __name__ == "__main__":
    pytest.main("test_019_wode_fenxiang.py")

