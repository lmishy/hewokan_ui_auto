#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/7
import uiautomator2 as u2
from time import sleep
from po import proxy,ExcuteCase as E
import pytest
import allure

@E.E
@allure.step('爱看--阿里体育')
def test_aikan_alitiyu():
    str = proxy.url
    #连接手机
    d = u2.connect(str)

    # 启动App
    d.app_start("com.chinamobile.cloudapp")

    #切换爱看tab
    d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_4").click()
    sleep(2)
    #阿里体育
    d(text=u"阿里体育").click()
    sleep(2)
    #播放实时直播
    d(resourceId="com.chinamobile.cloudapp:id/image_mid", className="android.widget.ImageView", instance=2).click()
    sleep(2)
    d.press("back")
    sleep(2)
    #精彩集锦
    d(resourceId="com.chinamobile.cloudapp:id/image_mid", className="android.widget.ImageView", instance=2).click()
    sleep(2)
    d.press("back")
    sleep(2)
    #向上滑动三次
    for i in range(3):
        d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
        sleep(1)

    #3X3联赛广州站
    d(resourceId="com.chinamobile.cloudapp:id/image_mid").click()
    sleep(5)
    d.press("back")
    sleep(2)

    # 向上滑动两次
    for i in range(2):
        d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
        sleep(1)

    #激情拉拉队
    d(resourceId="com.chinamobile.cloudapp:id/image_mid").click()
    sleep(5)
    d.press("back")

    sleep(5)
    # 停止app
    d.app_stop("com.chinamobile.cloudapp")

if __name__=="__main__":
    pytest.main()

