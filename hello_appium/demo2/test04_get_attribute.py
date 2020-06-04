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

'''发feed'''
# driver.find_element_by_xpath("//*[@bounds='[285,1812][338,1865]']").click()
# driver.find_element_by_xpath("//*[@bounds='[954,126][1017,189]']").click()
# input_text = driver.find_element_by_id('com.zhisland.android.blog:id/etFeed')
# input_text.send_keys('haha')
# input_text.clear()
# input_text.send_keys('你好')
# driver.find_element_by_xpath("//*[@bounds='[913,68][1075,184]']").click()

'''获取文本内容'''
# driver.find_element_by_xpath("//*[@bounds='[949,1812][1002,1865]']").click()
# eles = driver.find_elements_by_class_name('android.widget.TextView')
# for ele in eles:
#     print(ele.text)

'''获得元素的位置和大小'''
# driver.find_element_by_xpath("//*[@bounds='[285,1812][338,1865]']").click()
# search_botton = driver.find_element_by_id('com.zhisland.android.blog:id/ivTitleIcon')
# #输出是字典
# print(search_botton.location)
# print(search_botton.location['x'])
# print(search_botton.location['y'])
# print(search_botton.size)
# print(search_botton.size['height'])
# print(search_botton.size['width'])

'''获取元素属性值'''
# driver.find_element_by_xpath("//*[@bounds='[285,1812][338,1865]']").click()
# driver.find_element_by_xpath("//*[@bounds='[954,126][1017,189]']").click()
# ele = driver.find_element_by_xpath("//*[@bounds='[913,68][1075,184]']")
# print(ele.get_attribute('clickable'))


ele = driver.find_element_by_id('com.zhisland.android.blog:id/tvTodayRank')
print(ele.get_attribute('text'))
print(ele.get_attribute('resourceId'))
print(ele.get_attribute('className'))
print(ele.get_attribute('name'))






time.sleep(2)
driver.quit()
