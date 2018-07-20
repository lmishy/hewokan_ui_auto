#coding=utf-8
import uiautomator2 as u2
from time import sleep
from po import ExcuteCase as E, proxy
import pytest
import allure


class Test_register():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        sleep(5)
        self.d.app_stop("com.chinamobile.cloudapp")

    @allure.step('注册功能')
    def test_register(self):

        # 我的
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/head_pic").click(timeout=5)
        sleep(2)
        # 立即注册
        self.d(resourceId="com.chinamobile.cloudapp:id/tv_registing").click()
        sleep(2)
        assert self.d(text=u"注册").exists
        # 输入手机号
        self.d(resourceId="com.chinamobile.cloudapp:id/et_phone").set_text("18278987897")
        sleep(2)
        # 输入密码
        self.d(resourceId="com.chinamobile.cloudapp:id/et_pwd").set_text("qqq123")
        sleep(2)
        # 同意协议
        self.d(resourceId="com.chinamobile.cloudapp:id/cb_agreement").click()
        sleep(5)
        # 下一步
        self.d(text=u'下一步').click()
        sleep(5)

        assert self.d(text=u"获取验证码").exists
        sleep(5)
        # 获取验证码
        # d(resourceId="com.chinamobile.cloudapp:id/button_get_sms").click()





if __name__=="__main__":
    pytest.main("test_002_register.py")
