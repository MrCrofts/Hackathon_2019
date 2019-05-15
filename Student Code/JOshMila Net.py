import numpy as np
Input1=0.5
Input2=1

def sig(x):
    d=(1 / (1 + np.exp(-x)))
    return d

class layer1():
    def __init__(self,input1,input2):
            self.input1=input1
            self.input2=input2
            
    def n1(weight1, weight2):
        weight1=weight1
        weight2=weight2
        
        a=(self.input1*weight1)
        b=(self.input2*weight2)
        c=a+b
        return (sig(c))
        
        

layer1(Input1,Input2)
print(layer1.n1(0.5,0.25))

    


