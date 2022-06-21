# -*- encoding=utf8 -*-
__author__ = "janelin"

import sys
import os
import wda
from airtest.core.api import *
from poco.drivers.ios import iosPoco
from ios_device.py_ios_device import PyiOSDevice
from airtest.report.report import simple_report

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


class RoomSidebar():
    # 获取包名
    fanxing = "com.kugou.fanxingappstore"

    sdidebar1 = {'极品豪车来袭': Template(r"tpl1647419808582.png",
                                    record_pos=(-0.137, -0.68), resolution=(750, 1334)),'充值大狂欢': Template(r"tpl1647419819684.png",
                                   record_pos=(0.271, -0.681), resolution=(750, 1334)),'充值送优惠': Template(r"tpl1647419831240.png",
                                   record_pos=(-0.135, -0.465), resolution=(750, 1334))}
    sdidebar2 = {'合成钻戒': Template(r"tpl1647419843548.png",
                                  record_pos=(-0.257, -0.189), resolution=(750, 1334)),'大话骰': Template(r"tpl1647419859698.png",
                                 record_pos=(-0.097, -0.189), resolution=(750, 1334)),'部落保卫战': Template(r"tpl1647419871772.png",
                                   record_pos=(0.064, -0.189), resolution=(750, 1334)),'魔法音乐盒': Template(r"tpl1647419887750.png",
                                   record_pos=(0.227, -0.188), resolution=(750, 1334)),'甜蜜约定': Template(r"tpl1647419906645.png",
                                  record_pos=(0.388, -0.189), resolution=(750, 1334)),'三国大富翁': Template(r"tpl1647419917486.png",
                                   record_pos=(-0.255, 0.005), resolution=(750, 1334)),'阳光农场': Template(r"tpl1647419976874.png",
                                  record_pos=(-0.097, 0.003), resolution=(750, 1334)),
                 '许愿': Template(r"C:tpl1647419988681.png",
                                record_pos=(0.064, 0.005), resolution=(750, 1334)),'神秘礼包': Template(r"tpl1647419999092.png",
                                  record_pos=(0.227, 0.007), resolution=(750, 1334)),'充值优惠': Template(r"tpl1647420016246.png",
                                  record_pos=(0.388, 0.004), resolution=(750, 1334)),'全民推币机': Template(r"tpl1647420027644.png",
                                   record_pos=(-0.256, 0.2), resolution=(750, 1334)),'狂野飙车': Template(r"tpl1647420039342.png",
                                  record_pos=(-0.096, 0.201), resolution=(750, 1334)),'钓鱼达人': Template(r"tpl1647420575206.png",
                                  record_pos=(0.067, 0.199), resolution=(750, 1334)),'天天要抓球': Template(r"tpl1647420586856.png",
                                   record_pos=(0.227, 0.2), resolution=(750, 1334)),'玩更多': Template(r"tpl1647420612022.png",
                                 record_pos=(-0.257, 0.396), resolution=(750, 1334))}
    
    
    sdidebar1New = {'充值大狂欢': Template(r"tpl1654583542895.png", record_pos=(0.227, -0.779), resolution=(1170, 2532)),'充值送优惠':Template(r"tpl1654583552484.png", record_pos=(-0.158, -0.778), resolution=(1170, 2532))}
    sdidebar2New = {'许愿': Template(r"C:tpl1647419988681.png",record_pos=(0.064, 0.005), resolution=(750, 1334)),'神秘礼包': Template(r"tpl1647419999092.png",
                                  record_pos=(0.227, 0.007), resolution=(750, 1334))}
    sdidebar3 = {'任务中心':Template(r"tpl1654584514689.png", record_pos=(-0.234, -0.585), resolution=(1170, 2532)),'签到':Template(r"tpl1654584448456.png", record_pos=(-0.252, -0.467), resolution=(1170, 2532)),'分享':Template(r"tpl1654584436664.png", record_pos=(0.144, -0.465), resolution=(1170, 2532)),'私信':Template(r"tpl1654584428278.png", record_pos=(-0.256, -0.306), resolution=(1170, 2532)),'广告 ':Template(r"tpl1654584416839.png", record_pos=(0.141, -0.309), resolution=(1170, 2532)),'关注':Template(r"tpl1654584403374.png", record_pos=(-0.254, -0.15), resolution=(1170, 2532)),'观看':Template(r"tpl1654584388399.png", record_pos=(0.142, -0.152), resolution=(1170, 2532))}
    

    # 前置进房工作
    def setup(self):
        #print('-------------------------------进房前置工作--------------------------------------')
        stop_app(self.fanxing)
        start_app(self.fanxing)
        sleep(5)
        room = poco("Window").child("Other").child("Other").child("Other").child("Other").child("Other").child(
            "Other").child("Other")[0].child("ScrollView").child("Other").child("CollectionView").child("Cell")[0]
        room.click()
        sleep(10)
        #下面这行语句似乎触发了其他控件所以注释掉改为poco方式
        #wda.Client('http://localhost:8200')(label="更多").click()
        #print('-------------------------------打开侧边栏--------------------------------------')
        poco(name="更多").click()
        sleep(30)

    def step(self):
        #print('-------------------------------准备启动进房前置工作--------------------------------------')
        self.setup()
        #print('-------------------------------进房前置工作完成启动qita方法--------------------------------------')
        self.qita()
        self.huodong()
        self.renwuzhongxin()
        self.quanyi()
        #self.zhaorenwan()
        #self.Task_center()
        self.stop()

    def qita(self):
        for k, v in self.sdidebar1New.items():
            assert_exists(self.sdidebar1New[k])

    def huodong(self):
        for k, v in self.sdidebar2New.items():
            assert_exists(self.sdidebar2New[k])

    #         for i in range(len(sdidebar)):
    #             assert_exists(sdidebar[i+1])
    #             pint (i)
    
    def renwuzhongxin(self):
        poco(name='查看更多').click()
        for k, v in self.sdidebar3.items():
            assert_exists(self.sdidebar3[k])
    
    def quanyi(self):
        assert_exists(Template(r"tpl1654584712825.png", record_pos=(0.059, 0.784), resolution=(1170, 2532)))
    

    def zhaorenwan(self):
        p = exists(Template(r"tpl1647483627030.png",
                            record_pos=(-0.271, 0.388), resolution=(750, 1334)))
        assert (p)
        assert_exists(Template(r"tpl1647482682434.png",
                               record_pos=(0.345, 0.599), resolution=(750, 1334)), "任务中心发起图标")
        assert_exists(Template(r"tpl1647482695259.png",
                               record_pos=(-0.201, 0.497), resolution=(750, 1334)), "主题")
    
    def Task_center(self):
        poco("找人玩").swipe("up")
        assert_exists(Template(r"tpl1647482807578.png",
                               record_pos=(-0.259, -0.081), resolution=(750, 1334)), "任务中心")
        assert_exists(Template(r"tpl1647482815643.png",
                               record_pos=(0.384, -0.081), resolution=(750, 1334)), "任务中心入口")
    
    def stop(self):
        stop_app(self.fanxing)


def main():
    try:
        RoomSidebar().step()
    finally:
        simple_report(__file__, logpath=True,
                      output=r"C:\Users\o_zhuangzhang\Desktop\uiauto-master-2ea07ecf17e65a33cfef61c201b1b7aed73324e6\uiauto-master-2ea07ecf17e65a33cfef61c201b1b7aed73324e6\report\log.html")
        print("-----执行完毕-----")
        os._exit(0)
if __name__ == '__main__':
    main()