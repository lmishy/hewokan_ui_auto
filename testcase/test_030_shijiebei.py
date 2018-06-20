#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/14
import uiautomator2 as u2
from time import sleep
from po import ExcuteCase as E, proxy
import pytest
import allure

@E.E
@allure.step('热点--世界杯专区')
def test_shijiebei():
    str = proxy.url
    d = u2.connect(str)

    # 启动App
    d.app_start("com.chinamobile.cloudapp")

    # 世界杯专区
    d(text=u"世界杯专区").click()
    sleep(5)
    assert d(text=u"世界杯专区").exists == True
    sleep(5)
    #点击banner
    if(d(resourceId="com.chinamobile.cloudapp:id/image").exists):
        d(resourceId="com.chinamobile.cloudapp:id/image").click(timeout=10)
        d(resourceId="com.chinamobile.cloudapp:id/home_cloud_title").wait(timeout=10)
        if (d(text=u"咪咕钻石会员-超级视频").exists()):
            sleep(5)
            d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
            sleep(2)
            #点击开通
            d(description=u"btn").click()
            sleep(2)
            d(resourceId="close").click(timeout=5)
            d.press("back")
        elif (d(text=u"世界杯").exists):
            #分享
            d(resourceId="share").click(timeout=5)
            d.press("back")
            #活动规则
            d(resourceId="rules").click(timeout=5)
            d(resourceId="cover2").click(timeout=5)
            #会员兑换
            d(resourceId="exchange").click(timeout=5)
            #大厅
            d(resourceId="hall").click(timeout=5)
            #我的竞猜
            d(resourceId="myguess").click(timeout=5)
            d.press("back")
        else:
            raise Exception(u"页面时间请求过长！")

    else:
        raise Exception(u"页面请求时间过长，请检查！")



    #赛程安排
    if(d(text=u"赛程安排").exists):
        d(text=u"赛程安排").click()
        sleep(5)
        d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
        d.press("back")
    else:
        raise Exception(u"找不到控件")

    #猜球有奖
    if(d(text=u"猜球有奖").exists):
        d(text=u"猜球有奖").click()
        sleep(5)
        d.press("back")
    else:
        raise Exception(u"找不到控件")

    # 福利领取
    if (d(text=u"福利领取").exists):
        d(text=u"福利领取").click()
        sleep(5)
        d.press("back")
    else:
        raise Exception(u"找不到控件")

    # 福利领取
    if (d(text=u"前线战报").exists):
        d(text=u"前线战报").click()
        sleep(5)
        d.press("back")
    else:
        raise Exception(u"找不到控件")

    d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
    # 停止app
    d.app_stop("com.chinamobile.cloudapp")




if __name__=="__main__":
    test_shijiebei()
    # pytest.main("test_030_shijiebei.py")

