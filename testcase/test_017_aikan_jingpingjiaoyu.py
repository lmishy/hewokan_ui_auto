#coding=utf-8
import uiautomator2 as u2
from time import sleep
from po import proxy
import pytest
import allure

class Test_aikan4():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        sleep(5)
        self.d.app_stop("com.chinamobile.cloudapp")

    @allure.step('爱看--精品教育--幼儿')
    def test_aikan_youer(self):
        # 切换爱看tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_4").click()
        sleep(3)
        # 精品教育
        self.d(text=u"精品教育").click()
        sleep(5)
        # 幼儿
        self.d(text=u"幼儿").click()
        assert self.d(text=u"幼儿").wait(exists=True,timeout=20)==True
        sleep(5)
        # 向上滑动三次次
        for i in range(3):
            self.d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
            sleep(1)

    @allure.step('爱看--精品教育--小学')
    def test_aikan_youer(self):
        # 切换爱看tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_4").click()
        sleep(3)
        # 精品教育
        self.d(text=u"精品教育").click()
        sleep(5)
        # 小学
        self.d(text=u"小学").click()
        assert self.d(text=u"小学").wait(exists=True,timeout=20)
        sleep(5)
        # 向上滑动三次次
        for i in range(3):
            self.d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
            sleep(1)

    @allure.step('爱看--精品教育--初中')
    def test_aikan_youer(self):
        # 切换爱看tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_4").click()
        sleep(3)
        # 精品教育
        self.d(text=u"精品教育").click()
        sleep(5)
        # 初中
        self.d(text=u"初中").click()
        assert self.d(text=u"初中").wait(exists=True,timeout=20)
        sleep(5)
        # 向上滑动三次次
        for i in range(3):
            self.d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
            sleep(1)

    @allure.step('爱看--精品教育--高中')
    def test_aikan_youer(self):
        # 切换爱看tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_4").click()
        sleep(3)
        # 精品教育
        self.d(text=u"精品教育").click()
        sleep(5)
        # 高中
        self.d(text=u"高中").click()
        assert self.d(text=u"高中")
        sleep(5)
        # 向上滑动三次次
        for i in range(3):
            self.d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
            sleep(1)

        self.d.press("back")



if __name__=="__main__":
    pytest.main("test_017_aikan_jingpingjiaoyu.py")

