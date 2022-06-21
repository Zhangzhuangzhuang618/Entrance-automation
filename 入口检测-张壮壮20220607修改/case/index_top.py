# -*- encoding=utf8 -*-
__author__ = "o_zhuangzhang"

import wda
from airtest.core.api import *
from poco.drivers.ios import iosPoco
from ios_device.py_ios_device import PyiOSDevice
from airtest.report.report import simple_report
import sys
import time

# simple_report(__file__,logpath=True,output=r"C:\\Users\\janelin\\Desktop\\entrance\\ios_roomsidebar.air\\report\\log.html")

# 连接设备
device = PyiOSDevice()
wda_bundle_id = 'com.appiumtest21.WebDriverAgentRunner.xctrunner'
web_driver_agent_url = ""
wda_port = 8200


def xctest_callback(res):
    global web_driver_agent_url
    print(res)


xctest = device.start_xcuitest(bundle_id=wda_bundle_id, callback=xctest_callback,
                               app_env={"USE_PORT": wda_port}, pair_ports=["8200:8200"])
auto_setup(__file__, logdir=True, devices=['iOS:///localhost:8200'])
poco = iosPoco()


class HomeTop():
    # 获取包名
    # fanxing="com.kugou.fanxingappstore1"
    fanxing = "com.kugou.fanxingappstore1"

    # 执行测试用例clicktab方法
    def step(self):
        self.setup()
        self.clicktab()
        self.login()

    # 初始化及前置操作
    def setup(self):
        stop_app(self.fanxing)
        # clear_app(self.fanxing)
        start_app(self.fanxing)
        sleep(5.0)
        if poco("同意").exists():
            poco("同意").click()
        if poco("允许“酷狗直播”跟踪您在其他公司的App和网站上的活动吗？").exists():
            poco("要求App不跟踪").click()
        if poco("“酷狗直播”想要查找并连接到本地网络上的设备。").exists():
            poco("好").click()
        if poco("“酷狗直播”想给您发送通知").exists():
            poco("允许").click()
        if poco("其他登录方式").exists():
            poco("其他登录方式").click()
            self.login()
        if poco("fx_debug_logo").exists():
            poco("fx_debug_logo").swipe([0.0401, 0.3963])

    def login(self):
        if poco(name="我的").exists():
            poco(name="我的").click()
        if not exists(Template(r"tpl1647508050205.png", record_pos=(-0.368, -0.401), resolution=(1170, 2532))):
            poco("Window").child("Other").child("Other").child("Other").child("Other")[1].child("Other").child(
                "Other").child("Other").child("Other").child("Other").offspring("账号登录").click()
            touch(Template(r"tpl1647499554233.png", record_pos=(-0.177, -0.68), resolution=(1170, 2532)))
            text("ayawawatest")
            touch(Template(r"tpl1647499759998.png", record_pos=(-0.308, -0.529), resolution=(1170, 2532)))
            text("zRczT1aB")
            touch(Template(r"tpl1647500266552.png", record_pos=(-0.007, -0.312), resolution=(1170, 2532)))
            poco("同意").click()
            if poco(name="跳过").exists():
                poco(name="跳过").click()
            poco(name="首页").click()
            if poco(name="我知道了").exists():
                poco(name="我知道了").click()
        else:
            touch(Template(r"tpl1647508991120.png", record_pos=(-0.362, 0.943), resolution=(1170, 2532)))

    # 测试用例
    def clicktab(self):
        # 获取榜单控件
        ranlist = \
        poco("Window").child("Other").child("Other").child("Other").child("Other").child("Other").child("Other").child(
            "Other")[0].child("Other").child("Other")[0].child("Button")[0]

        # 获取搜索框控件
        search = poco("Window").child("Other").child("Other").child("Other").child("Other").child("Other").child("Other").child(
            "Other")[0].child("Other").offspring("TextField")[0]
        # 获取历史观看控件
        history = poco("Window").child("Other").child("Other").child("Other").child("Other").child("Other").child(
            "Other").child("Other")[0].child("Other").child("Other")[0].child("Button")[1]
        # 获取我的关注控件
        myfollow = poco("Window").child("Other").child("Other").child("Other").child("Other").child("Other").child("Other").child(
            "Other")[0].child("Other").child("Other")[0].child("Other")[1].child("Button")
        # 判断榜单是否正常
        if ranlist.exists():
            assert_exists(Template(r"tpl1647940966577.png", record_pos=(-0.429, -0.78), resolution=(750, 1334)), "榜单")
            ranlist.click()
            sleep(3.0)
            if poco(name="小时榜").exists():
                poco(name='返回').click()
                print('控件榜单正常')
        else:
            print('控件榜单不正常')

        # 判断搜索框控件是否正常
        if search.exists():
            search.click()
            sleep(3.0)
            poco("Window").child("Other").child("Other").child("Other").child("Other")[1].child("Other").child(
                "Other").child("Other").child("Other").child("Other").child("Other")[0].child("Other").child("取消").child("取消").click()
            print('控件搜索框正常')
        else:
            print('控件搜索框不正常')

        # 判断观看历史记录控件是否正常
        if history.exists():
            assert_exists(Template(r"tpl1647940997543.png", record_pos=(0.343, -0.78), resolution=(750, 1334)), "历史记录")
            history.click()
            assert_exists(Template(r"tpl1647941461206.png", record_pos=(0.425, -0.776), resolution=(750, 1334)), "清空按钮")
            touch(Template(r"tpl1647941515875.png", record_pos=(-0.436, -0.78), resolution=(750, 1334)))

            # 判断我的关注框控件是否正常
        if myfollow.exists():
            myfollow.click()
            sleep(3.0)
            if poco(name="我关注的").exists():
                # poco("Window").child("Other")[1].child("Other").child("Button").click()
                print('控件我的关注正常')
        else:
            print('控件我的关注不正常')


def main():
    try:
        HomeTop().step()
    finally:
        simple_report(__file__, logpath=True,
                      output=r"C:\Users\janelin\PycharmProjects\uientrance\report\log.html")
        print("-----执行完毕-----")
        os._exit(0)

if __name__ == '__main__':
    main()