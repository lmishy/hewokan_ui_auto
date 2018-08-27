#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/8
import uiautomator2 as u2
from time import sleep
from po import proxy
import pytest
import allure

class Test_wode10():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        sleep(5)
        self.d.app_stop("com.chinamobile.cloudapp")

    @allure.step('我的--关于我们')
    def test_wode_guanyu(self):

        # 切换我的tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
        sleep(2)
        # 向上滑动
        self.d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)

        # 关于我们
        self.d(text=u"关于我们").click(timeout=20)
        sleep(2)
        assert self.d(text=u"关于").wait(exists=True,timeout=20)
        sleep(2)
        self.d(text=u"应用简介").click(timeout=20)
        sleep(5)
        assert self.d(text=u"应用简介").wait(exists=True,timeout=20)
        sleep(2)
        self.d.press("back")
        sleep(2)
        self.d(text=u"用户协议").click()
        sleep(5)
        assert self.d(text=u"和我看用户协议").wait(exists=True,timeout=20)
        sleep(2)
        # 向上滑动
        sleep(5)
        for i in range(5):
            self.d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
            sleep(1)
        self.d.press("back")
        self.d(text=u"分享和我看给好友").click(timeout=20)
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/btn_share_weChat_moments").click(timeout=20)
        sleep(2)
        self.d.press("back")
        sleep(2)
        self.d.press("back")
        sleep(2)
        self.d.press("back")
        sleep(5)
        assert self.d(text=u"个人中心").wait(exists=True,timeout=20)
        sleep(5)






if __name__ == "__main__":
    pytest.main("test_028_wode_guanyu.py")

