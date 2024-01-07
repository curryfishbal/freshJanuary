from baselinecalculator import baselinecalculator
import numpy as np

class V2QRScalculatornew:
    #import 2 arrays and 1 parameter
    def __init__(self, newECGarr10000, Timeindexlist, halfQRSDuration):
        self.newECGarr10000 = newECGarr10000
        self.Timeindexlist = Timeindexlist
        self.halfQRSDuration = halfQRSDuration
        
    def V2QRS10000(self):
    
        
        #在5秒和6秒之間找到一個QRSwave的位置 分成一秒內有一個波 兩個波 兩個波以上的情況
        #因為波要是完整的 所以要五秒+QRSduration, 6秒-QRSduration 
        #一個波：除非是VPC 不然直接用
        #兩個波：用第二個波
        #三個波以上：用第二個波
        timelist = []
        for time in self.Timeindexlist:
            if int(time)>(2500+(int(self.halfQRSDuration)*2)) and int(time)<(3000-(int(self.halfQRSDuration)*2)):
                timelist.append(int(time))
              
        
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
        #從V2起始點一路算到越過QRSwave那一點 在過到一半的Duration內的最低點 會是S波
        for value in range(QRSwavelocation-self.halfQRSDuration*2, QRSwavelocation+self.halfQRSDuration*2,1):
            QRSvalue = self.newECGarr10000[value]
            QRSwavelist.append(QRSvalue)
        
        Svalue = min(QRSwavelist)
        
        Slocation = QRSwavelist.index(Svalue)+QRSwavelocation-self.halfQRSDuration*2
        
        
        Rwavecandidatelist=[]
        #往前一個QRSduration的範圍內找R波
        for i in range(Slocation,Slocation-self.halfQRSDuration*2,-1):
            Rwavecandidate=self.newECGarr10000[i]
            Rwavecandidatelist.append(Rwavecandidate)
            i=i-1
        Rwavevalue=max(Rwavecandidatelist)
        
        Rwavelocation=Slocation-Rwavecandidatelist.index(Rwavevalue)
        
         #兩者相減即為QRS量值 
        QRSV2=Rwavevalue-Svalue
        print("QRSV2 = "+str(QRSV2))
        print()
        return QRSV2, Rwavelocation
        