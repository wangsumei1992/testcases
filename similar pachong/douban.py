#coding=utf-8
"""
获取豆瓣电影及读书中的内容
"""
from selenium import webdriver
import time
import os

class Douban:

	def __init__(self):
		self.movie_url = 'https://movie.douban.com/cinema/nowplaying/beijing/'
		self.book_url = 'https://book.douban.com/'

	def __enter__(self):
		self.dr = webdriver.Firefox()
		return self

	def __exit__(self,exc_type,exc_value,traceback):
		self.dr.quit()

	def get_current_movies(self):
		def by_rate(dic):
			return float(dic['rate'])

		self.dr.get(self.movie_url)
		time.sleep(3)
		self.dr.save_screenshot('douban.jpg')
		wrap_div = self.dr.find_element_by_id('nowplaying')
		cards = wrap_div.find_elements_by_class_name('list-item')
		movies = []
		for card in cards:
			item = {}
			item['name'] = card.find_element_by_css_selector('.stitle a').get_attribute('title')
			item['rate'] = card.find_element_by_css_selector('.subject-rate').text
			if item['name'] and item['rate']:
				movies.append(item)

		return sorted(movies, key=by_rate, reverse=True)

	def get_hot_books(self):
		def by_rate(dic):
			return float(dic['rate'])

		self.dr.get(self.book_url)
		wrap_div = self.find_element_by_css_selector('.section books-express')
		cards = wrap_div.find_elements_by_tag_name('li')
		books = []
		for card in cards:
			item = {}
			item['name'] = card.find_element_by_css_selector('h4.title').text
			item['rate'] = card.find_element_by_css_selector('.average-rating').text
			item['author'] = card.find_element_by_css_selector('p.author').text
			if item['name'] and item['rate']:
				books.append(item)

		return sorted(books, key=by_rate, reverse=True)

if __name__ == '__main__':
	with Douban() as douban:
		movies = douban.get_current_movies
		books = douban.get_hot_books
