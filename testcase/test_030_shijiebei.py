#!/usr/bin/python2
# -*- coding:utf-8 -*-
#@time: 2018/6/14
import uiautomator2 as u2
from time import sleep
from po import proxy
import pytest
import allure

class Test_shijiebei():
    def setup(self):
        str = proxy.url
        self.d = u2.connect(str)
        self.d.app_start("com.chinamobile.cloudapp")
        sleep(5)

    def teardown(self):
        self.d.app_stop("com.chinamobile.cloudapp")

    @allure.step('热点--世界杯专区')
    def test_shijiebei(self):

        # 世界杯专区
        self.d(text=u"世界杯专区").click()
        sleep(5)
        assert self.d(text=u"世界杯专区").exists == True
        sleep(5)
        # 点击banner
        if (self.d(text=u"一瓶啤酒钱，快乐一夏天").exists):
            self.d(text=u"一瓶啤酒钱，快乐一夏天").click()
            self.d(text=u"咪咕钻石会员-超级视频").wait(timeout=10)
            sleep(5)
            self.d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
            sleep(2)
            # 点击开通
            self.d(description=u"btn").click()
            sleep(2)
            self.d(resourceId="close").click(timeout=5)
            self.d.press("back")
        elif (self.d(text=u"竞猜666，大奖赢不停").exists):
            self.d(text=u"竞猜666，大奖赢不停").click()
            self.d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
            # 分享
            self.d(resourceId="share").click(timeout=10)
            self.d.press("back")
            sleep(5)
            # 活动规则
            self.d(resourceId="rules").click(timeout=10)
            self.d(resourceId="cover2").click(timeout=10)
            sleep(5)
            # 会员兑换
            self.d(resourceId="exchange").click(timeout=5)
            # 大厅
            self.d(resourceId="hall").click(timeout=5)
            # 我的竞猜
            self.d(resourceId="myguess").click(timeout=5)
            self.d.press("back")

        elif (self.d(text=u"世界杯权益 领取专用通道").exists):
            self.d(description=u"btn").click(timeout = 10)
            self.d.press("back")
        else:
            raise Exception(u"页面请求时间过长，请检查！")

        # 赛程安排
        if (self.d(text=u"赛程安排").exists):
            self.d(text=u"赛程安排").click()
            sleep(5)
            self.d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)
            self.d.press("back")
        else:
            raise Exception(u"找不到控件")

        # 猜球有奖
        if (self.d(text=u"猜球有奖").exists):
            self.d(text=u"猜球有奖").click()
            sleep(5)
            self.d.press("back")
        else:
            raise Exception(u"找不到控件")

        # 福利领取
        if (self.d(text=u"福利领取").exists):
            self.d(text=u"福利领取").click()
            sleep(5)
            self.d.press("back")
        else:
            raise Exception(u"找不到控件")

        # 前线战报
        if (self.d(text=u"前线战报").exists):
            self.d(text=u"前线战报").click()
            sleep(5)
            self.d.press("back")
        else:
            raise Exception(u"找不到控件")

        self.d.swipe(0.5, 0.8, 0.5, 0.2, 0.5)



if __name__=="__main__":
    pytest.main("test_030_shijiebei.py")

