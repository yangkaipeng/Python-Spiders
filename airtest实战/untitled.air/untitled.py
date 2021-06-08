# -*- encoding=utf8 -*-
__author__ = "yangkaipeng"

from airtest.core.api import *

auto_setup(__file__)
import time


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# poco(text="知乎").click()
# time.sleep(6)
# poco(name="com.zhihu.android:id/input").click()
# poco(name="com.zhihu.android:id/input").set_text("新疆棉花")
# poco(name="com.zhihu.android:id/query").click()
text_obj_list = poco(name="android.view.View",textMatches=".+")
text_list = [title.get_text() for title in text_obj_list]

print(text_list)