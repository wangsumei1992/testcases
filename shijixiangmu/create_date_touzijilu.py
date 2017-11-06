#coding=utf-8
from selenium import webdriver
import time
dr = webdriver.Chrome()
dr.maximize_window()
dr.get("http://mk-2.apengdai.com/user/login")
#登录
dr.find_element_by_id("userName").send_keys("13949124982")
dr.find_element_by_id("loginPass").send_keys("13949124982")
time.sleep(10)
dr.find_element_by_tag_name("button").click()
time.sleep(5)
#投资
i=0
while i<=10:
    print ("+++++++++++++++++++++="+str(i))
    dr.get("http://mk-2.apengdai.com/licai/12216")
    time.sleep(2)
    amount=100+i
    try:
        dr.find_element_by_id("amount").send_keys(amount)
        time.sleep(2)
        dr.get("http://mk-2.apengdai.com/licai/12216")
        time.sleep(2)
    except Exception as e:
        dr.get("http://mk-2.apengdai.com/licai/12216")
        time.sleep(2)
        dr.find_element_by_id("amount").send_keys(amount)
        time.sleep(2)
    dr.find_element_by_css_selector("input[type='submit']").click()
    time.sleep(3)
    js = "document.getElementsByClassName('affirm_qr_bt')[0].click()"
    dr.execute_script(js)
    time.sleep(5)
    dr.find_element_by_id("pass").send_keys("123456")
    time.sleep(2)
    dr.find_element_by_id("sub").click()
    i=i+1
    time.sleep(3)
