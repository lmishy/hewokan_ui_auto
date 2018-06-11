#coding=utf-8
import uiautomator2 as u2
from time import sleep
from po import proxy,ExcuteCase as E
import pytest
import allure


@E.E
@allure.step("手机登录")
def login(user,pwd):
    str = proxy.url
    d = u2.connect(str)
    # 启动App
    d.app_start("com.chinamobile.cloudapp")
    # 我的
    d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/head_pic").click()
    sleep(2)
    # 输入手机号码
    d(resourceId="com.chinamobile.cloudapp:id/edittext_phone").set_text(user)
    sleep(2)
    # 输入错误密码
    d(resourceId="com.chinamobile.cloudapp:id/edittext_pwd").set_text(pwd)
    sleep(2)
    # 登录
    d(resourceId="com.chinamobile.cloudapp:id/button_login").click()
    #return d.info()
    sleep(5)
    #if d(resourceId="com.chinamobile.cloudapp:id/button_login").wait(10)

    #d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
    #d(resourceId="com.chinamobile.cloudapp:id/login_out").click()

    sleep(10)
    # 停止app
    d.app_stop("com.chinamobile.cloudapp")



def test_loginfail():
    login('18428027801','123245')

def test_loginsuccess():
    login('18428027801','qqq111')

if __name__=="__main__":
    # str = proxy.url
    # login(str)
    pytest.main()


