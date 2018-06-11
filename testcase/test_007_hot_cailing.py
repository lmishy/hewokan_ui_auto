#coding=utf-8
import uiautomator2 as u2
from time import sleep
from po import ExcuteCase as E, proxy
import pytest
import allure


@E.E
@allure.step("热点--视频彩铃")
def hot_cailing():
    str = proxy.url
    d = u2.connect(str)

    # 启动App
    d.app_start("com.chinamobile.cloudapp")

    d(resourceId="com.chinamobile.cloudapp:id/image_mid").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/image").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/iv_callshow_dianzan").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/iv_callshow_set").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/negativeButton").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/iv_callshow_share").click()
    sleep(2)
    d.press("back")
    sleep(2)
    d.press("back")


    #环球掠影
    d(resourceId="com.chinamobile.cloudapp:id/image", className="android.widget.ImageView", instance=1).click()
    sleep(2)
    d.press("back")

    #滑动到底端
    sleep(2)
    for i in range(4):
        d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
        sleep(2)

    # 滑动到底端
    d(resourceId="com.chinamobile.cloudapp:id/callshow_bottom_home_tab_2").click()
    sleep(1)
    d(resourceId="com.chinamobile.cloudapp:id/imageButton_1").click()
    sleep(1)
    d(resourceId="com.chinamobile.cloudapp:id/imageButton_8").click()
    sleep(1)
    d(resourceId="com.chinamobile.cloudapp:id/imageButton_4").click()
    sleep(1)
    d(resourceId="com.chinamobile.cloudapp:id/imageButton_2").click()
    sleep(1)
    d(resourceId="com.chinamobile.cloudapp:id/imageButton_8").click()
    sleep(1)
    d(resourceId="com.chinamobile.cloudapp:id/imageButton_0").click()
    sleep(1)
    d(resourceId="com.chinamobile.cloudapp:id/imageButton_2").click()
    sleep(1)
    d(resourceId="com.chinamobile.cloudapp:id/imageButton_7").click()
    sleep(1)
    d(resourceId="com.chinamobile.cloudapp:id/imageButton_8").click()
    sleep(1)
    d(resourceId="com.chinamobile.cloudapp:id/imageButton_0").click()
    sleep(1)
    d(resourceId="com.chinamobile.cloudapp:id/imageButton_1").click()
    sleep(1)
    d(resourceId="com.chinamobile.cloudapp:id/imageButton_call").click()
    sleep(1)
    d(resourceId="com.chinamobile.cloudapp:id/iv_phone_center").click()



    #切换通讯录
    d(resourceId="com.chinamobile.cloudapp:id/tv_address_book").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/tv_recent_calls").click()
    sleep(2)

    #广场
    d(resourceId="com.chinamobile.cloudapp:id/callshow_bottom_home_tab_3").click()
    sleep(2)
    d(text=u"最热").click()
    sleep(2)

    #我的
    d(resourceId="com.chinamobile.cloudapp:id/callshow_bottom_home_tab_4").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/rl_my_setting").click()
    sleep(2)
    d.press("back")
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/rl_my_diy").click()
    sleep(2)
    d.press("back")
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/rl_my_zan").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/home_cloud_title_left_return").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/rl_feed").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/home_cloud_title_left_return").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/rl_system_setting").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/checkBox0").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/checkBox0").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/checkBox1").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/checkBox1").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/rl_video_switch").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/rl_video_switch").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/home_cloud_title_left_return").click()
    sleep(2)
    d.press("back")
    sleep(5)
    # 停止app
    d.app_stop("com.chinamobile.cloudapp")

def test_hot_cailing():
    hot_cailing()

if __name__=="__main__":
    # str = proxy.url
    # hot_cailing(str)
    pytest.main()

