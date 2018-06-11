#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/8
import uiautomator2 as u2
from time import sleep
from po import proxy,ExcuteCase as E
import pytest
import allure

@E.E
@allure.step('我的--和包')
def wode_hebao():
    str = proxy.url
    # 连接手机
    d = u2.connect(str)

    # 启动App
    d.app_start("com.chinamobile.cloudapp")

    # 切换我的tab
    d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
    sleep(2)
    # 和包
    d(resourceId="com.chinamobile.cloudapp:id/andpacket").click()
    sleep(6)
    d.press("back")
    sleep(5)
    # 停止app
    d.app_stop("com.chinamobile.cloudapp")

def test_hebao():
    wode_hebao()

if __name__ == "__main__":
    # str = proxy.url
    # wode_hebao(str)
    pytest.main()

