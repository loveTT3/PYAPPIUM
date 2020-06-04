#获取app的包名和界面名
#关闭app和驱动对象


from appium import webdriver
import time


# 创建字典，包含对应启动参数
des_caps = dict()
# 手机参数
des_caps['platformName'] = 'android'
des_caps['platformVersion'] = '7'
des_caps['deviceName'] = '1'
#不重新登录
des_caps['noReset'] = 'true'

# 应用参数  包名、界面名
# des_caps['appPackage'] = 'com.android.settings'
# des_caps['appActivity'] = 'com.android.settings.HWSettings'
'''
这个是启动页， 必须使用这个界面名    .aa.controller.SplashActivity  
'''
# des_caps['appPackage'] = 'com.zhisland.android.blog'
# des_caps['appActivity'] = '.aa.controller.SplashActivity'

# 获取driver
driver = webdriver.Remote('http://localhost:4723/wd/hub',des_caps)



#输出当前程序包名界面名
print(driver.current_package)
print(driver.current_activity)


time.sleep(5)
#关闭应用程序，不关闭驱动对象
driver.close_app()
#关闭驱动对象
driver.quit()
