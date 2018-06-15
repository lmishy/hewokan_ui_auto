#!/usr/bin/python3
# -*- coding:utf-8 -*-
#@time: 2018/6/6
import uiautomator2 as u2
from time import sleep
from po import ExcuteCase as E, proxy
import uiautomator2 as u2
from time import sleep
from po import proxy,ExcuteCase as E
import pytest
import allure

@E.E
@allure.step('影视--即将上映--新片速递--重磅热播')
def test_yingshi_jjsy_xpsd_zbrb():
    str = proxy.url
    d = u2.connect(str)

    # 启动App
    d.app_start("com.chinamobile.cloudapp")

    # 切换影视tab
    d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_3").click()
    sleep(2)
    # 选择即将上映一个节目
    d(resourceId="com.chinamobile.cloudapp:id/cover_pic").click()
    sleep(5)
    assert d(resourceId="com.chinamobile.cloudapp:id/video_collect_icon").exists ==True
    d(resourceId="com.chinamobile.cloudapp:id/video_collect_icon").click()
    sleep(2)
    d.press("back")
    sleep(5)

    # 向上滑动
    sleep(5)
    for i in range(2):
        d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
        sleep(1)

    #选择新片速递一个节目
    d(resourceId="com.chinamobile.cloudapp:id/image", className="android.widget.ImageView", instance=1).click()
    sleep(6)
    d.press("back")
    sleep(2)
    #换一换
    d(text=u"换一换").click()
    sleep(2)
    #更多精彩
    d(text=u"更多精彩").click()
    sleep(5)
    assert d(text=u"电影").exists == True
    sleep(2)
    #全部电影
    d(text=u"内地").click()
    sleep(2)
    d(text=u"美国").click()
    sleep(2)
    d(text=u"韩国").click()
    sleep(2)
    d(text=u"香港").click()
    sleep(2)
    d(text=u"剧情").click()
    sleep(2)
    d(text=u"爱情").click()
    sleep(2)
    d(text=u"喜剧").click()
    sleep(2)
    d(text=u"动作").click()
    sleep(2)
    d(text=u"2017").click()
    sleep(2)
    d(text=u"2016").click()
    sleep(2)
    d(text=u"2015").click()
    sleep(2)
    d(text=u"2014").click()
    sleep(2)
    d(text=u"VIP").click()
    sleep(3)
    d.press("back")
    sleep(3)

    #向上滑动
    d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
    #点击任意一个节目
    d(resourceId="com.chinamobile.cloudapp:id/image", className="android.widget.ImageView", instance=2).click()
    sleep(5)
    d.press("back")
    #换一换
    sleep(5)
    d(text=u"换一换", className="android.widget.TextView", instance=1).click()
    #更多精彩
    d(text=u"更多精彩", className="android.widget.TextView", instance=1).click()
    sleep(5)
    assert d(text=u"电视剧").exists == True
    d.press("back")
    sleep(5)
    # 停止app
    d.app_stop("com.chinamobile.cloudapp")


if __name__=="__main__":
    # test_yingshi_jjsy_xpsd_zbrb()
    pytest.main()

