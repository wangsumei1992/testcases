from selenium import webdriver
import os

def shot_image(driver,image_name):
	base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	#这里获取的是谁的路径，自己的测试报告路径为 file:///F:/python01/shijixiangmu/apd_lianxi/login_po/wsm.html
	file_path = base_dir + '/report/screenshot_image/' + image_name
	print (file_path)
	driver.get_screenshot_as_file(file_path)

if __name__ == '__main__':
	driver = webdiver.Firefox()
	driver.get('http://www.baidu.com') #此处url是需要截图的报告的地址吗？
	shot_image(driver,"baidu.jpg")
	driver.quit()