#coding=utf-8
import uiautomator2 as u2
from time import sleep
from po import proxy
import pytest
import allure

class Test_xihuan_cangxian():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        self.d.app_stop("com.chinamobile.cloudapp")

    @allure.step("热点--喜欢")
    def test_hot_xihuan(self):
        # 向上滑动
        sleep(5)
        for i in range(3):
            self.d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
            sleep(1)
        # 选择一个节目
        self.d(resourceId="com.chinamobile.cloudapp:id/image", className="android.widget.ImageView", instance=2).click()
        sleep(5)
        if (self.d(resourceId="com.chinamobile.cloudapp:id/videoPauseImg").exists):
            self.d(resourceId="com.chinamobile.cloudapp:id/videoPauseImg").click()
        else:
            pass
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/video_collect_icon").click()
        sleep(2)
        self.d.press("back")
        sleep(2)

    @allure.step("热点--热点尝鲜")
    def test_hot_cangxian(self):
        # 向上滑动
        sleep(5)
        for i in range(3):
            self.d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
            sleep(1)
        # 热点尝鲜
        self.d(resourceId="com.chinamobile.cloudapp:id/image", className="android.widget.ImageView", instance=4).click()
        sleep(5)
        self.d.press("back")
        sleep(3)
        self.d(text=u"换一换").click()
        sleep(2)

        # 猜你喜欢
        for i in range(2):
            self.d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
            sleep(1)
        self.d(text=u"换一换").click()
        sleep(2)
        self.d(text=u"更多精彩").click()
        sleep(5)
        assert self.d(text=u"电影").exists == True
        sleep(2)
        self.d(text=u"内地").click()
        sleep(2)
        self.d(text=u"美国").click()
        sleep(2)
        self.d(text=u"韩国").click()
        sleep(2)
        self.d(text=u"韩国").click()
        sleep(2)
        self.d(text=u"剧情").click()
        sleep(2)
        self.d(text=u"爱情").click()
        sleep(2)
        self.d(text=u"喜剧").click()
        sleep(2)
        self.d(text=u"动作").click()
        sleep(2)
        self.d(text=u"VIP").click()
        sleep(2)
        self.d.press("back")
        sleep(5)





if __name__=="__main__":
    pytest.main("test_009_hot_xihuan_cangxian.py")

