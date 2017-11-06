class DengBenXi:
    def __init__(self,acount,term,lilu,jiaxi=0,youhuiquan=0):
        self.acount=float(acount)
        self.term=term
        self.lilu=float(lilu)
        self.jiaxi=float(jiaxi)
        self.youhuiquan=float(youhuiquan)

    def changgui_biao(self):
        return ((self.acount/self.term)+self.acount*0.0048)

    def jiaxi_biao(self):
        return ((self.jiaxi/12)/1.9*self.acount)

    def jiangli(self):
        return self.youhuiquan/12/1.9*self.term*self.acount
        

dengben=DengBenXi(600,6,0.09,0.03,0.01)
print(dengben.jiaxi_biao())
print (dengben.changgui_biao())
print (dengben.jiangli())
dengben1=DengBenXi(1400,6,0.09,0.03)
print("-------------------------------------")
print(dengben1.jiaxi_biao())
print (dengben1.changgui_biao())
print (dengben1.jiangli())
        
class DengBenXi:
    def __init__(self,acount,term,lilu,jiaxi=0,youhuiquan=0):
        self.acount=float(acount)
        self.term=term
        self.lilu=float(lilu)
        self.jiaxi=float(jiaxi)
        self.youhuiquan=float(youhuiquan)

    def changgui_biao(self):
        return ((self.acount/self.term)+self.acount*0.0048)

    def jiaxi_biao(self):
        return ((self.jiaxi/12)/1.9*self.acount)

    def jiangli(self):
        return self.youhuiquan/12/1.9*self.term*self.acount
        

dengben=DengBenXi(500,12,0.09,0.1,0.01)
print(dengben.jiaxi_biao())
print (dengben.changgui_biao())
print (dengben.jiangli())
dengben1=DengBenXi(1400,6,0.09,0.03)
print("-------------------------------------")
print(dengben1.jiaxi_biao())
print (dengben1.changgui_biao())
print (dengben1.jiangli())
        
