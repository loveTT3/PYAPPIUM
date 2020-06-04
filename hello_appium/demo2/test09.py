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



#获取当前屏幕分辨率
'''
print(driver.get_window_size())
print(driver.get_window_size()['height'])
print(driver.get_window_size()['width'])
'''


#截图当前屏幕,保存到指定文件夹
'''
driver.get_screenshot_as_file("C:\\Users\\user\\Desktop\\666.png")
'''

#获取当前网络信息
print(driver.network_connection)

'''#  from appium.webdriver.connectiontype import ConnectionType
class ConnectionType(object):
    NO_CONNECTION = 0
    AIRPLANE_MODE = 1
    WIFI_ONLY = 2
    DATA_ONLY = 4
    ALL_NETWORK_ON = 6
'''
if driver.network_connection == ConnectionType.NO_CONNECTION:
    pass

#设置当前网络
driver.set_network_connection(6)



driver.quit()