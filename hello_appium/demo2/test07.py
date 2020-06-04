from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction
import appium

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


#找到需要点击的元素
ele = driver.find_element_by_xpath("//*[@bounds='[270,1671][330,1731]']")
'''
#创建对象
ta = TouchAction(driver)
#轻敲动作
#ta.tap(ele)
ta.tap(x=271,y=1672)
#执行所有操作
ta.perform()
'''


#快速按下，抬起,相当于轻敲
'''
TouchAction(driver).press(x=271,y=1731).release().perform()
'''

'''
TouchAction(driver).press(x=271,y=1731).release().perform()  #打开邻里
time.sleep(2)
TouchAction(driver).press(x=73,y=850).release().perform()   #打开第一个的详情
time.sleep(2)
#等待，按下等待再抬起   相当于长按再抬起
TouchAction(driver).press(x=503,y=857).wait(2000).release().perform()  
'''

'''
#跳转设置->Wlan
driver.start_activity('com.android.settings','.Settings$WifiSettingsActivity')
TouchAction(driver).press(x=260,y=700).wait(2000).release().perform()  
# TouchAction(driver).long_press(x=260,y=700,duration=3000).perform()
print(driver.current_activity)
'''





#长按操作
TouchAction(driver).press(x=271,y=1731).release().perform()  #打开邻里
time.sleep(2)
TouchAction(driver).press(x=73,y=850).release().perform()   #打开第一个的详情
time.sleep(2)
TouchAction(driver).long_press(x=503,y=857,duration=3000).perform()  #长按





time.sleep(4)
driver.quit()

