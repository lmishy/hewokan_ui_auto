#coding=utf-8
import uiautomator2 as u2
from time import sleep
from po import ExcuteCase as E, proxy
import pytest
import allure

@E.E
@allure.step('一键登录')
def login_yi():
    str = proxy.url
    d = u2.connect(str)

    # 启动App
    d.app_start("com.chinamobile.cloudapp")

    # 我的
    d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
    if d(resourceId="com.chinamobile.cloudapp:id/head_pic").exists:
        d(resourceId="com.chinamobile.cloudapp:id/head_pic").click()
    else:
        raise Exception(u"没有找到控件!")


    # 一键登录
    d(resourceId="com.chinamobile.cloudapp:id/fl_login_yidong").click()
    sleep(5)
    if d(text=u"个人中心").exists:
        sleep(5)
        d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
        d(resourceId="com.chinamobile.cloudapp:id/login_out").click()

    else:
        raise Exception(u"出错了，没有登录手机号！")

    sleep(5)
    # 停止app
    d.app_stop("com.chinamobile.cloudapp")

def test_login_yi():
    login_yi()


if __name__=="__main__":
    # str = proxy.url
    # login_yi(str)
    pytest.main()


