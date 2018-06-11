#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/7

import uiautomator2 as u2
from time import sleep
from po import proxy,ExcuteCase as E
import pytest
import allure

@E.E
@allure.step('我的--分享')
def wode_fenxiang():
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
    d(resourceId="com.chinamobile.cloudapp:id/invitation_reward_record_btn").click()
    sleep(2)
    d.press("back")
    sleep(2)
    #分享邀请好友
    d(resourceId="com.chinamobile.cloudapp:id/invitation_reward_share_btn").click()
    sleep(2)
    d.press("back")
    d.press("back")
    sleep(5)
    # 停止app
    d.app_stop("com.chinamobile.cloudapp")

def test_fengxiang():
    wode_fenxiang()


if __name__ == "__main__":
    # str = proxy.url
    # wode_fenxiang(str)
    pytest.main()

