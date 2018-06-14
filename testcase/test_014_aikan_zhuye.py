#coding=utf-8
import uiautomator2 as u2
from time import sleep
from po import proxy,ExcuteCase as E
import pytest
import allure

@E.E
@allure.step('爱看——主页')
def test_aikan_zhuye():
    str = proxy.url
    #连接手机
    d = u2.connect(str)

    # 启动App
    d.app_start("com.chinamobile.cloudapp")

    #切换爱看tab
    d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_4").click()
    sleep(2)
    assert d(text=u"视频彩铃").exists == True
    #视频彩铃
    d(text=u"视频彩铃").click()
    sleep(5)
    assert d(text=u"VoLTE视频彩铃").exists == True
    d.press("back")
    sleep(2)
    #学而思
    d(text=u"学而思").click()
    sleep(2)
    assert d(text=u"学而思").exists == True
    d.press("back")
    sleep(2)
    #阿里体育
    d(text=u"阿里体育").click()
    sleep(2)
    assert d(text=u"阿里体育").exists == True
    d.press("back")
    sleep(2)
    #精品教育
    d(text=u"精品教育").click()
    sleep(2)
    assert d(text=u"精品教育").exists == True
    d.press("back")
    sleep(2)
    #换一换两次
    d(resourceId="com.chinamobile.cloudapp:id/more").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/more").click()
    sleep(2)
    #点击播放列表第一个
    d.click(0.5, 0.35)
    sleep(5)
    d.press("back")
    sleep(5)
    #向上滑动窗口3次
    for i in range(3):
        d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
        sleep(1)

    sleep(5)
    # 停止app
    d.app_stop("com.chinamobile.cloudapp")


if __name__=="__main__":
    pytest.main()

