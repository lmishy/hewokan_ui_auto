#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/8
import uiautomator2 as u2
from time import sleep
from po import proxy
import pytest
import allure

class Test_wode11():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        sleep(5)
        self.d.app_stop("com.chinamobile.cloudapp")

    @allure.step('我的--换头像')
    def test_wode_qita_change(self):
        # 切换我的tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
        sleep(2)
        assert self.d(text=u"个人中心").wait(exists=True,timeout=20)
        # 换头像
        self.d(resourceId="com.chinamobile.cloudapp:id/head_pic").click()
        sleep(5)
        self.d(resourceId="com.chinamobile.cloudapp:id/textView1").click()
        sleep(2)
        if (self.d(resourceId="com.oppo.camera:id/camera_from_other_app_close_btn").exists):
            self.d(resourceId="com.oppo.camera:id/camera_from_other_app_close_btn").click()
        else:
            self.d.press("back")
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/head_pic").click()
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/textView2").click()
        sleep(2)
        self.d.press("back")
        if (self.d(text=u"个人中心").exists):
            pass
        else:
            self.d.press("back")
        assert self.d(text=u"个人中心").wait(exists=True,timeout=20)
        sleep(2)

    @allure.step('我的--签到')
    def test_wode_qiandao(self):
        # 切换我的tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
        sleep(2)
        assert self.d(text=u"个人中心").wait(exists=True,timeout=20)
        # 签到
        self.d(resourceId="com.chinamobile.cloudapp:id/sign_button").click()
        sleep(2)
        if (self.d(text=u"未签到").exists):
            self.d(resourceId="headerUpP").click()
            sleep(2)
            assert self.d(text=u"已签到").wait(exists=True,timeout=20)
        else:
            self.d.press("back")

        sleep(5)



if __name__ == "__main__":
    pytest.main("test_029_wode_qita.py")

