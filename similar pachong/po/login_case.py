#coding=utf-8
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

class LoginCase(unittest.TestCase):

	def setUp(self):
		self.dr = webdriver.Firefox()
		self.dr.get('http://139.199.192.100:8000/wp-login.php')

	def test_login_sucess(self):
		username = password = 'admin'
		login_page = LoginPage(self.dr)
		login_page.url = 'http://139.199.192.100:8000/wp-login.php'
		login_page.navigate()
		dashboard_page = login_page.login(username, password)

		#断言
		greeting_link = dashboard_page.greeting_link
		self.assertTrue(username in greeting_link.text)






