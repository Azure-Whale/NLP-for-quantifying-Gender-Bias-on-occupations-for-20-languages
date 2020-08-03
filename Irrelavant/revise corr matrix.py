# -*- coding: utf-8 -*-
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

chosen_lang=pd.read_csv('Table/chosen langs.csv')   # load the list of chosen languages
reference=pd.read_csv(r'C:\Users\Night\Desktop\lan_path.csv')  # reference includes countries and their vec/ file paths
Coun_list=pd.read_csv('D:/Data/Table/lan_path.csv')  # load dict for all available countries
Corr_matrix = pd.read_csv('D:/Data/Table/Heatmap_Functions.csv', index_col=0)  # The corr_matrix including every languages

# looking up my reference and only find languages that we choose
lang_list=[]
for i in range(len(chosen_lang)):
    lang_list.append(chosen_lang['languages'][i])   # ['Vietnamese', 'Korean', 'Norwegian'] are not in list anymore
#print(lang_list)
#x=input()
print(Corr_matrix[lang_list])
print(Corr_matrix.loc[lang_list,lang_list])

Correlation = Corr_matrix.loc[lang_list,lang_list]
Correlation.to_csv('/Table/Corr_Matrix.csv')