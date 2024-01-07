from baselinecalculator import baselinecalculator
import numpy as np
class V4Rwavecalculatornew0712update:
    #import 2 arrays and 1 parameter
    def __init__(self, newECGarr10000, Timeindexlist, halfQRSDuration):
        self.newECGarr10000 = newECGarr10000
        self.Timeindexlist = Timeindexlist
        self.halfQRSDuration = halfQRSDuration
        
    def V4QRS10000(self):
        #把VPClist建立出來
        #在5秒和6秒之間找到一個QRSwave的位置 分成一秒內有一個波 兩個波 兩個波以上的情況
        #因為波要是完整的 所以要五秒+QRSduration, 6秒-QRSduration 
        #一個波：除非是VPC 不然直接用
        #兩個波：用第二個波
        #三個波以上：用第二個波
        timelist = []
        for time in self.Timeindexlist:
            if int(time)>(3750+(int(self.halfQRSDuration)*2)) and int(time)<(4250-(int(self.halfQRSDuration)*2)):
                timelist.append(int(time))
        print(timelist)
        print("timelistlength="+str(len(timelist)))        
        
        if len(timelist) == 1:
            QRSwavelocation = timelist[0]
            
        elif len(timelist) == 0:
            shortlist = []
            for Time in self.Timeindexlist:
                if Time>(3750+int(self.halfQRSDuration)*2):
                    shortlist.append((Time))
            QRSwavelocation = shortlist[0]        
        
        else:
            QRSwavelocation = timelist[1]
        
        a = self.Timeindexlist.index(QRSwavelocation)
        
        
        #找QRS位置前一個QRSduration中的最高點
        fronthightestlist = []
        #從V4起始點一路算到越過QRSwave那一點 在過到一半的Duration內的最低點 會是S波
        for value in range(QRSwavelocation-self.halfQRSDuration*2, QRSwavelocation, 1):
            QRSvalue = self.newECGarr10000[value]
            fronthightestlist.append(QRSvalue)
        
        Rwavecandidate1 = max(fronthightestlist)
        
        
        
        #找QRS位置後一個QRSduration中的最高點
        backhightestlist = []
        #從V4起始點一路算到越過QRSwave那一點 在過到一半的Duration內的最低點 會是S波
        for value in range(QRSwavelocation, QRSwavelocation+self.halfQRSDuration*2, 1):
            QRSvalue = self.newECGarr10000[value]
            backhightestlist.append(QRSvalue)
        
        Rwavecandidate2 = max(backhightestlist)
        
        if Rwavecandidate1 > Rwavecandidate2:
            Rwavevalue = Rwavecandidate1
            Rwavelocation = fronthightestlist.index(Rwavevalue)+QRSwavelocation-self.halfQRSDuration*2
        elif Rwavecandidate1 == Rwavecandidate2:
            Rwavevalue = Rwavecandidate1
            Rwavelocation = fronthightestlist.index(Rwavevalue)+QRSwavelocation-self.halfQRSDuration*2
        else:
            Rwavevalue = Rwavecandidate2       
            Rwavelocation = backhightestlist.index(Rwavevalue) + QRSwavelocation 
    
        #求得baseline高度
        V4b=baselinecalculator(self.newECGarr10000, QRSwavelocation)
        V4baseline=V4b.baseline()
        
        #求RV4量值
        RV4 = Rwavevalue - V4baseline
        print("RV4 = "+str(RV4))
        print()
        return RV4, Rwavelocation
        