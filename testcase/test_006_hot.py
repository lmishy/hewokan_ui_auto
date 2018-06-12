#coding=utf-8
import uiautomator2 as u2
from time import sleep
from po import ExcuteCase as E, proxy
import pytest
import allure

@E.E
@allure.step('热点页面--banner--导航')
def hot():
    str = proxy.url
    d = u2.connect(str)

    # 启动App
    d.app_start("com.chinamobile.cloudapp")

    # 热点banner
    d(resourceId="com.chinamobile.cloudapp:id/image").click()
    sleep(5)
    assert d(resourceId="com.chinamobile.cloudapp:id/video_back").exists == True
    d.press("back")

    #热门榜单
    d(text=u"热门榜单").click()
    sleep(2)
    assert d(text=u"电影").exists ==True
    sleep(2)
    d(text=u"电视剧").click()
    sleep(2)
    d(text=u"综艺").click()
    sleep(2)
    d(text=u"动漫").click()
    sleep(2)
    d.press("back")

    # 热门榜单
    d(text=u"精彩专题").click()
    sleep(2)
    assert d(text=u"精选专题").exists ==True
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/image_mid").click()
    sleep(2)
    assert d(resourceId="com.chinamobile.cloudapp:id/iv_coll").exists == True
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/iv_coll").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/iv_share").click()
    sleep(2)
    d.press("back")
    sleep(2)
    d.press("back")
    sleep(2)
    d.press("back")

    #签到有礼
    d(text=u"签到有礼").click()
    sleep(2)
    if (d(description = u"未签到").exists):
        d(resourceId="headerUpP").click()
    else:
        pass
    sleep(2)
    d.press("back")

    #福利社区
    d(text=u"福利社区").click()
    sleep(2)
    d.press("back")
    sleep(5)
    # 停止app
    d.app_stop("com.chinamobile.cloudapp")


def test_hot():
    hot()

if __name__=="__main__":
    # str = proxy.url
    # hot()
    pytest.main()

