import array
import xml.etree.ElementTree as ET 
import base64
import struct
import matplotlib.pyplot as plt

class readdata10000:
    def  __init__(self,path):
        self.path=path

    def V2data10000(self):
        tree=ET.parse(self.path)  
        root=tree.getroot()
        for LeadData in root.iter('LeadData'):#在所有LeadData包含的內容中
            LeadID=LeadData.find('LeadID').text#尋找LeadID內的text
            if(LeadID=='V2'):
                WaveFormData=LeadData.find('WaveFormData').text#尋找所有WaveFormData內的text
                BinaryECGData=base64.b64decode(WaveFormData)#把text內的資料作轉換
                n=len(BinaryECGData)
                if(n==10000):
                    V2array=array.array('d')#做一個矩陣拿來存檔

                    for t in range(0,n,2):
                        sample = struct.unpack("h", BinaryECGData[t:t+2])
                        V2array.append(sample[0])
        return V2array
    
    def V3data10000(self):
        tree=ET.parse(self.path)  
        root=tree.getroot()
        for LeadData in root.iter('LeadData'):#在所有LeadData包含的內容中
            LeadID=LeadData.find('LeadID').text#尋找LeadID內的text
            if(LeadID=='V3'):
                WaveFormData=LeadData.find('WaveFormData').text#尋找所有WaveFormData內的text
                BinaryECGData=base64.b64decode(WaveFormData)#把text內的資料作轉換
                n=len(BinaryECGData)
                if(n==10000):
                    V3array=array.array('d')#做一個矩陣拿來存檔

                    for t in range(0,n,2):
                        sample = struct.unpack("h", BinaryECGData[t:t+2])
                        V3array.append(sample[0])
        return V3array
    
    def V4data10000(self):
        tree=ET.parse(self.path)  
        root=tree.getroot()
        for LeadData in root.iter('LeadData'):#在所有LeadData包含的內容中
            LeadID=LeadData.find('LeadID').text#尋找LeadID內的text
            if(LeadID=='V4'):
                WaveFormData=LeadData.find('WaveFormData').text#尋找所有WaveFormData內的text
                BinaryECGData=base64.b64decode(WaveFormData)#把text內的資料作轉換
                n=len(BinaryECGData)
                if(n==10000):
                    V4array=array.array('d')#做一個矩陣拿來存檔

                    for t in range(0,n,2):
                        sample = struct.unpack("h", BinaryECGData[t:t+2])
                        V4array.append(sample[0])
        return V4array

