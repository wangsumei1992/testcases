#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import HTMLTestRunner
import unittest
import time,os

def send_mail(file_new):
	#发送邮箱
	mail_from = 'wsm3120380093@126.com'
	#收信邮箱
	mail_to = '3120380093@qq.com'
	f = open(file_new, 'rb')
	mail_body = f.read()
	f.close()
	msg=MIMEText(mail_body,_subtype='html',_charset='utf-8')
	msg['Subject'] = u'自动化测试报告'

	#四个类似步骤
	smtp = smtplib.SMTP()
	smtp.connect('smtp.126.com')
	smtp.login('wsm3120380093@126.com','41142519931028')
	smtp.sendmail(mail_from,mail_to,msg.as_string)
	smtp.quit()
	print('mail has sent out!')

def send_report(testreport):
	result_dir = testreport
	lists=os.listdir(result_dir)
	list.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn))
	#print (u'最新测试生成的报告: '+lists[-1])
	#找到最新生成的文件
	file_new = os.path.join(result_dir,lists[-1])
	print (file_new)
	#定义发送邮件
	send_mail(file_new)

#=========将用例添加到测试套件========
def creatsuite():
	testunit=unittest.TestSuite()
	#定义测试文件查找的目录
	test_dir='.\\test_case'
	#定义discover方法的参数
	discover=unittest.defaultTestLoader.discover(test_dir,pattern='invests*.py',top_level_dir=None)
	#discover方法筛选出来的用例，循环添加到测试套件中
	for test_case in discover:
		print test_case
		testunit.addTests(test_case)
	return testunit

if __name__ == '__main__':
	testreport = 'F:/python01/shijixiangmu/apd_lianxi/login_po'
	filename = testreport+'wsm.html'
	fp = file(filename, 'wb')
	runner = HTMLTestRunner.HTMLTestRunner(
		stream=fp,
		title=u'自动化测试报告',
		description=u'用例执行情况: ')

	alltestnames = createsuite()
	runner.run(alltestnames)
	fp.close() #关闭生成的报告
	send_report(testreport) #发送报告