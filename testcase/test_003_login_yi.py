#coding=utf-8
import uiautomator2 as u2
from time import sleep
from po import ExcuteCase as E, proxy
import pytest
import allure

@E.E
@allure.step('一键登录')
def test_login_yi():
    str = proxy.url
    d = u2.connect(str)

    # 启动App
    d.app_start("com.chinamobile.cloudapp")
    sleep(2)

    # 我的
    d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
    if d(resourceId="com.chinamobile.cloudapp:id/head_pic").exists:
        d(resourceId="com.chinamobile.cloudapp:id/head_pic").click()
    else:
        raise Exception(u"没有找到控件!")


    # 一键登录
    d(resourceId="com.chinamobile.cloudapp:id/fl_login_yidong").click()
    sleep(5)
    if d(text=u"个人中心").exists:
        sleep(5)
        assert d(text=u"个人中心").exists==True
        d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
        d(resourceId="com.chinamobile.cloudapp:id/login_out").click()
    else:
        assert d(text=u"登录和我看").exists == True


    sleep(5)
    # 停止app
    d.app_stop("com.chinamobile.cloudapp")



if __name__=="__main__":
    # test_login_yi()
    pytest.main()


