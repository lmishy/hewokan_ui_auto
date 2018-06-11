#coding=utf-8
import uiautomator2 as u2
from time import sleep
from po import proxy,ExcuteCase as E
import pytest
import allure


@E.E
@allure.step("热点--喜欢--尝鲜")
def hot_xihuan_cangxian():
    str = proxy.url
    d = u2.connect(str)

    # 启动App
    d.app_start("com.chinamobile.cloudapp")

    # 向上滑动
    sleep(5)
    for i in range(3):
        d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
        sleep(1)
    # 选择一个节目
    d(resourceId="com.chinamobile.cloudapp:id/image", className="android.widget.ImageView", instance=2).click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/videoPauseImg").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/video_collect_icon").click()
    sleep(2)
    d.press("back")
    sleep(2)

    #猜你喜欢
    d(text=u"换一换").click()
    sleep(2)
    d(text=u"更多精彩").click()
    sleep(2)
    d(text=u"内地").click()
    sleep(2)
    d(text=u"美国").click()
    sleep(2)
    d(text=u"韩国").click()
    sleep(2)
    d(text=u"韩国").click()
    sleep(2)
    d(text=u"剧情").click()
    sleep(2)
    d(text=u"爱情").click()
    sleep(2)
    d(text=u"喜剧").click()
    sleep(2)
    d(text=u"动作").click()
    sleep(2)
    d(text=u"VIP").click()
    sleep(2)
    d.press("back")

    #热点尝鲜
    sleep(2)
    for i in range(2):
        d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
        sleep(1)
    d(resourceId="com.chinamobile.cloudapp:id/image", className="android.widget.ImageView", instance=4).click()
    sleep(2)
    d.press("back")
    sleep(2)
    d(text=u"换一换").click()
    sleep(2)
    d(text=u"更多精彩").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/image_mid").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/video_collect_icon").click()
    sleep(2)
    d.press("back")
    sleep(5)
    # 停止app
    d.app_stop("com.chinamobile.cloudapp")


def test_hot_xihuan_cangxian():
    hot_xihuan_cangxian()

if __name__=="__main__":
    # str = proxy.url
    # hot_xihuan_cangxian(str)
    pytest.main()

