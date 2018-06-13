#coding=utf-8
import uiautomator2 as u2
from time import sleep
from po import proxy,ExcuteCase as E
import pytest
import allure




@E.E
@allure.step('忘记密码')
def test_forgetpwd():
    str = proxy.url
    d = u2.connect(str)

    # 启动App
    d.app_start("com.chinamobile.cloudapp")
    sleep(2)
    # 我的
    d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/head_pic").click()
    sleep(2)
    # 忘记密码
    d(resourceId="com.chinamobile.cloudapp:id/tv_get_pwd").click()
    sleep(2)
    # 输入手机号
    d(resourceId="com.chinamobile.cloudapp:id/et_phone").set_text("15295990599")
    sleep(2)
    # 获取验证码
    d(resourceId="com.chinamobile.cloudapp:id/button_get_sms").click()
    sleep(5)
    assert d(text=u"找回密码").exists


    # 停止app
    d.app_stop("com.chinamobile.cloudapp")







if __name__=="__main__":
    pytest.main("test_001_forgetpwd.py")

