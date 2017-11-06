#coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://mm-2.apengdai.com")
driver.find_element_by_id("UserName").send_keys("caihongguang")
driver.find_element_by_id("UserPass").send_keys("789654")
time.sleep(10)
driver.find_element_by_tag_name("button").click()
driver.get("http://mm-2.apengdai.com/loan/project/create")
driver.find_element_by_id("projectName").send_keys("zhitou")#项目名称
wsm=driver.find_element_by_id("projectCategory")#首先定位下拉框 上线项目分类
wsm.find_element_by_css_selector("option[value='PersonalCredit']").click()#其次定位下拉框中选择项  选择“信易融”
a=driver.find_element_by_id("projectNewType")
a.find_element_by_css_selector("option[value='DirectInvestment']").click()#项目类型选择为“直投”
driver.find_element_by_id("contractID").send_keys(123456)
driver.find_element_by_id("contractFullID").send_keys("1111111")
b=driver.find_element_by_name("contractType")
b.find_element_by_css_selector("option[value='10000']").click() #合同类型选择为投资居间服务协议
driver.find_element_by_id("loanContract").send_keys("1111111")
c=driver.find_element_by_id("address")
c.find_element_by_css_selector("option[value='BEIJING']").click() #选择丁方为“北京”
time.sleep(6)
driver.find_element_by_id("contractID").send_keys("888888")
#投资规则
driver.find_element_by_id("minBidAmount").clear()
driver.find_element_by_id("minBidAmount").send_keys(100)
d=driver.find_element_by_id("repaymentCalcType")
d.find_element_by_css_selector("option[value='OneInterestOnePrincipal']").click()#下拉框选择还款方式
driver.find_element_by_id("interestRatePercent").clear()
driver.find_element_by_id("interestRatePercent").send_keys('12')
driver.find_element_by_id("financingMaturity").clear()
driver.find_element_by_id("financingMaturity").send_keys('1') #融资期限
driver.find_element_by_id("amount").clear()
driver.find_element_by_id("amount").send_keys("1000")
time.sleep(20)
driver.find_element_by_id("userName").send_keys("w1694959")
driver.find_element_by_id("btnLoadUser").click()
time.sleep(3)
driver.find_element_by_id("purpose").send_keys(u"临时周转")
driver.find_element_by_id("projectDescription").send_keys(u"项目借款人资质良好")
driver.find_element_by_id("apdUserName").send_keys("11")
driver.find_element_by_id("firstAddress").send_keys("11")
driver.find_element_by_id("bankName").send_keys("11")
driver.find_element_by_id("bankAccountNumber").send_keys("11")
driver.find_element_by_id("bankAccount").send_keys(u"建设银行")
driver.find_element_by_id("signAddr").send_keys(u"北京市朝阳区")
time.sleep(10)
driver.find_element_by_id("saveLoanBtn").click()
