#coding=utf-8
import uiautomator2 as u2
from time import sleep
from po import ExcuteCase as E, proxy
import pytest
import allure



@E.E
@allure.step('注册功能')
def test_register():
    str = proxy.url
    d = u2.connect(str)

    # 启动App
    d.app_start("com.chinamobile.cloudapp")
    sleep(2)

    # 我的
    d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/head_pic").click(timeout=5)
    sleep(2)
    # 立即注册
    d(resourceId="com.chinamobile.cloudapp:id/tv_registing").click()
    sleep(2)
    assert d(text=u"注册").exists
    # 输入手机号
    d(resourceId="com.chinamobile.cloudapp:id/et_phone").set_text("18278987897")
    sleep(2)
    # 输入密码
    d(resourceId="com.chinamobile.cloudapp:id/et_pwd").set_text("qqq123")
    sleep(2)
    # 同意协议
    d(resourceId="com.chinamobile.cloudapp:id/cb_agreement").click()
    sleep(5)
    # 下一步
    d(text=u'下一步').click()
    sleep(5)

    assert d(text=u"获取验证码").exists==True
    # 获取验证码
    #d(resourceId="com.chinamobile.cloudapp:id/button_get_sms").click()
    sleep(5)
    # 停止app
    d.app_stop("com.chinamobile.cloudapp")



if __name__=="__main__":
    # test_register()
    pytest.main("test_002_register.py")
