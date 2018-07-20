#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/7

import uiautomator2 as u2
from time import sleep
from po import proxy
import pytest
import allure

class Test_wode2():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        sleep(5)
        self.d.app_stop("com.chinamobile.cloudapp")

    @allure.step('我的--观看历史')
    def test_wode_lishi(self):

        # 切换我的tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
        sleep(2)
        # 观看历史
        self.d(text=u"观看历史").click()
        sleep(2)
        # 过滤短视频
        self.d(resourceId="com.chinamobile.cloudapp:id/filter_short_video_icon").click()
        self.d(resourceId="com.chinamobile.cloudapp:id/filter_short_video_icon").click()
        sleep(2)
        # 编辑
        self.d(resourceId="com.chinamobile.cloudapp:id/home_cloud_edit").click()
        sleep(2)
        # 选择单个
        self.d(resourceId="com.chinamobile.cloudapp:id/collect_item_select").click()
        sleep(2)
        # 删除
        self.d(resourceId="com.chinamobile.cloudapp:id/delete_con_btn").click()
        sleep(2)
        # 确认删除
        self.d(resourceId="com.chinamobile.cloudapp:id/dialog_show_button1").click()
        sleep(2)
        # 全选
        self.d(resourceId="com.chinamobile.cloudapp:id/home_cloud_edit").click()
        self.d(resourceId="com.chinamobile.cloudapp:id/delete_all_btn").click()
        self.d(resourceId="com.chinamobile.cloudapp:id/delete_all_btn").click()
        sleep(2)
        # 切换资讯
        self.d(resourceId="com.chinamobile.cloudapp:id/tv_his_tab1").click()
        sleep(2)
        # 切换电台
        self.d(resourceId="com.chinamobile.cloudapp:id/tv_his_tab3").click()
        sleep(2)
        self.d.press("back")






if __name__ == "__main__":
    pytest.main("test_020_wode_lishi.py")

