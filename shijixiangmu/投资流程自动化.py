#coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://mk-2.apengdai.com/user/login")
driver.maximize_window()
time.sleep(2)
driver.find_element_by_xpath("//span[@class='login_reinput']/input").send_keys("15811507614")
driver.find_element_by_xpath("//input[@id='loginPass']").send_keys("15811507614")
time.sleep(10)
driver.find_element_by_tag_name('button').click()
#阿朋贷自动登录
time.sleep(3)
driver.get("http://mk-2.apengdai.com/project/list")
tzlb_window=driver.current_window_handle
driver.find_elements_by_link_text("投标")[2].click()
windows=driver.window_handles
time.sleep(6)
for handle in windows:
	if handle !=tzlb_window:
		driver.switch_to_window(handle)
		driver.find_element_by_id("amount").send_keys("100")
		driver.find_element_by_xpath("//input[@class='ft16 ztac-btn']").click()
		time.sleep(3)
		driver.find_element_by_tag_name("button").click()
time.sleep(5)
driver.find_element_by_id("J-payPwd_Savings").send_keys("wq15803863660")
driver.find_element_by_tag_name("button").click()
#前台投资自动化流程