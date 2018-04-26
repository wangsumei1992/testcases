#coding=utf-8
from base_page import BasePage
from invest_zf import InvestzfPage
import time

class Invest_xqPage(BasePage):
	url = "/licai/12607"

	def money_send(self):
		return self.by_id('amount')

	def invest_btn(self):
		return self.by_css("input[type='submit']") 

	def queren(self):
		return self.by_id("okcp")

	def toubiao(self, money):
		self.open() 
		time.sleep(5)
		self.money_send().send_keys(money)   #money_send()中需不需要传参数
		self.invest_btn().click()
		self.queren().click()
		time.sleep(3)  
		return InvestzfPage(self.driver)

	def error_text(self):
		return self.by_css(".alert-error>ul>li")

	#def error_ajax(self):  #作用是什么？
        #return self.By_id("error-tip")

	def balance_av(self):
		return self.by_css("p[id='zhanghu']>span")
		





