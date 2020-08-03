import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from sklearn import *
from scipy import stats
import seaborn as sns
import codecs
from scipy.cluster.hierarchy import dendrogram, linkage
import os
import pandas as pd
'''Using each languages's bias columns, find their common index and do the P-corr'''
languages=pd.read_csv(r"D:\Data\Bias_Project_Translation\Path Reference.csv")   # load the list of chosen languages
languages = languages['languages']
df = []
for lang1 in languages:
    row = []
    for lang2 in languages:

        '''Import data to variables for lang1 and lang2'''
        lang1_data=pd.read_csv('Results/'+lang1+'.csv')
        lang1_data = lang1_data[['index','bias']]
        #print(lang1_data)
        lang2_data=pd.read_csv('Results/'+lang2+'.csv')
        lang2_data = lang2_data[['index', 'bias']]
        #print(lang1_data)
        '''Language 1'''
        lang2_index=lang2_data['index'].tolist()  # get index of lang2
        lang1_column = lang1_data[lang1_data['index'].isin(lang2_index)]  # get rows of lang1 having index in lang2
        lang1_column = lang1_column.sort_values(by='index',ascending=True)  # sort the order get ready for analyze
        #print(lang1,' AND ',lang2)
        #print(lang1_column)
        '''Language 2'''
        lang1_index = lang1_data['index'].tolist()  # get index of lang2
        lang2_column= lang2_data[lang2_data['index'].isin(lang1_index)]  # get rows of lang1 having index in lang2
        lang2_column = lang2_column.sort_values(by='index', ascending=True)  # sort the order get ready for analyze
        #print(lang2_column)
        #print(len(lang1_column['index']),len(lang2_column['index']))
        corr = np.corrcoef(lang1_column['bias'].tolist(),lang2_column['bias'].tolist())
        print(lang1, ' AND ', lang2)
        print(corr[0,1])
        row.append(corr[0,1])
        #print(lang1_column['index'].equals(lang2_column['index']))
        #print(lang1_column['bias'].equals(lang2_column['bias']))
        #a=input()
    df.append(row)
col_name = languages.tolist()  #Set name for new correlation Matrix
df=pd.DataFrame(df)
df.columns=col_name
df.index=col_name
df.to_csv('Correlation_Files/Corr_Matrix.csv', encoding='utf-8-sig')

