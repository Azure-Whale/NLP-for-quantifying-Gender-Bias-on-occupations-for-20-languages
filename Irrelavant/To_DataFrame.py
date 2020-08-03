from math import *
import numpy
import pandas as pd

a=[1,2,3]
b=[3,4,5]
for i in a:
    print(i)


answer=0
a=[]
a.append(0.019574583)
a=[1,2,3,3,4]
K={"A":a}
p=pd.DataFrame(K)
print(p[0:2])
print(len(p[0:2]))
print(list(p.columns))
p.rename(columns={'A':'B'},inplace=True)
print(p)
p.columns=['C']
print(p)

'''Familiar with the dict'''
haha={}
a=[4,3,2,1]
b=[1,2,3,4]
for i in range(len(b)):
    haha[b[i]]=a[i]
print(haha)
print(haha.keys(),haha.values(),haha.items())
print(list(haha.keys()))
L=[]
for i in sorted(list(haha.keys())):
    L.append([i,haha[i]])
print('Attention   ',L)
'''How to build a matrix or table using your dictionary'''
dict={'A':list(haha.values()),'B':list(haha.keys())}
Df=pd.DataFrame(dict)
Df.to_csv('test.csv',index=False)
table=pd.read_csv('test.csv')
print(table)