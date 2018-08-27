#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/7
import uiautomator2 as u2
from time import sleep
from po import proxy
import pytest
import allure

class Test_wode3():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        sleep(5)
        self.d.app_stop("com.chinamobile.cloudapp")

    @allure.step('我的--我的收藏')
    def test_wode_shoucang(self):
        # 切换我的tab
        self.d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click(timeout=20)
        sleep(2)
        # 我的收藏
        self.d(text=u"我的收藏").click(timeout=20)
        sleep(2)
        # 播放节目
        self.d(resourceId="com.chinamobile.cloudapp:id/collect_item_head").click(timeout=20)
        sleep(5)
        self.d.press("back")
        sleep(2)
        # 编辑
        self.d(resourceId="com.chinamobile.cloudapp:id/home_cloud_edit").click(timeout=20)
        sleep(2)
        # 选择单个
        self.d(resourceId="com.chinamobile.cloudapp:id/collect_item_select").click(timeout=20)
        sleep(2)
        # 取消删除
        self.d(resourceId="com.chinamobile.cloudapp:id/delete_con_btn").click(timeout=20)
        sleep(2)
        self.d(resourceId="com.chinamobile.cloudapp:id/dialog_show_button2").click(timeout=20)
        sleep(2)
        # 确定删除
        self.d(resourceId="com.chinamobile.cloudapp:id/delete_con_btn").click(timeout=20)
        self.d(resourceId="com.chinamobile.cloudapp:id/dialog_show_button1").click(timeout=20)
        sleep(2)
        # 全选视频
        self.d(resourceId="com.chinamobile.cloudapp:id/home_cloud_edit").click(timeout=20)
        self.d(resourceId="com.chinamobile.cloudapp:id/listView").click(timeout=20)
        # 切换资讯
        self.d(resourceId="com.chinamobile.cloudapp:id/tv_collect_tab1").click(timeout=20)
        assert self.d(text=u"资讯").wait(exists=True,timeout=20)
        sleep(2)
        # 切换电台
        self.d(resourceId="com.chinamobile.cloudapp:id/tv_collect_tab3").click(timeout=20)
        assert self.d(text=u"电台").wait(exists=True,timeout=20)
        sleep(2)
        self.d.press("back")


if __name__ == "__main__":
    pytest.main("test_021_wode_shoucang.py")

