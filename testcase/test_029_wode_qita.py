#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/8
import uiautomator2 as u2
from time import sleep
from po import proxy,ExcuteCase as E
import pytest
import allure

@E.E
@allure.step('我的--签到--换头像')
def test_wode_qita():
    str = proxy.url
    # 连接手机
    d = u2.connect(str)

    # 启动App
    d.app_start("com.chinamobile.cloudapp")

    # 切换我的tab
    d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
    sleep(2)
    assert d(text=u"个人中心").exists == True
    # 换头像
    d(resourceId="com.chinamobile.cloudapp:id/head_pic").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/textView1").click()
    sleep(2)
    d(resourceId="com.oppo.camera:id/camera_from_other_app_close_btn").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/head_pic").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/textView2").click()
    sleep(2)
    d.press("back")
    assert d(text=u"个人中心").exists ==True
    sleep(2)
    #签到
    d(resourceId="com.chinamobile.cloudapp:id/sign_button").click()
    sleep(2)
    if(d(text=u"未签到").exists):
        d(resourceId="headerUpP").click()
        sleep(2)
        assert d(text=u"已签到").exists == True
    else:
        d.press("back")

    sleep(5)
    # 停止app
    d.app_stop("com.chinamobile.cloudapp")


if __name__ == "__main__":
    pytest.main()

