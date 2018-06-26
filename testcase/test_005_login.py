#coding=utf-8
import uiautomator2 as u2
from time import sleep
from po import proxy,ExcuteCase as E
import pytest
import allure


@E.E
@allure.step("手机登录")
def test_login():
    str = proxy.url
    d = u2.connect(str)
    # 启动App
    d.app_start("com.chinamobile.cloudapp")
    sleep(2)
    # 我的
    d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/head_pic").click()
    sleep(2)
    # 输入手机号码
    d(resourceId="com.chinamobile.cloudapp:id/edittext_phone").set_text('18428027801')
    sleep(2)
    # 输入错误密码
    d(resourceId="com.chinamobile.cloudapp:id/edittext_pwd").set_text('123245')
    sleep(2)
    # 登录
    d(resourceId="com.chinamobile.cloudapp:id/button_login").click()
    sleep(5)
    assert d(text=u"登录和我看").exists == True
    sleep(2)
    # 输入手机号码

    d(resourceId="com.chinamobile.cloudapp:id/edittext_phone").clear_text()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/edittext_phone").set_text('13981817893')
    sleep(2)
    # 输入正确密码
    d(resourceId="com.chinamobile.cloudapp:id/edittext_pwd").clear_text()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/edittext_pwd").set_text('zhou1xin')
    sleep(2)
    # 登录
    d(resourceId="com.chinamobile.cloudapp:id/button_login").click()
    sleep(10)
    assert d(text=u"个人中心").exists == True

    sleep(10)
    # 停止app
    d.app_stop("com.chinamobile.cloudapp")




if __name__=="__main__":
    # test_login()
    pytest.main("test_005_login.py")


