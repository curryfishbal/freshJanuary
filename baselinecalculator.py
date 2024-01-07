
import numpy as np 
class baselinecalculator:
    def __init__(self, newECGarr, QRSwavelocation):
        self.newECGarr = newECGarr
        self.QRSwavelocation = QRSwavelocation
    #計算baseline需要兩個變數 ECG波形以及要算baseline的那一個點 然後取其前面200個點(0.4秒內 應該可以包含到PR interval)來統計最逼近baseline的位置
    def baseline(self):
        counterlist=[]
        for height in range(60,-60,-1):
            counter=0
            
            if self.QRSwavelocation<50:
                for i in range(0,self.QRSwavelocation,1):
                    k = self.newECGarr[i]
        
                    a = (height/2) - k
                    b = abs(a)
                    if b<0.25:
                        counter = counter+1
                counterlist.append(counter)     
            
            else:
                for i in range(self.QRSwavelocation-50,self.QRSwavelocation,1):
                    k = self.newECGarr[i]
            
                    a = (height/2) - k
                    b = abs(a)
                    if b<0.25:
                        counter = counter+1
                counterlist.append(counter)            
            
    
          

        maxvalue=max(counterlist)#此數值為list中的編號29 但因為list從0開始算 所以u    
        baselinevalue=(30-(counterlist.index(maxvalue)/2))
       
        return baselinevalue