# This program aims to combien all tables in /table into one table because of disturbe of Vietnamese
import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from sklearn import *
from scipy import stats
from scipy.cluster.hierarchy import dendrogram, linkage
import os



#The bias for each languages is separated into many files(aligned), this prog amis to calculate their correlation matrix

def Cal_Correlation_rank_Coefficient(df1, df2):
    coef, p = stats.spearmanr(df1, df2)
    return coef, p

def Correlation_rank_Coefficient(df1,df2):
    # find the occupations found both in two data sets, which is OCC, a list of ...



    Occ = []
    s = set(df2.iloc[:]['Occupations'])
    for Occ_name in range(0, len(df1)):
        try:
            if df1.iloc[Occ_name]['Occupations'] in s:
                Occ.append(df1.iloc[Occ_name]['Occupations'])
        except:
            print('unexpected error occurs')
            exit(1)
    #print('the length of the occupation existing both in the df1 and df2:  ', len(Occ))
    # Occ=set(Occ)

    data1 = []  # 1st parameter compared within Pearson rank coefficient, which is a list from df1
    data2 = []  # 2nd parameter compared within Pearson rank coefficient, which is a list from df2
    for Occ_name in Occ:
        for j in range(0, len(df1)):
            if df1.iloc[j]['Occupations'] == Occ_name:
                data1.append(df1.iloc[j]['Woman Bias'])
        for j in range(0, len(df2)):
            if df2.iloc[j]['Occupations'] == Occ_name:
                data2.append(df2.iloc[j]['Woman Bias'] + 1)

    coef, p = Cal_Correlation_rank_Coefficient(data1, data2)
    #print(coef, p)  # Don't know what's p yet
    '''Verification Plot'''

    return coef, p

table_name_lists = os.listdir('tables/')  # All table names in target directory


# Get all names of Country
#Refer = pd.read_csv('Plot/Coun-Bias.csv')
Country = table_name_lists
print(Country)
# modify names into paths
for i in range(len(Country)):
    Country[i] ='tables/'+Country[i]
# set space for matrix
row=[]
col=[]
# cal corr matrix
for coun1 in Country:  # for each lang, set a row
    row=[] # every iteration in row, updating row[]
    print(coun1)
    table1=pd.read_csv(coun1)
    index1 = list(table1['index'])
    for coun2 in Country:  # for each lang, cal corr for all lang
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
Corr_matrix.columns=Country
Corr_matrix.set_index(Country,inplace=True)
Corr_matrix.to_csv('plot/Corr_matrix.csv')



