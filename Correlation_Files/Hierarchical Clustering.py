# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from sklearn import *
from scipy import stats
from scipy.cluster.hierarchy import dendrogram, linkage

correlation_matrix=pd.read_csv('Revised_Corr_Matrix.csv',index_col=0)
#print(correlation_matrix)
correlation_matrix.fillna(0)
col = correlation_matrix.columns
correlation_matrix=np.array(correlation_matrix)
#print(correlation_matrix)
correlation_matrix = np.sqrt(2*(-correlation_matrix+1))
print(correlation_matrix)
linked = linkage(correlation_matrix, 'single')
plt.figure(figsize = (15,10))
dendrogram(linked,
show_contracted=True,
                    orientation = 'top',
                    labels = list(col),
                    distance_sort = 'descending',
                    show_leaf_counts = True
)
#plt.figure(figsize = (20,1))
plt.title('Gender_Occ_Bias_Clustering')
plt.savefig('hierarchical map.png')
plt.show()
