## hewokan_ui_auto配置文档

##环境配置 ： 1、安装node
           2、安装python2.7
           3、安装uiautomator2  ：pip install --pre uiautomator2  ；pip install pillow
           4、下载allure2 报告生成工具 (建议放在和工程同一个目录下，方便查看)附链接（https://bintray.com/qameta/generic/allure2/2.6.0）


##python 安装包列表：
            1、pytest
            2、pytest-allure-adaptor
            3、urllib
            4、BeautifulSoup
            5、requests

##运行前准备：
            1、用数据线连接手机和电脑，打开命令提示符窗口，输入python -m uiautomator2 init，回车，出现success后手机和电脑连接完成
            2、如果在同一个网段，手机ip配置在po>proxy.py,进行修改，保证 url="手机IP"
            3、如果手机和电脑不在一个网段，需要运行adb forward tcp:7912 tcp:7912

##运行：
      1、在pycham等编辑器，直接右键运行即可
      2、python 命令运行：cd hewokan_ui_auto
                        python -m pytest testcase/ --alluredir report/
      3、结合jenkins运行：构建一个git/svn项目，构建后操作添加allure report,点击构建即可


##查看报告：
         1、进入报告生成工具allure2\bin目录
         2、命令运行完之后，运行命令allure generate hewokan_ui_auto/report/ -o hewokan_ui_auto/report/html 生成报告，进入report/html文件夹点击index.html即可查看相关报告
         3、在jenkins构建完成之后，点击构建项目右侧图标即可查看相关报告

##注意：
       1、目前项目在jenkins上运行暂时只支持本地

















