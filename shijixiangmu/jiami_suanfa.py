



class JiaMi():
    def __init__(self,a,b,c,d):
       self.a=a
       self.b=b
       self.c=c
       self.d=d
    #投资人用户标识修改加密算法
    def user_change(self):
        return self.b*self.b+self.a*self.a+self.d+self.c*self.c*self.c
    #批量划扣加密算法
    def pilianghuangkou(self):
        return self.b*self.b-self.a*self.a+self.d-self.c
    #提前还款加密算法
    def tiqianhuankuan(self):
        return self.b*self.b+self.a*self.a+self.d+self.c
    #冻结账户加密算法
    def dongjiezhanghu(self):
        return self.b*self.b-self.a*self.a+self.d-self.c*self.c
    #解结账户加密算法
    def jiedong(self):
        return self.b*self.b-self.a*self.a+self.d+self.c*self.c
    #发红包加密算法
    def fahongbao(self):
        return (self.a*self.b+self.c+self.d)*self.b*self.d

wq = JiaMi(9,2,6,1)
print (wq.fahongbao())
