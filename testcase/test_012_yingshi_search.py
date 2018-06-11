#!/usr/bin/python3
# -*- coding:utf-8 -*-
#@time: 2018/6/6
import uiautomator2 as u2
from time import sleep
from po import proxy,ExcuteCase as E
import pytest
import allure

@E.E
@allure.step('影视--搜索')
def yingshi_search():
    str = proxy.url
    #连接手机
    d = u2.connect(str)

    # 启动App
    d.app_start("com.chinamobile.cloudapp")

    #切换影视tab
    d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_3").click()
    sleep(2)


    #搜索功能-数字
    d(resourceId="com.chinamobile.cloudapp:id/home_cloud_title_right_search").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/et_content").set_text("12")
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/title_right_img_2").click()
    sleep(5)
    d(resourceId="com.chinamobile.cloudapp:id/more").click()
    sleep(2)
    d.press("back")
    sleep(2)
    d.press("back")
    sleep(2)
    # 搜索功能-中文
    d(resourceId="com.chinamobile.cloudapp:id/et_content").set_text("萝莉")
    sleep(5)
    d(resourceId="com.chinamobile.cloudapp:id/title_right_img_2").click()
    sleep(2)
    d.press("back")
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/textView", text=u"1.唐人街探案2").click()
    sleep(5)
    d.press("back")
    sleep(2)
    d.press("back")
    sleep(2)
    # 搜索功能-英文
    d(resourceId="com.chinamobile.cloudapp:id/et_content").set_text("boy")
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/title_right_img_2").click()
    sleep(5)
    d.press("back")
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/textView", text=u"1.唐人街探案2").click()
    sleep(2)
    d.press("back")
    sleep(2)
    d.press("back")
    sleep(5)
    # 停止app
    d.app_stop("com.chinamobile.cloudapp")


def test_yingshi_search():
    yingshi_search()

if __name__=="__main__":
    # str = proxy.url
    # yingshi_search(str)
    pytest.main()

