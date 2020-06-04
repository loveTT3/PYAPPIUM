#元素等待
from appium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait


des_caps = dict()
des_caps['platformName'] = 'android'
des_caps['platformVersion'] = '6'
des_caps['deviceName'] = '1'
des_caps['noReset'] = 'true'
des_caps['appPackage'] = 'com.zhisland.android.blog'
des_caps['appActivity'] = '.aa.controller.SplashActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub',des_caps)

driver.find_element_by_xpath("//*[@bounds='[949,1812][1002,1865]']").click()



# #隐式等待，单位秒,所有获取元素都等待
# driver.implicitly_wait(4)
# print('----寻找元素点击----')
# driver.find_element_by_xpath("//*[@bounds='[954,126][1017,189]']").click()
# print('----点击完成----')
# time.sleep(4)



print('----寻找元素点击----')
#显式等待
wait = WebDriverWait(driver,10)
#调用一个until方法，然后点击
wait.until(lambda x : x.find_element_by_xpath("//*[@bounds='[954,126][1017,189]']")).click()
print('----点击完成----')



driver.quit()











