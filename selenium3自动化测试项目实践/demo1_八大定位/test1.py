from  selenium import webdriver

# 获取驱动对象
driver = webdriver.Chrome()

# 打开百度
driver.get('https://www.baidu.com')

# 通过id定位
# driver.find_element_by_id('kw').send_keys('python')

# 通过name定位，需保证name值唯一
# driver.find_element_by_name('wd').send_keys('python')

# 通过class_name定位
# driver.find_element_by_class_name('s_ipt').send_keys('python')

# 通过link_text定位,通过超链接的文字，文字需要写全
# driver.find_element_by_link_text('新闻').click()

# 通过partial_link_text定位  模糊查询
# driver.find_element_by_partial_link_text('新').click()
 
# css定位
# driver.find_element_by_css_selector('.s_ipt').send_keys('python')
driver.find_element_by_css_selector('#kw').send_keys('python')