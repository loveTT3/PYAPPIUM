from appium import webdriver
import time

des_caps = dict()
des_caps['platformName'] = 'android'
des_caps['platformVersion'] = '6'
des_caps['deviceName'] = '1'
des_caps['noReset'] = 'true'
des_caps['appPackage'] = 'com.zhisland.android.blog'
des_caps['appActivity'] = '.aa.controller.SplashActivity'
#如果输入中文有问题，加入这两行代码试一试
des_caps['unicodekeyboard'] = True
des_caps['resetkeyboard'] = True  
driver = webdriver.Remote('http://localhost:4723/wd/hub',des_caps)
#隐式等待三秒
driver.implicitly_wait(3)

driver.find_element_by_xpath("//*[@bounds='[949,1812][1002,1865]']").click()
time.sleep(2)

#获取手机屏幕高和宽
def get_size():
    print(driver.get_window_size())

#swipe滑动
try:
    driver.swipe(300,1000,300,300,3000)
finally:
    time.sleep(3)
    driver.quit()

