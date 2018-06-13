#coding=utf-8
import uiautomator2 as u2
from time import sleep
from po import ExcuteCase as E, proxy
import pytest
import allure


@E.E
@allure.step("热点--视频彩铃")
def test_cailing():
    str = proxy.url
    d = u2.connect(str)

    # 启动App
    d.app_start("com.chinamobile.cloudapp")
    # 切换到爱看
    d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_4").click()
    #进入彩铃
    d(text=u"视频彩铃").click()
    sleep(2)
    assert d(text=u"VoLTE视频彩铃").exists==True
    sleep(6)
    #首页banner
    d(resourceId="com.chinamobile.cloudapp:id/image").click(timeout=15.0)
    sleep(3)
    if (d(text=u"寻找萌王").exists):
        d.press("back")
    elif (d(text=u"	萌翻6月，寻找萌王").exists):
        d.press("back")
    else:
        d(resourceId="com.chinamobile.cloudapp:id/iv_callshow_dianzan").click()
        sleep(2)
        d(resourceId="com.chinamobile.cloudapp:id/iv_callshow_set").click()
        sleep(2)
        d(resourceId="com.chinamobile.cloudapp:id/iv_callshow_share").click()
        sleep(2)
        d.press("back")
        sleep(2)
        d.press("back")

    sleep(2)
    assert d(text=u"VoLTE视频彩铃").exists == True



    #彩铃小常识
    d(text=u"视频彩铃小常识 >").click()
    sleep(3)
    assert d(text=u"小常识").exists
    sleep(2)
    d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
    sleep(2)
    d.press("back")


    #环球掠影
    d(resourceId="com.chinamobile.cloudapp:id/image", className="android.widget.ImageView", instance=1).click()
    sleep(2)
    assert d(resourceId="com.chinamobile.cloudapp:id/iv_phone_center").exists ==True
    d.press("back")

    #滑动到底端
    sleep(2)
    for i in range(4):
        d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
        sleep(2)

    # 切换到呼叫
    d(resourceId="com.chinamobile.cloudapp:id/callshow_bottom_home_tab_2").click()
    sleep(5)
    assert d(text=u"拔号键盘").exists == True
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
    assert d(text=u"通讯录").exists == True
    sleep(1)
    d(resourceId="com.chinamobile.cloudapp:id/tv_recent_calls").click()
    sleep(2)
    assert d(text=u"最近通话").exists == True

    #广场
    d(resourceId="com.chinamobile.cloudapp:id/callshow_bottom_home_tab_3").click()
    sleep(5)
    assert d(text=u"最新").exists == True
    sleep(2)
    d(text=u"最热").click()
    sleep(2)
    d(text=u"最萌").click()
    sleep(2)

    #我的
    d(resourceId="com.chinamobile.cloudapp:id/callshow_bottom_home_tab_4").click()
    sleep(2)
    assert d(text=u"我的会员").exists
    sleep(2)
    #检查视频彩铃状态
    if (d(text=u"已开通").exists):
        pass
    else:
        d(resourceId="com.chinamobile.cloudapp:id/tv_ordered").click()
        sleep(2)
        d.press("back")

    #彩铃设置
    d(resourceId="com.chinamobile.cloudapp:id/rl_my_setting").click()
    sleep(2)
    assert d(text=u"当前设置的彩铃").exists
    d.press("back")
    sleep(2)

    #我的DIY
    if (d(text=u"已开通").exists):
        d(resourceId="com.chinamobile.cloudapp:id/rl_my_diy").click()
        sleep(2)
        assert d(text=u"我上传的视频彩铃").exists == True
        d(resourceId="com.chinamobile.cloudapp:id/toset").click(timeout=10)
        sleep(2)
        d.press("back")

    else:
        d(resourceId="com.chinamobile.cloudapp:id/rl_my_diy").click()
        sleep(2)
        d.press("back")
    sleep(5)

    #我的点赞
    d(text=u"我的点赞").click()
    sleep(2)
    assert d(text=u"我的点赞").exists == True
    d(resourceId="com.chinamobile.cloudapp:id/home_cloud_title_left_return").click()
    sleep(2)

    #用户反馈
    d(resourceId="com.chinamobile.cloudapp:id/rl_feed").click()
    sleep(2)
    assert d(text=u"意见反馈").exists==True
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/home_cloud_title_left_return").click()
    sleep(2)

    #系统设置
    d(resourceId="com.chinamobile.cloudapp:id/rl_system_setting").click()
    sleep(2)
    assert d(text=u"设置").exists == True
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


if __name__=="__main__":
    test_cailing()
    # pytest.main("test_007_cailing.py")

