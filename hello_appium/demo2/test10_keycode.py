#发送键到设备
#按键对应的编码报读  android keycode

from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction
import appium
from appium.webdriver.connectiontype import ConnectionType


des_caps = dict()
des_caps['platformName'] = 'android'
des_caps['platformVersion'] = '7'
des_caps['deviceName'] = '11'
des_caps['noReset'] = 'true'
des_caps['appPackage'] = 'com.android.settings'
des_caps['appActivity'] = '.Settings$ScreenLockSettingsActivity'
#如果输入中文有问题，加入这两行代码试一试
des_caps['unicodekeyboard'] = True
des_caps['resetkeyboard'] = True  
driver = webdriver.Remote('http://localhost:4723/wd/hub',des_caps)
#隐式等待三秒
driver.implicitly_wait(3)

'''
#增加两次音量，再减少两次音量
driver.press_keycode(24)
time.sleep(2)
driver.press_keycode(24)
time.sleep(2)
driver.press_keycode(25)
time.sleep(2)
driver.press_keycode(25)
'''

# 打开通知栏
driver.open_notifications()
# 关闭通知栏，没有官方方法，按返回键或者向上滑动
time.sleep(3)
driver.press_keycode(4)

time.sleep(5)
driver.quit()