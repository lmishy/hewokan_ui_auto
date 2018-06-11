#coding=utf-8
import uiautomator2 as u2
from time import sleep
from po import proxy,ExcuteCase as E
import pytest
import allure

@E.E
@allure.step('直播页面')
def zhibo():
    str = proxy.url
    d = u2.connect(str)

    # 启动App
    d.app_start("com.chinamobile.cloudapp1")

    # 切换直播tab
    d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_2").click()
    sleep(2)
    d(text=u"本地").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/image_mid").click()
    sleep(2)
    d.press("back")
    sleep(2)
    d(text=u"电视").click()
    sleep(2)
    d(text=u"主播").click()
    sleep(2)
    d(className="com.tencent.tbs.core.webkit.WebView").click()
    sleep(2)
    d(text=u"演唱会").click()
    sleep(2)
    d(className="com.tencent.tbs.core.webkit.WebView").click()
    sleep(2)

    sleep(5)
    # 停止app
    d.app_stop("com.chinamobile.cloudapp")


def test_zhibo():
    zhibo()

if __name__=="__main__":
    # str = proxy.url
    # zhibo(str)
    pytest.main()

