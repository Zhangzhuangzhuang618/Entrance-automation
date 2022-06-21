# -*- encoding=utf8 -*-
__author__ = "o_zhuangzhang"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["ios:///http://127.0.0.1:8200",])


from poco.drivers.ios import iosPoco
poco = iosPoco()
poco(name="更多").click()


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)