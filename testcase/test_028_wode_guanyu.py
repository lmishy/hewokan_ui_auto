#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/8
import uiautomator2 as u2
from time import sleep
from po import proxy,ExcuteCase as E
import pytest
import allure

@E.E
@allure.step('我的--关于我们')
def test_wode_guanyu():
    str = proxy.url
    # 连接手机
    d = u2.connect(str)

    # 启动App
    d.app_start("com.chinamobile.cloudapp")
    sleep(5)

    # 切换我的tab
    d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
    sleep(2)
    #向上滑动
    d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)

    #关于我们
    d(text=u"关于我们").click()
    sleep(2)
    assert d(text=u"关于").exists == True
    sleep(2)
    d(text=u"应用简介").click()
    sleep(5)
    assert d(text=u"应用简介").exists == True
    sleep(2)
    d.press("back")
    sleep(2)
    d(text=u"用户协议").click()
    sleep(5)
    assert d(text=u"和我看用户协议").exists == True
    sleep(2)
    # 向上滑动
    sleep(5)
    for i in range(5):
        d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
        sleep(1)
    d.press("back")
    d(text=u"分享和我看给好友").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/btn_share_weChat_moments").click()
    sleep(2)
    d.press("back")
    sleep(2)
    d.press("back")
    sleep(2)
    assert d(text=u"个人中心").exists == True
    sleep(2)
    d.press("back")

    sleep(5)
    # 停止app
    d.app_stop("com.chinamobile.cloudapp")




if __name__ == "__main__":
    test_wode_guanyu()
    # pytest.main()

