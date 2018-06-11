#coding=utf-8
import uiautomator2 as u2
from time import sleep
from po import proxy,ExcuteCase as E
import pytest
import allure

@E.E
@allure.step('爱看--学而思')
def aikan_xueersi():
    str = proxy.url
    #连接手机
    d = u2.connect(str)

    # 启动App
    d.app_start("com.chinamobile.cloudapp")

    #切换爱看tab
    d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_4").click()
    sleep(2)
    #学而思
    d(text=u"学而思").click()
    sleep(2)
    #播放节目
    d(resourceId="com.chinamobile.cloudapp:id/image_mid").click()
    sleep(5)
    #收藏
    d(resourceId="com.chinamobile.cloudapp:id/video_collect_icon").click()
    sleep(2)
    #选集
    d(resourceId="com.chinamobile.cloudapp:id/video_episode_update").click()
    sleep(5)
    d(resourceId="com.chinamobile.cloudapp:id/episode_select_txt", text=u"15").click()
    sleep(5)
    d.press("back")
    sleep(5)
    # 停止app
    d.app_stop("com.chinamobile.cloudapp")

def test_aikan_xueersi():
    aikan_xueersi()

if __name__=="__main__":
    # str = proxy.url
    # aikan_xueersi(str)
    pytest.main()

