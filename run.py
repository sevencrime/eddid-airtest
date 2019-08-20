#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- encoding=utf8 -*-
__author__ = "Onedi Zheng"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

auto_setup(__file__)

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

start_app("io.newtype.eddid.app")

# poco("io.newtype.eddid.app:id/btn_start").click()
poco(text="开户").click()
poco(text="便捷开户").click()
poco(text="去登录").click()
poco(text="请输入手机号").set_text("15089514626")
poco(text="请输入密码").set_text("abcd1234")

poco("android.widget.ScrollView").child("android.widget.TextView").child("android.view.ViewGroup").child("android.widget.TextView", text="登录")



