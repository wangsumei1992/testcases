'''
class Dog:
    age = 0
    def dog1(self):
        age = self.age + 1
        print(self.age)

    def dog2(self):
        age = self.age + 1
        print(self.age)

d = Dog()
d.dog1()
d.dog2()
str = '42,031.09'
a = str.replace(',', '')
print a
import os,sys
path = 'F:/python01/shijixiangmu/apd_lianxi/login_po'
dirs = os.listdir(path)

for file in dirs:
	print file
'''
