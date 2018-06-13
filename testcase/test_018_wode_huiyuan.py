#!/usr/bin/python3
# -*- coding:utf-8 -*-
#@time: 2018/6/7
import uiautomator2 as u2
from time import sleep
from po import proxy,ExcuteCase as E
import pytest
import allure

@E.E
@allure.step('我的--会员')
def wode_huiyuan():
    str = proxy.url
    # 连接手机
    d = u2.connect(str)

    # 启动App
    d.app_start("com.chinamobile.cloudapp")

    # 切换我的tab
    d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
    sleep(2)
    # 会员中心
    d(resourceId="com.chinamobile.cloudapp:id/member_area").click()
    sleep(2)
    # 查看用户协议
    d(resourceId="com.chinamobile.cloudapp:id/tv_user_agreement").click()
    sleep(6)
    # 向上滑动六次
    for i in range(6):
        d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
        sleep(1)
    d.press("back")
    sleep(2)
    # 芒果TV
    d(resourceId="com.chinamobile.cloudapp:id/tv_vip_name", text=u"芒果TV").click()
    sleep(2)
    d(description=u"立即订购").click()
    sleep(2)
    d.press("back")
    d.press("back")

    # 百视通VIP
    d(resourceId="com.chinamobile.cloudapp:id/tv_vip_name", text=u"百视通VIP").click()
    sleep(2)
    d(description=u"立即订购").click()
    sleep(2)
    d.press("back")
    d.press("back")

    # 咪咕会员VIP
    d(resourceId="com.chinamobile.cloudapp:id/btn_order").click()
    d.press("back")
    d.press("back")

    sleep(5)
    # 停止app
    d.app_stop("com.chinamobile.cloudapp")

def test_huiyuan():
    wode_huiyuan()


if __name__ == "__main__":
    pytest.main()
