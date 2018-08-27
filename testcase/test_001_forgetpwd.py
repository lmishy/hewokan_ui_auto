#coding=utf-8
import uiautomator2 as u2
from time import sleep
from po import proxy
import pytest
import allure


class Test_forgetpwd():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        sleep(5)
        self.d.app_stop("com.chinamobile.cloudapp")

    @allure.step('忘记密码')
    def test_forgetpwd(self):
        # 我的
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click(timeout=20)
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/head_pic").click(timeout=20)
        sleep(2)
        # 忘记密码
        self.d(resourceId="com.chinamobile.cloudapp:id/tv_get_pwd").click(timeout=20)
        sleep(2)
        # 输入手机号
        self.d(resourceId="com.chinamobile.cloudapp:id/et_phone").set_text("15295990599")
        sleep(2)
        # 获取验证码
        self.d(resourceId="com.chinamobile.cloudapp:id/button_get_sms").click(timeout=20)
        sleep(5)
        assert self.d(text=u"找回密码").exists 
        sleep(5)


if __name__=="__main__":
    pytest.main()

