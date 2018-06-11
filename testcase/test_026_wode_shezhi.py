#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/8
import uiautomator2 as u2
from time import sleep
from po import proxy,ExcuteCase as E
import pytest
import allure

@E.E
@allure.step('我的--设置')
def wode_shezhi():
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
    d(text=u"设置").click()
    sleep(2)
    #修改密码
    d(resourceId="com.chinamobile.cloudapp:id/layout_change_psd").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/et_old_pwd").set_text("12346")
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/et_new_pwd1").set_text("123456")
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/et_new_pwd2").set_text("123456")
    sleep(2)
    d.press("back")
    sleep(2)
    d.press("back")
    sleep(2)
    #开启2G/3G/4G网络自动播放
    d(resourceId="com.chinamobile.cloudapp:id/checkBox").click()
    sleep(2)
    #关闭2G/3G/4G网络自动播放
    d(resourceId="com.chinamobile.cloudapp:id/checkBox").click()
    sleep(2)
    #清理缓存
    d(resourceId="com.chinamobile.cloudapp:id/rl_clear_cache").click()
    sleep(2)
    d.press("back")
    sleep(5)
    # 停止app
    d.app_stop("com.chinamobile.cloudapp")

def test_shezhi():
    wode_shezhi()


if __name__ == "__main__":
    # str = proxy.url
    # wode_shezhi(str)
    pytest.main()

