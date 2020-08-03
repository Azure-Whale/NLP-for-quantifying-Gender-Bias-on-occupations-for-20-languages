import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from sklearn import *
from scipy import stats
from scipy.cluster.hierarchy import dendrogram, linkage

#The bias for each languages is separated into many files(aligned), this prog amis to calculate their correlation matrix

def Cal_Correlation_rank_Coefficient(df1, df2):
    coef, p = stats.spearmanr(df1, df2)
    return coef, p

# Get all names of Country
Languages_Reference = pd.read_csv(r"D:\Data\Bias_Project_Translation\Path Reference.csv")
languages = Languages_Reference['languages'].tolist()
# modify names into paths
for i in range(len(languages)):
    languages[i] ='Results/'+languages[i]+'.csv'
# set space for matrix
row=[]
col=[]
# cal corr matrix
for coun1 in languages:
    languages[i] = 'Results/' + languages[i] + '.csv'



for coun1 in languages:  # for each lang, set a row
    row=[] # every iteration in row, updating row[]
    print(coun1)
    table1=pd.read_csv(coun1)
    index1 = list(table1['index'])
    for coun2 in languages:  # for each lang, cal corr for all lang
        print(coun2)
        table2=pd.read_csv(coun2)
        index2=list(table2['index'])
        try:
            Index=[]
            print(index1)
            print(index2)
            for m in index1:
                if m in index2:
                    Index.append(m)
        except:
            print(coun1,' and ',coun2,'have no common embedding')
        print(Index)
        array1 = []
        array2 = []
        print()
        for k in range(len(table1)):
            if table1['index'][k] in Index:
                array1.append(table1['bias'][k])
        for j in range(len(table2)):
            if table2['index'][j] in Index:
                array2.append(table2['bias'][j])
        corr, p = Cal_Correlation_rank_Coefficient(array1, array2)
        row.append(corr)
        print(corr,'iteration')
    col.append(row)
col=np.array(col)
Corr_matrix=pd.DataFrame(col)
#Corr_matrix.rename(Country,axis='columns',index=False)
Corr_matrix.columns=Languages_Reference['languages'].tolist()
Corr_matrix.to_csv('Correlation_Files/Corr_matrix.csv',index=False)



