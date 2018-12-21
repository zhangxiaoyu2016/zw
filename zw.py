import time

from selenium import webdriver

from selenium.webdriver.support.ui import Select

username = "用户名"

password = "密码"

driver=webdriver.Chrome()# 选择Chrome浏览器

driver.get('http://a.nuist.edu.cn')# 打开i-nuist

time.sleep(3)

driver.find_element_by_id('username').click()# 点击用户名输入框

driver.find_element_by_id('username').send_keys(username) # 自动输入用户名

selector = Select(driver.find_element_by_id("domain")) # 实例化Select类的对象

selector.select_by_value("CMCC") #选择接入用户类型

driver.find_element_by_id('password').click()# 点击密码输入框

driver.find_element_by_id('password').send_keys(password) # 自动输入密码

driver.find_element_by_id('login').click() # 点击“登录”按钮

time.sleep(3)

driver.close()
