#coding=utf-8
from selenium import webdriver
import time
import unittest

class Login_error(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		self.dr = webdriver.Firefox()
		self.dr.get('http://139.199.192.100:8000/wp-login.php')
	
	def test_login_error1(self):#用户名正确，密码错误
		self.by_id("user_login").clear()
		self.by_id('user_login').send_keys('admin')
		self.by_id("user_pass").clear()
		self.by_id('user_pass').send_keys('123456')
		self.by_id('wp-submit').click()
		error_text = self.by_id("login_error").text
		print error_text
		self.assertTrue(u"为用户名admin指定的密码不正确" in error_text)


	def test_login_error2(self):#用户名错误，密码正确
		
		self.by_id("user_login").clear()
		self.by_id('user_login').send_keys('123456')
		self.by_id("user_pass").clear()
		self.by_id('user_pass').send_keys('admin')
		self.by_id('wp-submit').click()
		error_text = self.by_id("login_error").text
		print(error_text)
		self.assertTrue(u"无效用户名" in error_text)

	def test_login_error3(self):
		
		self.by_id("user_login").clear()
		self.by_id('user_login').send_keys('')
		self.by_id("user_pass").clear()
		self.by_id('user_pass').send_keys('admin')
		self.by_id('wp-submit').click()
		error_text = self.by_id("login_error").text
		self.assertTrue(u"用户名一栏为空" in error_text)
	
	def by_id(self, the_id):
		return self.dr.find_element_by_id(the_id)
	@classmethod
	def tearDownClass(self):
		self.dr.quit()

if __name__ == '__main__':

	#构造测试集
	suite = unittest.TestSuite()
	suite.addTest(Login_error("test_login_error1"))
	suite.addTest(Login_error("test_login_error2"))
	suite.addTest(Login_error("test_login_error3"))

	#执行测试
	runner = unittest.TextTestRunner()
	runner.run(suite)
