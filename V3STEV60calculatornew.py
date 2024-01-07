from baselinecalculator import baselinecalculator
import numpy as np
class V3STEV60calculatornew:
    #import 2 arrays and 1 parameter
    def __init__(self, newECGarr10000, Timeindexlist, halfQRSDuration):
        self.newECGarr10000 = newECGarr10000
        self.Timeindexlist = Timeindexlist
        self.halfQRSDuration = halfQRSDuration
        
    def V3QRS10000(self):
        #把VPClist建立出來
        
        
        #在5秒和6秒之間找到一個QRSwave的位置 分成一秒內有一個波 兩個波 兩個波以上的情況
        #因為波要是完整的 所以要五秒+QRSduration, 6秒-QRSduration 
        #一個波：除非是VPC 不然直接用
        #兩個波：用第二個波
        #三個波以上：用第二個波
        timelist = []
        for time in self.Timeindexlist:
            if int(time)>(2500+(int(self.halfQRSDuration)*2)) and int(time)<(3000-(int(self.halfQRSDuration)*2)):
                timelist.append(int(time))
        print(timelist)
        print("timelistlength="+str(len(timelist)))        
        
        if len(timelist) == 1:
            QRSwavelocation = timelist[0]
            
        elif len(timelist) == 0:
            shortlist = []
            for Time in self.Timeindexlist:
                if Time>(2500+int(self.halfQRSDuration)*2):
                    shortlist.append((Time))
            QRSwavelocation = shortlist[0]        
        
        else:
            QRSwavelocation = timelist[1]
        
        a = self.Timeindexlist.index(QRSwavelocation)
        
             
        #需要一個QRSwave的位置傳進來
        QRSwavelist = []
        #從V3起始點一路算到越過QRSwave那一點 在過到一半的Duration內的最低點 會是S波
        for value in range(QRSwavelocation-self.halfQRSDuration*2, QRSwavelocation+self.halfQRSDuration*2,1):
            QRSvalue = self.newECGarr10000[value]
            QRSwavelist.append(QRSvalue)
        
        Svalue = min(QRSwavelist)
        
        Slocation = QRSwavelist.index(Svalue)+QRSwavelocation-self.halfQRSDuration*2
        
        
        #S點找到之後 開始處理J點
        
        #開始求Jpoint
        tengentlist=[]#準備裝連續的割線斜率
        
        for a in range(Slocation,(Slocation+self.halfQRSDuration*2),5):#從S點開始每五個點取一條割線斜率 放到tengentlist中
    
            tengent5=(self.newECGarr10000[a+5]-self.newECGarr10000[a])/5
            tengentlist.append(tengent5)

        Stengent=tengentlist[0]#以頭五個點所形成的割線斜率作為S波的基準斜率

        counter=0
        while tengentlist[counter]>(max(tengentlist)/5):#當下一條割線斜率出現了巨大轉折時(此時是小於基準斜率的1/10)把counter提出來 當作Jpoint 我用1/10當作cutoff 有可能會再做更改
            counter=counter+1
        
        Jpointvalue=self.newECGarr10000[Slocation+counter*5-2]#找到那條變化巨大的割線終點
        Jpointlocation=Slocation+counter*5-2
       
        #把J60點高度求出來
        J60pointlocation=Jpointlocation+30#每2ms取一個點 60ms後就是+30個點
        J60pointvalue=self.newECGarr10000[J60pointlocation]
        
        #求得baseline高度
        V3b=baselinecalculator(self.newECGarr10000, QRSwavelocation)
        V3baseline=V3b.baseline()
        
        #J60-baseline就是抬升高度
        STEV60=J60pointvalue-V3baseline
        print("STEV60 = " +str(STEV60))
        print()
        return STEV60
        