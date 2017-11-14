#coding=utf-8
from base_page import BasePage
class AccountPage(BasePage):
	def login_successfield(self):
		return self.by_css("li.subNav>a")
