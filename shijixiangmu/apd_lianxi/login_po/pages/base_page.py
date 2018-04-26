class BasePage(object):
	base_url = "http://mk-2.apengdai.com/"
	
	def __init__(self, driver, domain=base_url):
		self.driver = driver
		self.domain = domain

	def _open(self, url):
		url = self.domain+self.url
		self.driver.get(url)

	def open(self):
		self._open(self.url)

	def by_id(self, the_id):
		return self.driver.find_element_by_id(the_id)

	def by_name(self, the_name):
		return self.driver.find_element_by_name(the_name)

	def by_css(self, css):
		return self.driver.find_element_by_css_selector(css)

	def by_tag_name(self, tagname):
		return self.driver.find_element_by_tag_name(tagname)

	def js(self, js_text):
		return self.driver.execute_script(js_text)

	

