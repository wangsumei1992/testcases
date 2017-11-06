from selenium import webdriver
#import selenium.webdriver
import unittest
import time,sys
sys.path.append("E:\\project_python\\apengdai\\public")
import login
class Choujf(unittest.TestCase):
	def setUp(self):
		self.dr=webdriver.Chrome()
		self.dr.implicitly_wait(10)
	def test_choujf(self):
		#调用登录模块
		login.login(self)
		self.dr.find_element_by_link_text("积分商城").click()
		self.dr.find_element_by_xpath("//div[@class='header']//a").click()
		cishu=int(self.dr.find_element_by_xpath("//div[@class='pokTimes landAfter']//span").text

		while cishu>0:
			self.dr.find_element_by_xpath("//div[@class='pokDeal']/img").click()
			time.sleep(5)
			self.dr.find_element_by_xpath("//div[@class='pokDraw']/img").click()
			time.sleep(5)
			self.dr.find_element_by_xpath("/html/body/div[3]/div[1]/div[6]/div[4]/img").click()
 			cishu=cishu-10
	def tearDown(self):
		self.dr.quit()
if __name__ == '__main__':
	suit=unittest.TestSuite()
	suit.addTest(Choujf("test_choujf"))
	runner=unittest.TextTestRunner()
	runner.run(suit)
