# -*- encoding=utf8 -*-
__author__ = "o_zhuangzhang"

import wda
from airtest.core.api import *
from poco.drivers.ios import iosPoco
from ios_device.py_ios_device import PyiOSDevice
from airtest.report.report import simple_report
import sys

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


class HomeClassify():
    # fanxing="com.kugou.fanxing"
    fanxing = "com.kugou.fanxingappstore"

    def step(self):
        self.setup()
        self.clicktab()

    def setup(self):
        stop_app(self.fanxing)
        # clear_app(self.fanxing)
        start_app(self.fanxing)
        sleep(5.0)
        # logPop = poco("Window").child("Other").child("Other").child("Other").child("Other").child("Other").child(
        # "Other").child("Other")[0].child("Other").child("Other")[1].child("Button") logPop.click()
        if exists(Template(r"tpl1654594853613.png", record_pos=(0.309, -0.224), resolution=(1170, 2532))):
            touch(Template(r"tpl1654594853613.png", record_pos=(0.309, -0.224), resolution=(1170, 2532)))
        # 下方代码跑非debug包引起程序暂停，需要跑debug包再取消注释
        # poco("fx_debug_logo").swipe([0.0401, 0.3963])
        if exists(Template(r"tpl1654596585453.png", record_pos=(0.452, -0.798), resolution=(1170, 2532))):
            touch((Template(r"tpl1654596585453.png", record_pos=(0.452, -0.798), resolution=(1170, 2532))))

    def clicktab(self):
        name = {'附近': Template(r"tpl1654593835654.png", record_pos=(-0.349, -0.621), resolution=(1170, 2532)),
                '推荐': Template(r"tpl1654593845955.png", record_pos=(-0.118, -0.62), resolution=(1170, 2532)),
                '新秀': Template(r"tpl1654593865799.png", record_pos=(0.12, -0.621), resolution=(1170, 2532)),
                '歌手': Template(r"tpl1654593877261.png", record_pos=(0.349, -0.62), resolution=(1170, 2532)),
                '竖屏': Template(r"tpl1654593887743.png", record_pos=(-0.353, -0.498), resolution=(1170, 2532)),
                '颜值': Template(r"tpl1654593896400.png", record_pos=(-0.12, -0.497), resolution=(1170, 2532)),
                '游戏': Template(r"tpl1654593906848.png", record_pos=(-0.355, -0.373), resolution=(1170, 2532)),
                '舞蹈': Template(r"tpl1654593917863.png", record_pos=(0.354, -0.491), resolution=(1170, 2532))}
        if exists(Template(r"tpl1654594411514.png", record_pos=(0.401, -0.73), resolution=(1170, 2532))):
            for k, v in name.items():
                assert_exists(name[k])
        elif not exists(Template(r"tpl1654594411514.png", record_pos=(0.401, -0.73), resolution=(1170, 2532))):
            if exists(Template(r"tpl1654596585453.png", record_pos=(0.452, -0.798), resolution=(1170, 2532))):
                touch((Template(r"tpl1654596585453.png", record_pos=(0.452, -0.798), resolution=(1170, 2532))))
            for k, v in name.items():
                assert_exists(name[k])


def main():
    try:
        HomeClassify().step()
    finally:
        simple_report(__file__, logpath=True,
                      output=r"C:\Users\o_zhuangzhang\Desktop\uiauto-master-2ea07ecf17e65a33cfef61c201b1b7aed73324e6"
                             r"\uiauto-master-2ea07ecf17e65a33cfef61c201b1b7aed73324e6\report\log.html")
        print("-----执行完毕-----")
        os._exit(0)


if __name__ == '__main__':
    main()
