#coding=utf-8
import sys, os
file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(file_path)
sys.path.append(file_path + "/login_po/pages")
from login_page import LoginPage
from account import AccountPage
import unittest, time
from selenium import webdriver

class LoginTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.maximize_window()
		self.login_p = LoginPage(self.driver)
	def test_login_success(self):
		username = password = '15558524693' 
		mylogin = self.login_p.login(username, password)
		time.sleep(5)
		assert_text = mylogin.login_successfield().text      
		print(assert_text)
		self.assertEqual(u'账户总览', assert_text, msg="======")

if __name__ == '__main__':
	unittest.main()





