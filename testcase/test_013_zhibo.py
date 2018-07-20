#coding=utf-8
import uiautomator2 as u2
from time import sleep
from po import proxy
import pytest
import allure

class Test_zhibo():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        sleep(5)
        self.d.app_stop("com.chinamobile.cloudapp")

    @allure.step('直播页面')
    def test_zhibo(self):
        # 切换直播tab
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_2").click()
        sleep(5)
        assert self.d(text=u"本地").exists 
        sleep(2)
        self.d(text=u"本地").click()
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/image_mid").click()
        sleep(2)
        self.d.press("back")
        sleep(2)
        self.d(text=u"电视").click()
        sleep(2)
        self.d(text=u"主播").click()
        sleep(2)
        self.d(description=u"我的关注").click()
        sleep(2)
        self.d(text=u"演唱会").click()
        sleep(2)
        self.d(description=u"往期回看").click()
        sleep(2)



if __name__=="__main__":
    pytest.main("test_013_zhibo.py")

