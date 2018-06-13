#!/usr/bin/python3
# -*- coding:utf-8 -*-
#@time: 2018/6/6
import uiautomator2 as u2
from time import sleep
from po import proxy,ExcuteCase as E
import pytest
import allure

@E.E
@allure.step('影视--banner--导航')
def test_yingshi_banner_dh():
    str = proxy.url
    #连接手机
    d = u2.connect(str)

    # 启动App
    d.app_start("com.chinamobile.cloudapp")

    #切换影视tab
    d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_3").click()
    sleep(2)
    #播放其中一个视频
    d(resourceId="com.chinamobile.cloudapp:id/image").click()
    sleep(5)
    d(resourceId="com.chinamobile.cloudapp:id/video_collect_icon").click()
    sleep(2)
    d.press("back")
    sleep(2)
    #咪咕专区
    d(text=u"咪咕视频").click()
    sleep(5)
    d(text=u"咪咕专区").wait(timeout=10)
    assert d(text=u"咪咕专区").exists == True
    d.press("back")
    sleep(2)
    #芒果专区
    d(text=u"芒果TV").click()
    sleep(5)
    assert d(text=u"芒果TV-精选").exists == True
    d.press("back")
    sleep(2)
    #百视通专区
    d(text=u"百视通").click()
    sleep(5)
    assert d(text=u"百视通").exists == True
    d.press("back")
    #凤凰网
    d(text=u"凤凰网").click()
    sleep(5)
    assert d(text=u"凤凰网专区").exists == True
    d.press("back")
    sleep(2)
    # #魔百盒
    # d(text=u"魔百盒").click()
    # sleep(2)
    # d.press("back")
    sleep(5)
    # 停止app
    d.app_stop("com.chinamobile.cloudapp")


if __name__=="__main__":
    test_yingshi_banner_dh()
    # pytest.main()

