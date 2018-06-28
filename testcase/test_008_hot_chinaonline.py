#coding=utf-8
import uiautomator2 as u2
from time import sleep
from po import ExcuteCase as E, proxy
import pytest
import allure


class Test_chinaplus():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        self.d.app_stop("com.chinamobile.cloudapp")

    @allure.step("热点--一带一路")
    def test_yidaiyilu(self):

        # 一带一路文化长廊
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/txt1").click()
        sleep(2)
        if (self.d(text=u"一带一路文化长廊").exists):
            assert self.d(text=u"一带一路文化长廊").exists == True
            # banner
            self.d(resourceId="com.chinamobile.cloudapp:id/image").click()
            sleep(5)
            self.d.press("back")
            sleep(2)
            # 列表内容
            self.d(resourceId="com.chinamobile.cloudapp:id/image_mid").click()
            sleep(2)
            if (self.d(resourceId="com.chinamobile.cloudapp:id/videoPauseImg").exists):
                self.d(resourceId="com.chinamobile.cloudapp:id/videoPauseImg").click()
            else:
                pass
            sleep(5)
            self.d.press("back")
            self.d.press("back")

        else:
            self.d.press("back")
            # raise Exception(u"用例异常！")
        sleep(2)

    @allure.step("热点--radio")
    def test_radio(self):
        self.d(resourceId="com.chinamobile.cloudapp:id/pic2").click()
        sleep(5)
        assert self.d(text=u"首页").exists == True
        sleep(2)
        self.d(text=u"首页").click()
        sleep(2)
        self.d(text=u"收音机").click()
        sleep(5)
        self.d(text=u"推荐栏目").wait(timeout=10)
        assert self.d(text=u"推荐栏目").exists == True
        sleep(2)
        self.d(text=u"分类").click()
        sleep(5)
        self.d(text=u"新闻").wait(timeout=10)
        assert self.d(text=u"新闻").exists == True
        sleep(2)
        self.d(text=u"专题").click()
        sleep(5)
        self.d(text=u"排行榜").click()
        sleep(5)
        self.d(text=u"节目榜单").wait(timeout=10)
        assert self.d(text=u"节目榜单").exists == True
        sleep(2)
        self.d.press("back")

    @allure.step("热点--Cinitalia")
    def test_Cinitalia(self):
        # Cinitalia
        self.d(resourceId="com.chinamobile.cloudapp:id/pic3").click()
        sleep(5)
        self.d(text=u"Cinitalia").wait(timeout=10)
        assert self.d(text=u"Cinitalia").exists == True
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/image").click()
        sleep(5)
        for i in range(3):
            self.d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
            sleep(1)
        self.d.press("back")
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/image_mid").click()
        sleep(5)
        for i in range(3):
            self.d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
            sleep(1)
        self.d.press("back")
        self.d.press("back")

    @allure.step("gengduo")
    def test_more(self):
        self.d(resourceId="com.chinamobile.cloudapp:id/txt4").click()
        sleep(1)
        self.d.press("back")



if __name__=="__main__":
    pytest.main("test_008_hot_chinaonline.py")

