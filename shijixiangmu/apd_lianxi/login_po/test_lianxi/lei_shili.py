#coding:utf-8
class Student(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def print_a(self):
        print("展示self的用处")
        return self

    def print_text(self):
        print(self.name)
        print(self.sex)

if __name__ == '__main__':
    stu1 = Student('lilei', 'boy')
    stu1.print_a().print_text()

    stu2 = Student('hanmeimei', 'girl')
    stu2.print_text()