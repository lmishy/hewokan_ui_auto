#coding=utf-8
import uiautomator2 as u2
from time import sleep
from po import proxy,ExcuteCase as E
import pytest
import allure

@E.E
@allure.step('直播页面')
def test_zhibo():
    str = proxy.url
    d = u2.connect(str)

    # 启动App
    d.app_start("com.chinamobile.cloudapp1")

    # 切换直播tab
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_2").click()
    sleep(2)
    assert d(text=u"本地").exists ==True
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
    d(description=u"我的关注").click()
    sleep(2)
    d(text=u"演唱会").click()
    sleep(2)
    d(description=u"往期回看").click()
    sleep(2)

    sleep(5)
    # 停止app
    d.app_stop("com.chinamobile.cloudapp")



if __name__=="__main__":
    # test_zhibo()
    pytest.main()

