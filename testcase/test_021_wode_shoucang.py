#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/7
import uiautomator2 as u2
from time import sleep
from po import proxy,ExcuteCase as E
import pytest
import allure

@E.E
@allure.step('我的--我的收藏')
def test_wode_shoucang():
    str = proxy.url
    # 连接手机
    d = u2.connect(str)

    # 启动App
    d.app_start("com.chinamobile.cloudapp")

    # 切换我的tab
    d(resourceId="com.chinamobile.cloudapp:id/root_bottom_home_tab_5").click()
    sleep(2)
    # 我的收藏
    d(text=u"我的收藏").click()
    sleep(2)
    #播放节目
    d(resourceId="com.chinamobile.cloudapp:id/collect_item_head").click()
    sleep(5)
    d.press("back")
    sleep(2)
    #编辑
    d(resourceId="com.chinamobile.cloudapp:id/home_cloud_edit").click()
    sleep(2)
    #选择单个
    d(resourceId="com.chinamobile.cloudapp:id/collect_item_select").click()
    sleep(2)
    #取消删除
    d(resourceId="com.chinamobile.cloudapp:id/delete_con_btn").click()
    sleep(2)
    d(resourceId="com.chinamobile.cloudapp:id/dialog_show_button2").click()
    sleep(2)
    #确定删除
    d(resourceId="com.chinamobile.cloudapp:id/delete_con_btn").click()
    d(resourceId="com.chinamobile.cloudapp:id/dialog_show_button1").click()
    sleep(2)
    #全选视频
    d(resourceId="com.chinamobile.cloudapp:id/home_cloud_edit").click()
    d(resourceId="com.chinamobile.cloudapp:id/listView").click()
    #切换资讯
    d(resourceId="com.chinamobile.cloudapp:id/tv_collect_tab1").click()
    sleep(2)
    #切换电台
    d(resourceId="com.chinamobile.cloudapp:id/tv_collect_tab3").click()
    sleep(2)
    d.press("back")

    sleep(5)
    # 停止app
    d.app_stop("com.chinamobile.cloudapp")



if __name__ == "__main__":
    pytest.main()

