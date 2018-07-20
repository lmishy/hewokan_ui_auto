#coding=utf-8
import uiautomator2 as u2
from time import sleep
from po import ExcuteCase as E, proxy
import pytest
import allure


class Test_login_thd():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        sleep(5)
        self.d.app_stop("com.chinamobile.cloudapp")

    @allure.step('微信登录')
    def test_login_wechat(self):

        # 我的
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/head_pic").click()
        sleep(2)
        assert self.d(text=u"登录和我看").exists


        # 微信
        self.d(text=u"微信账号登录").click()
        sleep(5)
        if (self.d(text=u"登录微信").exists):
            assert self.d(text=u"登录微信").exists
            self.d.press("back")
            self.d.press("back")
            sleep(2)
        else:
            assert self.d(text=u"登录和我看").exists
            pass

    @allure.step('微博登录')
    def test_login_weibo(self):

        # 我的
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/head_pic").click()
        sleep(5)
        assert self.d(text=u"登录和我看").exists

        # 新浪
        sleep(2)
        self.d(text=u"微博账号登录").click()
        sleep(10)
        if (self.d(resourceId="com.sina.weibo:id/ivUserPic").exists):
            assert self.d(resourceId="com.sina.weibo:id/ivUserPic").exists == True
            # d.press("back")
            # sleep(2)
            self.d.press("back")
        elif (self.d(text=u"登录和我看").exists):
            assert self.d(text=u"登录和我看").exists
            pass
        else:
            self.d.press("back")
            pass

    @allure.step('QQ登录')
    def test_login_qq(self):

        # 我的
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/head_pic").click()
        sleep(2)
        assert self.d(text=u"登录和我看").exists

        # QQ账号登录
        sleep(2)
        self.d(text=u"QQ账号登录").click()
        sleep(5)
        assert self.d(resourceId="com.tencent.mobileqq:id/name",
                      className="android.widget.ImageView").exists
        self.d.press("back")
        sleep(5)

        assert self.d(resourceId="com.chinamobile.cloudapp:id/home_cloud_title").get_text() == u"登录和我看"


if __name__=="__main__":
    pytest.main("test_004_login_thd.py")

