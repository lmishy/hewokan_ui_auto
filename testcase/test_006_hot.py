#coding=utf-8
import uiautomator2 as u2
from time import sleep
from po import  proxy
import pytest
import allure

class Test_hot():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        sleep(5)
        self.d.app_stop("com.chinamobile.cloudapp")

    @allure.step('热点页面--banner')
    def test_banner(self):
        # 热点banner
        self.d(resourceId="com.chinamobile.cloudapp:id/image").click(timeout=20)
        sleep(5)
        if (self.d(resourceId="com.chinamobile.cloudapp:id/home_cloud_title_left_return").exists):
            self.d.press("back")
        else:
            assert self.d(resourceId="com.chinamobile.cloudapp:id/video_back").wait(exists=True,timeout=20)
            self.d.press("back")

    @allure.step('热点页面--热门榜单')
    def test_bandan(self):
        # 热门榜单
        self.d(text=u"热门榜单").click(timeout=20)
        sleep(2)
        assert self.d(text=u"电影").wait(exists=True,timeout=20)
        sleep(2)
        self.d(text=u"电视剧").click(timeout=20)
        sleep(2)
        self.d(text=u"动漫").click(timeout=20)
        sleep(2)
        self.d.press("back")

    @allure.step('热点页面--签到')
    def test_qiandao(self):
        # 签到有礼
        self.d(text=u"每日签到").click(timeout=20)
        sleep(2)
        if (self.d(description=u"未签到").exists):
            self.d(resourceId="headerUpP").click()
            sleep(5)
            assert self.d(description=u"已签到").exists
        else:
            pass
        sleep(5)
        self.d.press("back")

        '''
        #福利社区
        self.d(text=u"福利社区").click()
        sleep(2)
        d.press("back")
        '''



if __name__=="__main__":
    pytest.main("test_006_hot.py")

