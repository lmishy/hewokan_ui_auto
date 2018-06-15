#coding=utf-8
import uiautomator2 as u2
from time import sleep
from po import proxy,ExcuteCase as E
import pytest
import allure

@E.E
@allure.step('爱看--精品教育')
def test_aikan_jingpinjiaoyu():
    str = proxy.url
    #连接手机
    d = u2.connect(str)

    # 启动App
    d.app_start("com.chinamobile.cloudapp")

    #切换爱看tab
    d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_4").click()
    sleep(3)
    #精品教育
    d(text=u"精品教育").click()
    sleep(5)

    #幼儿
    d(text=u"幼儿").click()
    sleep(5)
    #向上滑动三次次
    for i in range(3):
        d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
        sleep(1)

     #小学
    d(text=u"小学").click()
    sleep(5)
    #向上滑动三次次
    for i in range(3):
        d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
        sleep(1)

    #初中
    d(text=u"初中").click()
    sleep(5)
    #向上滑动三次次
    for i in range(3):
        d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
        sleep(1)

    #高中
    d(text=u"高中").click()
    sleep(5)
    #向上滑动三次次
    for i in range(3):
        d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
        sleep(1)

    d.press("back")
    
    sleep(5)
    # 停止app
    d.app_stop("com.chinamobile.cloudapp")


if __name__=="__main__":
    test_aikan_jingpinjiaoyu()
    # pytest.main()

