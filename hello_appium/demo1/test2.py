#在脚本内启动其他app


from appium import webdriver
import time

# 创建字典，包含对应启动参数
des_caps = dict()
# 手机参数
des_caps['platformName'] = 'android'
des_caps['platformVersion'] = '7'
des_caps['deviceName'] = '1'
# 应用参数  包名、界面名
des_caps['appPackage'] = 'com.android.settings'
des_caps['appActivity'] = 'com.android.settings.HWSettings'
#不重新登录
des_caps['noReset'] = 'true'
# 获取driver
driver = webdriver.Remote('http://localhost:4723/wd/hub',des_caps)

time.sleep(2)

#driver.start_activity("com.android.mms",".ui.ConversationList")
#跳转微信
driver.start_activity("com.tencent.mm","com.tencent.mm.ui.LauncherUI")

time.sleep(2)
# 退出
driver.quit()
