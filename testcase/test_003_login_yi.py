#coding=utf-8
import uiautomator2 as u2
from time import sleep
from po import ExcuteCase as E, proxy
import pytest
import allure

class Test_login_yijian():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        self.d.app_stop("com.chinamobile.cloudapp")

    @allure.step('一键登录')
    def test_login_yi(self):
        # 我的
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
        if self.d(resourceId="com.chinamobile.cloudapp:id/head_pic").exists:
            self.d(resourceId="com.chinamobile.cloudapp:id/head_pic").click()
        else:
            raise Exception(u"没有找到控件!")

        # 一键登录
        self.d(resourceId="com.chinamobile.cloudapp:id/fl_login_yidong").click()
        sleep(5)
        if self.d(text=u"个人中心").exists:
            sleep(5)
            assert self.d(text=u"个人中心").exists == True
            self.d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
            self.d(resourceId="com.chinamobile.cloudapp:id/login_out").click()
        else:
            assert self.d(text=u"登录和我看").exists == True




if __name__=="__main__":
    # test_login_yi()
    pytest.main("test_003_login_yi.py")


