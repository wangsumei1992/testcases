#coding=utf-8
import time
from base_page import BasePage

class LoginPage(BasePage):
	url = "user/login"

	@property
	def username_text(self):
		return self.by_id("userName")

	@property 
	def password_text(self):
		return self.by_id("loginPass")

	@property 
	def button_text(self):
		return self.by_css(".ft14 login_reinput_bu cfff w332 dis_b")

	def login(self, username, password):
		self.open()
		self.username_text.send_keys(username)
		self.password_text.send_keys(password)
		time.sleep(5)
		self.button_text.click()
		return AccountPage(self.driver) #这里为什么传driver
		
