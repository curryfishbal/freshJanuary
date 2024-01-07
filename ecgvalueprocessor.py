import numpy as np
class ecgvalueprocessor:
    def __init__(self, data):
        self.data=data
        
    def newecgvalue(self):
        ECGarray = np.array(self.data)
        n=len(ECGarray)

        newECGarr= np.array([])

        for i in range(1,n,1):
            k=4.88*0.01*ECGarray[i]
            newECGarr = np.append(newECGarr, k)
            
        return newECGarr