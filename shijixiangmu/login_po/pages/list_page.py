#coding=utf-8
import sys, os
from base_page import BasePage
class ListPage(BasePage):
	def list_page(self):
		self.url = "http://mk-2.apengdai.com/licai/"
		self.by_css(".clearfix b-r > a").click()
		return biaodixiangqingye 

	biaodixiangqingye :
	# 这个页面怎样写
