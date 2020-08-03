"""Packages"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from gensim.models import KeyedVectors
import os
import gc

test_data = pd.read_csv('D:\Data\Bias_Project_Translation\gender_Translations/' + 'English' + '.csv')
print(test_data.head())
one=input('Indexing\n')
print(test_data.iat[0,0],'\nDone!')
print(test_data['male'],'\nDone!')

print(test_data['male'].iat[0],'\nDone!')
print(test_data['male'][0],'\nDone!')
#print(test_data[0][0],'\nDone!')  the first one is always the key of column
#print(test_data.loc['male'])   Error
#print(test_data.loc[0,'male'])  If the index is not string, then loc cannot find it
print(test_data.iat[0,0],'\nDone!')
print(test_data.iloc[0, 0],'\nDone!')
clear= lambda : os.system('cls')
two=input('Length')
print(test_data.columns,'\nDone!')
print(test_data.info,'\nDone!')
print(test_data.info(),'\nDone!')
print(test_data.shape,'\nDone!')  # df.shape doesn't need a ()
print(len(test_data),'\nDone!')
print(test_data.iloc[:,1].count(),'\nDone!')
clear= lambda : os.system('cls')
third=input('to_list')
print(test_data.iloc[:,1].tolist())  # transfer specific column into list including null value

bool_list = pd.notnull(test_data.iloc[:,1])  # get bool list of origin column in order to later filter
print(test_data[bool_list].iloc[:,1].tolist()) # filter the dataset firstly and after that you can just do normal operaition


