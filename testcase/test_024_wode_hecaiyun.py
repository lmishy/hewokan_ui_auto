#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/8
import uiautomator2 as u2
from time import sleep
from po import proxy,ExcuteCase as E
import pytest
import allure

@E.E
@allure.step('我的--和彩云')
def test_wode_hecaiyun():
    str = proxy.url
    # 连接手机
    d = u2.connect(str)

    # 启动App
    d.app_start("com.chinamobile.cloudapp")

    # 切换我的tab
    d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
    sleep(2)
    # 和彩云
    d(text=u"和彩云").click()
    sleep(2)
    d.press("back")
    sleep(2)
    d.press("back")
    sleep(2)
    d.press("back")
    sleep(5)
    d.press("back")
    sleep(5)
    # 停止app
    d.app_stop("com.chinamobile.cloudapp")


if __name__ == "__main__":
    pytest.main()

