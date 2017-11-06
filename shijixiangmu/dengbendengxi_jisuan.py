#coding=utf-8
class DengBenXi:
    def __init__(self,acount,term,jiaxi=0,youhuiquan=0):
        self.acount=float(acount)
        self.term=term
        self.jiaxi=float(jiaxi)
        self.youhuiquan=float(youhuiquan)

    def changgui_biao(self):
        return ((self.acount/self.term)+self.acount*0.0048)

    def jiaxi_biao(self):
        return ((self.jiaxi/12)/1.9*self.acount)

    def jiangli(self):
        return self.youhuiquan/12/1.9*self.term*self.acount

    def yuqishouyi(self):
        return (self.changgui_biao()*self.term-self.acount)

    def jiaxi_yuqishouyi(self):
        return (self.jiaxi_biao()*24+self.yuqishouyi())
        

dengben=DengBenXi(15000,24,0.01,0)
print("加息标每月应返钱: "+str(dengben.jiaxi_biao()))
print ("每月还款额: "+str(dengben.changgui_biao()))
print ("使用加息券应返钱: "+str(dengben.jiangli()))
print ("常规标预期收益："+str(dengben.yuqishouyi()))
print ("加息标预期收益"+ str(dengben.jiaxi_yuqishouyi()))
