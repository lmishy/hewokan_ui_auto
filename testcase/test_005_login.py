#coding=utf-8
import uiautomator2 as u2
from time import sleep
from po import proxy
import pytest
import allure


class Test_login():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        sleep(5)
        self.d.app_stop("com.chinamobile.cloudapp")

    @allure.step("手机登录失败")
    def test_login_fail(self):
        # 我的
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click(timeout=20)
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/head_pic").click(timeout=20)
        sleep(2)
        # 输入手机号码
        self.d(resourceId="com.chinamobile.cloudapp:id/edittext_phone").set_text('18428027801')
        sleep(2)
        # 输入错误密码
        self.d(resourceId="com.chinamobile.cloudapp:id/edittext_pwd").set_text('123245')
        sleep(2)
        # 登录
        self.d(resourceId="com.chinamobile.cloudapp:id/button_login").click(timeout=20)
        sleep(5)
        self.d(text=u"登录和我看").wait(timeout=10)
        assert self.d(text=u"登录和我看").exists 
        sleep(5)

    @allure.step("手机登录成功")
    def test_login_seccess(self):
        # 我的
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click(timeout=20)
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/head_pic").click(timeout=20)
        sleep(2)
        # 输入手机号码
        self.d(resourceId="com.chinamobile.cloudapp:id/edittext_phone").set_text('13981817893')
        sleep(2)
        # 输入错误密码
        self.d(resourceId="com.chinamobile.cloudapp:id/edittext_pwd").set_text('zhou1xin')
        sleep(2)
        # 登录
        self.d(resourceId="com.chinamobile.cloudapp:id/button_login").click(timeout=20)
        sleep(5)
        self.d(text=u"个人中心").wait(timeout=10)
        assert self.d(text=u"个人中心").exists 
        sleep(5)


if __name__=="__main__":
    pytest.main("test_005_login.py")


