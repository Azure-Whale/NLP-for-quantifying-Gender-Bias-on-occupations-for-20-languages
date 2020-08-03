"""Packages"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from gensim.models import KeyedVectors

import os
import gc



'''Gender'''
tranlation_file_path = 'D:\Data\Bias_Project_Translation/gender_Translations/German.csv'
table= pd.read_csv(tranlation_file_path)
embedding = KeyedVectors.load_word2vec_format("D:\Data\Word Embedding\Vectors/" + 'wiki.de.align.vec')
words = table.iloc[:,0].tolist()
a=[]
print('Group Nature%%%%%%%%%%%%%%%%%%%%%%')
for word in words:
    try:
        if embedding[word]:
            print(word)
            # print(embedding[word])
            a.append(word)
    except:
        continue
print(len(words))
print(len(a))
print(a)
print('Group1%%%%%%%%%%%%%%%%%%%%%%')
words = table.iloc[:,1].tolist()
for word in words:
    try:
        if embedding[word]:
            print(word)
            #print(embedding[word])
            a.append(word)
    except:
        continue
print(len(words))
print(len(a))
print(a)
print('Group2%%%%%%%%%%%%%%%%%%%%%%')
words = table.iloc[:,2].tolist()
for word in words:
    try:
        if embedding[word]:
            print(word)
            # print(embedding[word])
            a.append(word)
    except:
        continue
print(len(words))
print(len(a))
print(a)

k=input()
Group_Nature_vec = embedding['nurse']
Group1 = embedding['man']
Group2  = embedding['woman']
Bias = ((np.linalg.norm(np.subtract(Group_Nature_vec, Group1))) - (np.linalg.norm(
            np.subtract(Group_Nature_vec, Group2))))
print(Bias)
Group1_= table.iloc[:,1].tolist()
#Group1_=np.mean(Group1_)
Group2_= table.iloc[:,2].tolist()
#Group2_=np.mean(Group2_)
Group1_vec = []
for item in Group1_:
    try:
        Group1_vec.append(embedding[item])
    except:
        continue
Group1_vec = np.array(Group1_vec)

# Get vectors of test word group
Group2_vec = []
for item in Group2_:
    try:
        Group2_vec.append(embedding[item])
    except:
        continue
Group2_vec = np.array(Group2_vec)

Group1 = np.mean(Group1_vec, axis=0)
Group2 = np.mean(Group2_vec, axis=0)

Bias = ((np.linalg.norm(np.subtract(Group_Nature_vec, Group1))) - (np.linalg.norm(
            np.subtract(Group_Nature_vec, Group2))))
print(Bias)