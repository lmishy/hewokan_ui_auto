#coding=utf-8
import uiautomator2 as u2
from time import sleep
from po import proxy
import pytest
import allure


class Test_chinaplus():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        sleep(5)
        self.d.app_stop("com.chinamobile.cloudapp")


    @allure.step("热点--一带一路")
    def test_yidaiyilu(self):

        # 一带一路文化长廊
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/pic1").click(timeout=20)
        sleep(2)
        if (self.d(text=u"一带一路文化长廊").exists):
            assert self.d(text=u"一带一路文化长廊").wait(exists=True,timeout=20)
            # banner
            self.d(resourceId="com.chinamobile.cloudapp:id/image").click(timeout=20)
            sleep(5)
            self.d.press("back")
            sleep(2)
            # 列表内容
            self.d(resourceId="com.chinamobile.cloudapp:id/image_mid").click(timeout=20)
            sleep(2)
            if (self.d(resourceId="com.chinamobile.cloudapp:id/videoPauseImg").exists):
                self.d(resourceId="com.chinamobile.cloudapp:id/videoPauseImg").click(timeout=20)
            else:
                pass
            sleep(5)
            self.d.press("back")
            self.d.press("back")

        else:
            self.d.press("back")
            # raise Exception(u"用例异常！")
        sleep(5)

    @allure.step("热点--ChinaRadio")
    def test_radio(self):
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/pic2").click(timeout=20)
        sleep(5)
        assert self.d(text=u"首页").wait(exists=True,timeout=20)
        sleep(2)
        self.d(text=u"首页").click()
        sleep(2)
        self.d(text=u"收音机").click()
        sleep(5)
        self.d(text=u"分类").click()
        sleep(5)
        self.d(text=u"专题").wait(timeout=10)
        assert self.d(text=u"专题").wait(exists=True,timeout=20)
        self.d(text=u"排行榜").click()
        sleep(5)
        assert self.d(text=u"排行榜").wait(exists=True, timeout=20)
        self.d.press("back")
        sleep(5)


    @allure.step("热点--Cinitalia")
    def test_Cinitalia(self):
        # Cinitalia
        self.d(resourceId="com.chinamobile.cloudapp:id/pic3").click(timeout=20)
        sleep(5)
        self.d(text=u"Cinitalia").wait(timeout=10)
        assert self.d(text=u"Cinitalia").wait(exists=True,timeout=20)
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/image").click(timeout=20)
        sleep(5)
        for i in range(3):
            self.d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
            sleep(1)
        self.d.press("back")
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/image_mid").click(timeout=20)
        sleep(5)
        for i in range(3):
            self.d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
            sleep(1)
        self.d.press("back")
        self.d.press("back")
        sleep(5)


    @allure.step("更多")
    def test_more(self):
        self.d(resourceId="com.chinamobile.cloudapp:id/txt4").click(timeout=20)
        sleep(2)
        assert self.d(text=u"下载").wait(exists=True, timeout=20)
        self.d.press("back")
        sleep(5)



if __name__=="__main__":
    pytest.main("test_008_hot_chinaonline.py")

