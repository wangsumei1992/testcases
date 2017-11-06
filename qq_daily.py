#coding=utf-8
from selenium import webdriver
import time

class QQDailyHot:
	def __init__(self):
		self.dr = webdriver.Firefox()
		self.title, self.content = self.get_title_and_content_from_daily_hot()

	def get_daily_hot_url(self):
		return self.by_css("#todaytop a").get_attribute('href')
        
	def get_title_and_content_from_daily_hot(self):
		self.dr.get('http://www.qq.com/')
		url = self.get_daily_hot_url()
		print url
		self.dr.get(url)
		time.sleep(3)
		title = self.by_id("sharetitle").text
		time.sleep(3)
		content = self.by_id("articleContent").get_attribute('innerHTML')
		return (title, content)

	def quit(self):
		self.dr.quit()

	def create_from_daily_hot(self):
		self.dr.get('http://139.199.192.100:8000/wp-login.php')
		self.login_as_admin()

		self.dr.get('http://139.199.192.100:8000/wp-admin/post-new.php')
		self.by_id('title').send_keys(self.title)
		time.sleep(3)
		self.set_content(self.content)
		time.sleep(5)
		self.by_id('publish').click()

	def set_content(self, text):
		text = text.strip()
		js = 'document.getElementById("content_ifr").contentWindow.document.body.innerHTML= \'%s\'' %(text)
		print js
		self.dr.execute_script(js)

	def login(self, username, password):
		self.by_id('user_login').send_keys(username)
		self.by_id('user_pass').send_keys(password)
		self.by_id('wp-submit').click()
	def login_as_admin(self):
		username = password = 'admin'
		self.login(username, password)
	def by_id(self, the_id):
		return self.dr.find_element_by_id(the_id)
	def by_css(self, css):
		return self.dr.find_element_by_css_selector(css)
	def by_name(self, name):
		return self.dr.find_element_by_name(name)

if __name__ == '__main__':
	qq_daily = QQDailyHot()
	qq_daily.create_from_daily_hot()
	qq_daily.quit()
