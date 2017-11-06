#coding=utf-8
import unittest
#import BSTestRunner
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time

class LoginCase(unittest.TestCase):
	def setUp(self):
		self.dr = webdriver.Firefox()
		self.dr.get('http://139.199.192.100:8000/wp-login.php')

	'''
	def test_login_success(self):
		username = password = 'admin'
		self.login(username, password)
		
		self.assertTrue('wp-admin' in self.dr.current_url)
		uuuu_name = self.by_css('#wp-admin-bar-my-account .ab-item')
		self.assertTrue(username in uuuu_name.text)

	#def test_create_post_success(self):
		username = password = 'admin'
		self.login(username, password)
		title = 'title %s' %(time.time())
		content = 'content %s' %(time.time())
		self.dr.get('http://139.199.192.100:8000/wp-admin/post-new.php')
		self.by_name('post_title').send_keys(title)
		self.set_content(content)
		self.by_id('publish').click()

		self.dr.get('http://139.199.192.100:8000/wp-admin/edit.php')
		first_title_text = self.by_css('.row-title').text
		self.assertEqual(first_title_text, title)
    '''
	def test_delete_post_success(self):
		username = password = 'admin'
		self.login(username, password)

		title = 'title %s' %(time.time())
		content = 'content %s' %(time.time())
		post_id = self.create_post_and_return_its_id(title, content)

		self.dr.get('http://139.199.192.100:8000/wp-admin/edit.php')
		row_id = 'post-' + post_id
		post = self.by_id(row_id)

		ActionChains(self.dr).move_to_element(post).perform()
		post.find_element_by_css_selector('.trash').click()

		with self.assertRaises(NoSuchElementException):
			self.by_id(row_id)

	def create_post(self, title, content):
		self.dr.get("http://139.199.192.100:8000/wp-admin/post-new.php")
		self.by_name('post_title').send_keys(title)
		self.set_content(content)
		self.by_id('publish').click()

	def create_post_and_return_its_id(self, title, content):
		self.create_post(title, content)
		tokens = self.by_id('sample-permalink').text.split('=')
		return tokens[-1]

	def set_content(self, content):
		js = "document.getElementById('content_ifr').contentWindow.document.body.innerHTML = '%s'" %(content)
		print(js)
		self.dr.execute_script(js)

	def login(self, username, password):
		self.by_id("user_login").send_keys(username)
		self.by_id("user_pass").send_keys(password)
		self.by_id("wp-submit").click()

	def by_id(self, the_id):
		return self.dr.find_element_by_id(the_id)

	def by_css(self, css):
		return self.dr.find_element_by_css_selector(css)

	def by_name(self, name):
		return self.dr.find_element_by_name(name)

	def tearDown(self):
		self.dr.quit()

if __name__ == '__main__':
	unittest.main()
	#BSTestRunner.main()
