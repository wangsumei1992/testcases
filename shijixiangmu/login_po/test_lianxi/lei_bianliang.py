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
