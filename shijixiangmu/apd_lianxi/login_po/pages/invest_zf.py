#coding=utf-8
from base_page import BasePage
import time

class InvestzfPage(BasePage):

	def zhifubtn(self):
		return self.by_css(".dis-ib>button[name='btn_send_m_code']").click()

		#js = "document.getElementsByClassName('affirm_qr_bt')[0].click()"
		#self.driver.execute_script(js)  

	def huishang(self, password):
		self.by_id("pass").send_keys(password)
		time.sleep(5)
		self.by_id("sub").click()
