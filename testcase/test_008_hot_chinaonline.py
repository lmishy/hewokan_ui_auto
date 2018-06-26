#coding=utf-8
import uiautomator2 as u2
from time import sleep
from po import ExcuteCase as E, proxy
import pytest
import allure


@E.E
@allure.step("热点--ChinaOnline")
def test_hot_chinaonline():
    str = proxy.url
    d = u2.connect(str)

    # 启动App
    d.app_start("com.chinamobile.cloudapp")

    # 一带一路文化长廊
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/txt1").click()
    sleep(2)
    if (d(text=u"一带一路文化长廊").exists):
        assert d(text=u"一带一路文化长廊").exists == True
        # banner
        d(resourceId="com.chinamobile.cloudapp:id/image").click()
        sleep(5)
        d.press("back")
        sleep(2)
        # 列表内容
        d(resourceId="com.chinamobile.cloudapp:id/image_mid").click()
        sleep(2)
        if(d(resourceId="com.chinamobile.cloudapp:id/videoPauseImg").exists):
            d(resourceId="com.chinamobile.cloudapp:id/videoPauseImg").click()
        else:
            pass
        sleep(5)
        d.press("back")
        d.press("back")

    else:
        d.press("back")
        # raise Exception(u"用例异常！")
    sleep(2)



    #ChinaRadio
    d(resourceId="com.chinamobile.cloudapp:id/pic2").click()
    sleep(5)
    assert d(text=u"首页").exists == True
    sleep(2)
    d(text=u"首页").click()
    sleep(2)
    d(text=u"收音机").click()
    sleep(5)
    d(text=u"推荐栏目").wait(timeout=10)
    assert d(text=u"推荐栏目").exists == True
    sleep(2)
    d(text=u"分类").click()
    sleep(5)
    d(text=u"新闻").wait(timeout=10)
    assert d(text=u"新闻").exists == True
    sleep(2)
    d(text=u"专题").click()
    sleep(5)
    d(text=u"排行榜").click()
    sleep(5)
    d(text=u"节目榜单").wait(timeout = 10)
    assert d(text=u"节目榜单").exists == True
    sleep(2)
    d.press("back")

    #Cinitalia
    d(resourceId="com.chinamobile.cloudapp:id/pic3").click()
    sleep(5)
    d(text=u"Cinitalia").wait(timeout=10)
    assert d(text=u"Cinitalia").exists == True
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/image").click()
    sleep(5)
    for i in range(3):
        d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
        sleep(1)
    d.press("back")
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/image_mid").click()
    sleep(5)
    for i in range(3):
        d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
        sleep(1)
    d.press("back")
    d.press("back")

    #更多
    d(resourceId="com.chinamobile.cloudapp:id/txt4").click()
    sleep(1)
    d.press("back")

    sleep(5)
    # 停止app
    d.app_stop("com.chinamobile.cloudapp")




if __name__=="__main__":
    test_hot_chinaonline()
    # pytest.main()

