# 安装和卸载以及是否安装
#将应用置于后台

from appium import webdriver
import time

des_caps = dict()
des_caps['platformName'] = 'android'
des_caps['platformVersion'] = '7'
des_caps['deviceName'] = '1'
des_caps['noReset'] = 'true'
des_caps['appPackage'] = 'com.android.settings'
des_caps['appActivity'] = 'com.android.settings.HWSettings'
driver = webdriver.Remote('http://localhost:4723/wd/hub',des_caps)


# if driver.is_app_installed("com.zhisland.android.blog"):
#     driver.remove_app("com.zhisland.android.blog")
# else:
#     driver.install_app('C:\\Users\\user\\Desktop\\QA259.apk')


# 将应用置于后台  
driver.background_app(3)



time.sleep(3)
# 退出
driver.quit()
