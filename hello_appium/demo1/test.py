#启动参数设置及打开界面

from appium import webdriver
print(1)
import time
# 创建字典，包含对应启动参数
des_caps = dict()
# 平台 不限制大小写    android ios
des_caps['platformName'] = 'android'
# 手机版本（5.2.1的版本可以写成5 或 5.2 或 5.2.1）
des_caps['platformVersion'] = '7'
# 连接的手机设备号 android平台可以随便写 但不能不写  
des_caps['deviceName'] = '1'
# 包名
des_caps['appPackage'] = 'com.android.settings'
# 界面名
des_caps['appActivity'] = 'com.android.settings.HWSettings'
# 连接appium服务器
driver = webdriver.Remote('http://localhost:4723/wd/hub',des_caps)
time.sleep(4)
# 退出
driver.quit()




des_caps = dict()
des_caps['platformName'] = 'android'
des_caps['platformVersion'] = '7'
des_caps['deviceName'] = '1'
des_caps['noReset'] = 'true'
des_caps['appPackage'] = 'com.android.settings'
des_caps['appActivity'] = 'com.android.settings.HWSettings'
driver = webdriver.Remote('http://localhost:4723/wd/hub',des_caps)


