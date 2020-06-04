#获取一组元素


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
#打开个人中心
driver.find_element_by_xpath("//*[@bounds='[942,1671][1002,1731]']").click()
time.sleep(2)

# #当前界面获取一组元素
# eles = driver.find_elements_by_class_name("android.widget.TextView")
# for ele in eles:
#     print(ele.text)


# 获取文案中有“客”的元素
eles = driver.find_elements_by_xpath("//*[contains(@text,'的')]")
print(len(eles))
for ele in eles:
    print(ele.text)

print(eles[2])

driver.quit()


