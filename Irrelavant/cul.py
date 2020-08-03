from math import *
import numpy
import pandas as pd

def Entropy(a,b):
    c=b-a
    val = -(a/b*log(a/b,2)+c/b*log(c/b,2))
    val = round(val,2)
    print(val)
    return val

k=5/7    ######################################
def InfoGain(a,b):
    return round(a-k*b,2)

a1,a2=2,7
print('#########Before Split######')
a = Entropy(a1,a2)   # before
b1,b2=2,5   #######################################
print('######After Split#####')
b = Entropy(b1,b2)   # after
print('######After Split#####')
print(InfoGain(a,b))
