# -*- coding: utf-8 -*-
import traceback
import sys
import uiautomator2 as u2
import proxy
import time
import datetime

str = proxy.url
d = u2.connect(str)






def E(func):
    def wrapper(*args, **kwargs):
        error_msg = True
        #T1= time.time()
        try:
            func(*args, **kwargs)
        except Exception as e:
            print("%s 用例运行失败,请检查！"% func.__name__)
            error_msg=traceback.format_exc()
            print(error_msg)
            d.app_stop("com.chinamobile.cloudapp")
        # finally:
        #     print "结果是:",

    return wrapper
#return E

def time(func):
    def int_time(*args, **kwargs):
        start_time = datetime.datetime.now()  # 程序开始时间
        func(*args, **kwargs)
        over_time = datetime.datetime.now()   # 程序结束时间
        total_time = (over_time-start_time).total_seconds()
        print('程序运行%s秒' % total_time)
    return int_time