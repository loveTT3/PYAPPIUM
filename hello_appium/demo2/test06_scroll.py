
#屏幕拖拽，滑动



from appium import webdriver
import time
des_caps = dict()
des_caps['platformName'] = 'android'
des_caps['platformVersion'] = '7'
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


driver.find_element_by_xpath("//*[@bounds='[933,1671][993,1731]']").click()
before_botton = driver.find_element_by_xpath("//*[@text='访问过我的人']")
after_botton = driver.find_element_by_xpath("//*[@text='我的社群']")
time.sleep(1)


# driver.scroll(after_botton,before_botton)
driver.drag_and_drop(after_botton,before_botton)

time.sleep(2)
driver.quit()

