#coding=utf-8
from selenium import webdriver
import time

dr = webdriver.Chrome()
dr.maximize_window()
dr.get('https://www.apengdai.com/')
dr.find_element_by_link_text("登录").click()
time.sleep(2)
dr.find_element_by_id("userName").send_keys('wangsumei1992')
dr.find_element_by_id("loginPass").send_keys('41142519931028')
time.sleep(5)
dr.find_element_by_css_selector('.login_retext button').click()
time.sleep(2)
dr.get('https://www.apengdai.com/points/intGet')
time.sleep(3)
cishu = int(dr.find_element_by_css_selector('.pokTimes>span').text)

while cishu > 0:
	dr.find_element_by_css_selector('.pokDeal > img').click()
	time.sleep(3)
	dr.find_element_by_css_selector('.pokDraw > img').click()
	time.sleep(3)
	#dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[6]/div[4]/img').click()
	#dr.find_element_by_css_selector(".getGift>.delete>img").click()
	element=dr.find_element_by_css_selector(".getGift")
	button1 = element.find_element_by_css_selector(".delete").click()
	cishu = cishu-10

