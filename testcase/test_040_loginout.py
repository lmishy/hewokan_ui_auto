#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/11
import uiautomator2 as u2
from time import sleep
from po import proxy
import pytest
import allure

class Test_loginout():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        sleep(5)
        self.d.app_stop("com.chinamobile.cloudapp")

    @allure.step("退出登录")
    def test_login_out(self):
        # 我的
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
        sleep(5)
        self.d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
        if (self.d(resourceId="com.chinamobile.cloudapp:id/login_out").exists):
            self.d(resourceId="com.chinamobile.cloudapp:id/login_out").click()
            sleep(2)
            assert self.d(text=u"个人中心").exists
        else:
            raise Exception(u"退出按钮不存在！")




if __name__=="__main__":
    pytest.main("test_040_loginout.py")