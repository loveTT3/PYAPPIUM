#定位一个元素


from appium import webdriver
import time

des_caps = dict()
des_caps['platformName'] = 'android'
des_caps['platformVersion'] = '7'
des_caps['deviceName'] = '1'
des_caps['noReset'] = 'true'
des_caps['appPackage'] = 'com.zhisland.android.blog'
des_caps['appActivity'] = '.aa.controller.SplashActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub',des_caps)


time.sleep(2)
#打开邻里
driver.find_element_by_xpath("//*[@bounds='[276,1671][336,1731]']").click()
time.sleep(2)

'''定位一个元素'''
#发表feed
driver.find_element_by_xpath("//*[@bounds='[936,144][1008,216]']").click()
time.sleep(1)
driver.find_element_by_class_name("android.widget.EditText").send_keys("hello")
time.sleep(1)
driver.find_element_by_xpath("//*[@text='发布']").click()
time.sleep(2)


driver.quit()