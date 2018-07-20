#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/8
import uiautomator2 as u2
from time import sleep
from po import proxy
import pytest
import allure

class Test_wode8():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        sleep(5)
        self.d.app_stop("com.chinamobile.cloudapp")

    @allure.step('我的--设置')
    def test_wode_shezhi(self):

        # 切换我的tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
        sleep(2)
        # 向上滑动
        self.d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)

        # 设置
        self.d(text=u"设置").click()
        sleep(2)
        assert self.d(text=u"设置").exists 
        sleep(5)
        # 修改密码
        self.d(resourceId="com.chinamobile.cloudapp:id/layout_change_psd").click()
        sleep(2)
        assert self.d(text=u"修改密码").exists 
        self.d(resourceId="com.chinamobile.cloudapp:id/et_old_pwd").set_text("12346")
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/et_new_pwd1").set_text("123456")
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/et_new_pwd2").set_text("123456")
        sleep(2)
        self.d.press("back")
        sleep(2)
        self.d.press("back")
        sleep(2)
        # 开启2G/3G/4G网络自动播放
        self.d(resourceId="com.chinamobile.cloudapp:id/checkBox").click()
        sleep(2)
        # 关闭2G/3G/4G网络自动播放
        self.d(resourceId="com.chinamobile.cloudapp:id/checkBox").click()
        sleep(2)
        # 清理缓存
        self.d(resourceId="com.chinamobile.cloudapp:id/rl_clear_cache").click()
        sleep(2)
        assert self.d(text=u'0K').exists 
        self.d.press("back")
        sleep(5)



if __name__ == "__main__":
    pytest.main("test_026_wode_shezhi.py")

