#coding=utf-8
import uiautomator2 as u2
from time import sleep
from po import ExcuteCase as E, proxy
import pytest
import allure


@E.E
@allure.step('第三方登录')
def login_thd():
    str = proxy.url
    d = u2.connect(str)

    # 启动App
    d.app_start("com.chinamobile.cloudapp")

    # 我的
    d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()

    d(resourceId="com.chinamobile.cloudapp:id/head_pic").click()

    # 微信
    d(text=u"微信账号登录").click()
    sleep(5)
    d.press("back")
    #d.press("back")

    # 新浪
    sleep(2)
    d(text=u"微博账号登录").click()
    sleep(10)
    #d.press("back")
    #sleep(2)
    d.press("back")

    # QQ账号登录
    sleep(2)
    d(text=u"QQ账号登录").click()
    sleep(2)
    d.press("back")

    assert d(resourceId="com.chinamobile.cloudapp:id/home_cloud_title").get_text=="登录和我看"

    sleep(3)
    # 停止app
    d.app_stop("com.chinamobile.cloudapp")

def test_login_thd():
    login_thd()

if __name__=="__main__":
    #str = proxy.url
    #test_login_thd(str)
    pytest.main()

