#coding=utf-8
import uiautomator2 as u2
from time import sleep
from po import proxy
import pytest
import allure

class Test_aikan1():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        sleep(5)
        self.d.app_stop("com.chinamobile.cloudapp")

    @allure.step('爱看——彩铃')
    def test_aikan_cailing(self):
        # 切换爱看tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_4").click(timeout=20)
        sleep(2)
        assert self.d(text=u"视频彩铃").wait(exists=True,timeout=20)
        # 视频彩铃
        self.d(text=u"视频彩铃").click(timeout=20)
        sleep(5)
        assert self.d(text=u"VoLTE视频彩铃").wait(exists=True,timeout=20)
        self.d.press("back")
        sleep(2)

    @allure.step('爱看——学而思')
    def test_aikan_xueersi(self):
        # 切换爱看tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_4").click(timeout=20)
        sleep(2)
        # 学而思
        self.d(text=u"学而思").click(timeout=20)
        sleep(2)
        assert self.d(text=u"学而思").wait(exists=True,timeout=20)
        self.d.press("back")
        sleep(2)

    @allure.step('爱看——阿里体育')
    def test_aikan_alitiyu(self):
        # 切换爱看tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_4").click(timeout=20)
        sleep(2)
        # 阿里体育
        self.d(text=u"阿里体育").click(timeout=20)
        sleep(2)
        assert self.d(text=u"阿里体育").wait(exists=True,timeout=20)
        self.d.press("back")
        sleep(2)

    @allure.step('爱看——精品教育')
    def test_aikan_jiaoyu(self):
        # 切换爱看tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_4").click(timeout=20)
        sleep(2)
        # 精品教育
        self.d(text=u"精品教育").click(timeout=20)
        sleep(2)
        assert self.d(text=u"精品教育").wait(exists=True,timeout=20)
        self.d.press("back")
        sleep(2)
        # 换一换两次
        self.d(resourceId="com.chinamobile.cloudapp:id/more").click(timeout=20)
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/more").click(timeout=20)
        sleep(2)
        # 点击播放列表第一个
        self.d.click(0.5, 0.35)
        sleep(5)
        self.d.press("back")
        sleep(5)
        # 向上滑动窗口3次
        for i in range(3):
            self.d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
            sleep(1)




if __name__=="__main__":
    pytest.main("test_014_aikan_zhuye.py")

