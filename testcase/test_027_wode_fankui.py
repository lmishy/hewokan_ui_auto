#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/8
import uiautomator2 as u2
from time import sleep
from po import proxy,ExcuteCase as E
import pytest
import allure

@E.E
@allure.step('我的--反馈')
def test_wode_fankui():
    str = proxy.url
    # 连接手机
    d = u2.connect(str)

    # 启动App
    d.app_start("com.chinamobile.cloudapp")

    # 切换我的tab
    d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
    sleep(2)
    #向上滑动
    d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)

    # 设置
    d(text=u"意见反馈").click()
    sleep(2)
    assert d(text=u"意见反馈").exists == True
    #输入文字
    d(resourceId="com.chinamobile.cloudapp:id/editText").set_text("APP很好，就是有些慢")
    sleep(2)
    #输入联系方式
    d(resourceId="com.chinamobile.cloudapp:id/editText2").set_text("546564565")
    sleep(2)
    d.press("back")
    sleep(2)
    d.press("back")
    sleep(5)
    # 停止app
    d.app_stop("com.chinamobile.cloudapp")



if __name__ == "__main__":
    pytest.main()


