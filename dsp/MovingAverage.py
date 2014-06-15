import numpy as np

#Moving average class for numbers, vectors, arrays, etc
#Just pass in shape parameter (arrayname.shape)
class MovingAverage(object):
    def __init__(self, shape, integration_time):
        self.sum                    = np.zeros((np.prod(shape),1),dtype=np.uint64)
        self.integration_time       = integration_time
        self.array                  = np.zeros((np.prod(shape), integration_time),dtype=np.int32)
        self.index                  = 0
        self.shape                  = shape
        self.temp                   = np.zeros((np.prod(shape),1),dtype=np.int32)
        
        

    def update(self,newupdate):
        #Reshape to a column vector. No, newupdate[:,None] doesn't work for some reason
        self.temp = np.reshape(newupdate,np.prod(self.shape))
        #New mean is simply removing the oldest vector from and adding the new vector
        #to the running sum

        self.sum[:,0] += self.temp - self.array[:,self.index]
        self.array[:,self.index] = self.temp
        self.index = np.mod(self.index+1,self.integration_time)
        return np.reshape(np.divide(self.sum,self.integration_time),self.shape)