#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/11

import uiautomator2 as u2
from time import sleep
from po import proxy,ExcuteCase as E
import pytest
import allure


@E.E
@allure.step("退出登录")
def test_login_out():
    str = proxy.url
    d = u2.connect(str)
    # 启动App
    d.app_start("com.chinamobile.cloudapp")
    sleep(5)
    # 我的
    d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
    sleep(5)

    d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
    if(d(resourceId="com.chinamobile.cloudapp:id/login_out").exists):
        d(resourceId="com.chinamobile.cloudapp:id/login_out").click()
        sleep(2)
        assert d(text=u"登录和我看").exists == True
    else:
        raise Exception(u"退出按钮不存在！")

    sleep(10)
    # 停止app
    d.app_stop("com.chinamobile.cloudapp")


if __name__=="__main__":
    pytest.main()