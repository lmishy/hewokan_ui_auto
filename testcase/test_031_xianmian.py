#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/14
import uiautomator2 as u2
from time import sleep
from po import ExcuteCase as E, proxy
import pytest
import allure

@E.E
@allure.step('热点--限免')
def test_xianmian():
    str = proxy.url
    d = u2.connect(str)

    # 启动App
    d.app_start("com.chinamobile.cloudapp")

    # 限免专区
    d(text=u"限免专区").click()
    sleep(5)
    assert d(text=u"限免专区").exists == True
    sleep(5)
    #点击banner
    if(d(resourceId="com.chinamobile.cloudapp:id/image").exists):
        d(resourceId="com.chinamobile.cloudapp:id/image").click()
        sleep(5)
        d.press("back")
    else:
        raise Exception(u"页面请求时间过长，请检查！")



    #即将限免的一部
    if(d(resourceId="com.chinamobile.cloudapp:id/cover_pic").exists):
        d(resourceId="com.chinamobile.cloudapp:id/cover_pic").click()
        sleep(5)
        d.press("back")
    else:
        raise Exception(u"找不到控件")

    #高分电影大放送
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/image", className="android.widget.ImageView", instance=1).click()
    sleep(5)
    d.press("back")
    sleep(2)
    d.press("back")
    sleep(5)
    assert d(text=u"热点").exists == True


    # 停止app
    d.app_stop("com.chinamobile.cloudapp")




if __name__=="__main__":
    # test_hot()
    pytest.main("test_031_xianmian.py")

