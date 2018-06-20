#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/7

import uiautomator2 as u2
from time import sleep
import time
from po import proxy,ExcuteCase as E
import pytest
import allure

@E.E
@allure.step('我的--分享')
def test_wode_fenxiang():
    str = proxy.url
    # 连接手机
    d = u2.connect(str)

    # 启动App
    d.app_start("com.chinamobile.cloudapp")

    # 切换我的tab
    d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
    sleep(2)
    # 分享有奖
    d(resourceId="com.chinamobile.cloudapp:id/welfare_area").click()
    sleep(2)
    #邀请记录
    d(resourceId="btn1").click()
    sleep(2)
    assert d(description=u"用户名").exists == True
    d.press("back")
    sleep(2)
    #分享邀请好友
    d(resourceId="inviteBtn").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/btn_share_weChat").click()
    sleep(2)
    d.press("back")
    d.press("back")
    d.press("back")
    sleep(5)
    # 停止app
    d.app_stop("com.chinamobile.cloudapp")



if __name__ == "__main__":
    pytest.main("test_019_wode_fenxiang.py")

