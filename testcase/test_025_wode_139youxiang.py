#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/8
import uiautomator2 as u2
from time import sleep
from po import proxy,ExcuteCase as E
import pytest
import allure

@E.E
@allure.step('我的--139邮箱')
def wode_139youxiang():
    str = proxy.url
    # 连接手机
    d = u2.connect(str)

    # 启动App
    d.app_start("com.chinamobile.cloudapp")

    # 切换我的tab
    d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
    sleep(2)
    #向上滑动
    d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
    # 139邮箱
    d(text=u"139邮箱").click()
    sleep(6)
    d.press("back")
    sleep(5)
    # 停止app
    d.app_stop("com.chinamobile.cloudapp")

def test_139youxiang():
    wode_139youxiang()


if __name__ == "__main__":
    # str = proxy.url
    # wode_139youxiang(str)
    pytest.main()

