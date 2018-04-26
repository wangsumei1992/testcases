#coding=utf-8
import sys, os
reload(sys)
sys.setdefaultencoding('utf-8')
import unittest
file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #这个abspath是写在第三层还是写在最里层
sys.path.append(file_path + "/login_po/pages")
#import BSTestRunner
from base_page import BasePage
from invest_xq import Invest_xqPage
from login_page import LoginPage
from invest_zf import InvestzfPage
from selenium import webdriver
import time

class TestInvestzt(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		self.driver = webdriver.Firefox()
		self.driver.maximize_window()
		#调用登录方法
		login_p = LoginPage(self.driver)
		login_p.login('15658524692', '15658524692')
		time.sleep(5)
		self.invest_p = Invest_xqPage(self.driver)
		self.zhifu_p = InvestzfPage(self.driver)

	def test1_zhitou(self):
		self.invest_p.open()
		time.sleep(3)
		balance1 = self.invest_p.balance_av().text
		time.sleep(3)
		balance_before = float(balance1.replace(',', ''))
		print(balance1.replace(',', ''))
		print(type(balance1.replace(',', '')))
		time.sleep(3)
		toubiao_p = self.invest_p.toubiao("100")
		time.sleep(3)
		#self.invest_p.invest_btn().click()
		#time.sleep(3)
		self.zhifu_p.zhifubtn()
		time.sleep(3)
		self.zhifu_p.huishang("123456")
		self.invest_p.open()
		time.sleep(3)
		balance2 = self.invest_p.balance_av().text
		balance_after = float(balance2.replace(',', '')) 
		print(balance_after)
		print(balance_before)
		self.assertEqual(100, balance_before-balance_after)

	def test2_less100(self):
		self.invest_p.toubiao('10')
		error_content = self.invest_p.error_text().text
		print (error_content)
		self.assertEqual(error_content, "认购金额至少 100.00 元。")

	def test3_send0(self):
		self.invest_p.toubiao('0')
		error_content = self.invest_p.error_text().text
		print (error_content)
		self.assertEqual(error_content, '投标金额必须大于0。')

	@classmethod
	def tearDownClass(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()
	#BSTestRunner.main()


		


