#coding=utf-8
import uiautomator2 as u2
from time import sleep
from po import proxy
import pytest
import allure

class Test_aikan2():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        sleep(5)
        self.d.app_stop("com.chinamobile.cloudapp")

    @allure.step('爱看--学而思')
    def test_aikan_xueersi(self):
        # 切换爱看tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_4").click(timeout=20)
        sleep(2)
        # 学而思
        self.d(text=u"学而思").click(timeout=20)
        sleep(5)
        assert self.d(text=u"学而思").wait(exists=True,timeout=20)
        # 播放节目
        self.d(resourceId="com.chinamobile.cloudapp:id/image").click(timeout=20)
        sleep(5)
        # 收藏
        self.d(resourceId="com.chinamobile.cloudapp:id/video_collect_icon").click(timeout=20)
        sleep(2)
        # 选集
        self.d(resourceId="com.chinamobile.cloudapp:id/video_episode_update").click(timeout=20)
        sleep(5)
        self.d(resourceId="com.chinamobile.cloudapp:id/episode_select_txt", text=u"15").click(timeout=20)
        sleep(5)
        self.d.press("back")





if __name__=="__main__":
    pytest.main("test_015_aikan_xueersi.py")

