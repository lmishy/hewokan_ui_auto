## hewokan_ui_auto配置文档

#### 安装node

[官网地址](https://nodejs.org/en/download/)

* OS:brew install node
* windows,linux参照官网

#### 安装uiautomator2

pip install --pre uiautomator2

pip install pillow

###初始化,部署相关的守护进程。
python -m uiautomator2 init
安装完成，设备上会多一个uiautomator的应用。
电脑连接上一个手机或多个手机, 确保adb已经添加到环境变量中，执行上面的命令会自动安装本库所需要的设备端程序：
uiautomator-server 、atx-agent、openstf/minicap、openstf/minitouch


### python2.7

方法请自行查找


##项目和手机配置
1、确保电脑和手机在同一个网段
2、连接手机配置在po>proxy.py,确保是同一个ip



### 运行


* git 源码
* cd hewokan_ui_auto
* py.test -m testcase/

###如果不在一个网段，则需要一个转发的过程
adb forward tcp:7912 tcp:7912





