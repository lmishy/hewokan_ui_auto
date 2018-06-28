#coding=utf-8
import uiautomator2 as u2
from time import sleep
from po import proxy
import pytest
import allure


class Test_cailing():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        self.d.app_stop("com.chinamobile.cloudapp")

    @allure.step("爱看--视频彩铃--banner")
    def test_cailing(self):

        # 切换到爱看
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_4").click()
        # 进入彩铃
        self.d(text=u"视频彩铃").click()
        sleep(2)
        assert self.d(text=u"VoLTE视频彩铃").exists == True
        sleep(6)
        # 首页banner
        self.d(resourceId="com.chinamobile.cloudapp:id/image").click(timeout=15.0)
        sleep(3)
        if (self.d(text=u"视频彩铃").exists):
            self.d.press("back")
        elif (self.d(text=u"视频彩铃流量福利社").exists):
            self.d.press("back")
        else:
            self.d(resourceId="com.chinamobile.cloudapp:id/iv_callshow_dianzan").click()
            sleep(2)
            self.d(resourceId="com.chinamobile.cloudapp:id/iv_callshow_set").click()
            sleep(2)
            self.d(resourceId="com.chinamobile.cloudapp:id/iv_callshow_share").click()
            sleep(2)
            self.d.press("back")
            sleep(2)
            self.d.press("back")
        sleep(2)
        assert self.d(text=u"VoLTE视频彩铃").exists == True

    @allure.step("首页--小常识")
    def test_cangshi(self):
        # 切换到爱看
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_4").click()
        # 进入彩铃
        self.d(text=u"视频彩铃").click()
        sleep(2)
        assert self.d(text=u"VoLTE视频彩铃").exists == True
        sleep(6)
        # 彩铃小常识
        self.d(text=u"视频彩铃小常识 >").click()
        sleep(3)
        assert self.d(text=u"小常识").exists
        sleep(2)
        self.d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
        sleep(2)
        self.d.press("back")

    @allure.step("首页--彩铃素材")
    def test_sucai(self):
        # 切换到爱看
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_4").click()
        # 进入彩铃
        self.d(text=u"视频彩铃").click()
        sleep(2)
        assert self.d(text=u"VoLTE视频彩铃").exists == True
        sleep(6)
        # 环球掠影
        self.d(resourceId="com.chinamobile.cloudapp:id/image", className="android.widget.ImageView", instance=1).click()
        sleep(2)
        assert self.d(resourceId="com.chinamobile.cloudapp:id/iv_phone_center").exists == True
        self.d.press("back")

        # 滑动到底端
        sleep(2)
        for i in range(4):
            self.d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
            sleep(2)

    @allure.step("拨号盘")
    def test_dail(self):
        # 切换到爱看
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_4").click()
        # 进入彩铃
        self.d(text=u"视频彩铃").click()
        sleep(2)
        assert self.d(text=u"VoLTE视频彩铃").exists == True
        sleep(6)
        # 切换到呼叫
        self.d(resourceId="com.chinamobile.cloudapp:id/callshow_bottom_home_tab_2").click()
        sleep(5)
        assert self.d(text=u"拔号键盘").exists == True
        sleep(1)
        self.d(resourceId="com.chinamobile.cloudapp:id/imageButton_1").click()
        sleep(1)
        self.d(resourceId="com.chinamobile.cloudapp:id/imageButton_8").click()
        sleep(1)
        self.d(resourceId="com.chinamobile.cloudapp:id/imageButton_4").click()
        sleep(1)
        self.d(resourceId="com.chinamobile.cloudapp:id/imageButton_2").click()
        sleep(1)
        self.d(resourceId="com.chinamobile.cloudapp:id/imageButton_8").click()
        sleep(1)
        self.d(resourceId="com.chinamobile.cloudapp:id/imageButton_0").click()
        sleep(1)
        self.d(resourceId="com.chinamobile.cloudapp:id/imageButton_2").click()
        sleep(1)
        self.d(resourceId="com.chinamobile.cloudapp:id/imageButton_7").click()
        sleep(1)
        self.d(resourceId="com.chinamobile.cloudapp:id/imageButton_8").click()
        sleep(1)
        self.d(resourceId="com.chinamobile.cloudapp:id/imageButton_0").click()
        sleep(1)
        self.d(resourceId="com.chinamobile.cloudapp:id/imageButton_1").click()
        sleep(1)
        self.d(resourceId="com.chinamobile.cloudapp:id/imageButton_call").click()
        sleep(3)
        self.d(resourceId="com.chinamobile.cloudapp:id/iv_phone_center").click()

    @allure.step("通讯录")
    def test_tongxunlu(self):
        # 切换到爱看
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_4").click()
        # 进入彩铃
        self.d(text=u"视频彩铃").click()
        sleep(2)
        assert self.d(text=u"VoLTE视频彩铃").exists == True
        sleep(6)
        # 切换通讯录
        self.d(resourceId="com.chinamobile.cloudapp:id/tv_address_book").click()
        sleep(2)
        assert self.d(text=u"通讯录").exists == True
        sleep(1)
        self.d(resourceId="com.chinamobile.cloudapp:id/tv_recent_calls").click()
        sleep(2)
        assert self.d(text=u"最近通话").exists == True

    @allure.step("广场")
    def test_guangchang(self):
        # 切换到爱看
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_4").click()
        # 进入彩铃
        self.d(text=u"视频彩铃").click()
        sleep(2)
        assert self.d(text=u"VoLTE视频彩铃").exists == True
        sleep(6)
        # 广场
        self.d(resourceId="com.chinamobile.cloudapp:id/callshow_bottom_home_tab_3").click()
        sleep(5)
        assert self.d(text=u"最新").exists == True
        sleep(2)
        self.d(text=u"最热").click()
        sleep(2)
        # self.d(text=u"最萌").click()
        # sleep(2)

    @allure.step("我的")
    def test_wode(self):
        # 切换到爱看
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_4").click()
        # 进入彩铃
        self.d(text=u"视频彩铃").click()
        sleep(2)
        assert self.d(text=u"VoLTE视频彩铃").exists == True
        sleep(6)
        # 我的
        self.d(resourceId="com.chinamobile.cloudapp:id/callshow_bottom_home_tab_4").click()
        sleep(2)
        assert self.d(text=u"我的会员").exists
        sleep(2)
        # 检查视频彩铃状态
        if (self.d(text=u"已开通").exists):
            pass
        else:
            self.d(resourceId="com.chinamobile.cloudapp:id/tv_ordered").click()
            sleep(2)
            self.d.press("back")

        # 彩铃设置
        self.d(resourceId="com.chinamobile.cloudapp:id/rl_my_setting").click()
        sleep(2)
        assert self.d(text=u"当前设置的彩铃").exists
        self.d.press("back")
        sleep(2)

        # 我的DIY
        if (self.d(text=u"已开通").exists):
            self.d(resourceId="com.chinamobile.cloudapp:id/rl_my_diy").click()
            sleep(2)
            assert self.d(text=u"我上传的视频彩铃").exists == True
            self.d(resourceId="com.chinamobile.cloudapp:id/toset").click(timeout=10)
            sleep(2)
            self.d.press("back")

        else:
            self.d(resourceId="com.chinamobile.cloudapp:id/rl_my_diy").click()
            sleep(2)
            self.d.press("back")
        sleep(5)
        self.d.press("back")

        # 我的点赞
        self.d(text=u"我的点赞").click()
        sleep(2)
        assert self.d(text=u"我的点赞").exists == True
        self.d(resourceId="com.chinamobile.cloudapp:id/home_cloud_title_left_return").click()
        sleep(2)

        # 用户反馈
        self.d(resourceId="com.chinamobile.cloudapp:id/rl_feed").click()
        sleep(2)
        assert self.d(text=u"意见反馈").exists == True
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/home_cloud_title_left_return").click()
        sleep(2)

        # 系统设置
        self.d(resourceId="com.chinamobile.cloudapp:id/rl_system_setting").click()
        sleep(2)
        assert self.d(text=u"设置").exists == True
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/checkBox0").click()
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/checkBox0").click()
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/checkBox1").click()
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/checkBox1").click()
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/rl_video_switch").click()
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/rl_video_switch").click()
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/home_cloud_title_left_return").click()
        sleep(2)
        self.d.press("back")
        sleep(5)




if __name__=="__main__":
    pytest.main("test_007_cailing.py")

