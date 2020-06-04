from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction
import appium

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


#打开设置的绘制图案密码
driver.find_element_by_xpath("//*[@bounds='[48,349][786,410]']").click()
#末尾加右斜线，将代码换行
driver.find_element_by_xpath("//*[@bounds='[48,397][984,512]']")\
.click()
time.sleep(1)
#代码太长，加括号
(TouchAction(driver).press(x=262,y=808)
.move_to(x=816,y=1362).release().perform())


time.sleep(3)
driver.quit()