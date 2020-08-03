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

#Corr_matrix = pd.read_csv('Table/Corr_Matrix.csv', index_col=0)
Corr_matrix = pd.read_csv('Regreesion&lists/Corr_matrix.csv', index_col=0)
label = list(Corr_matrix.columns)
plt.tight_layout()
plt.figure(figsize=(90,90))
g = sns.heatmap(Corr_matrix, cbar=True, xticklabels=label,yticklabels=label,
                fmt='.2f', annot_kws={'size': 10}, annot=True,
                square=True)
# fix for mpl bug that cuts off top/bottom of seaborn viz
b, t = plt.ylim() # discover the values for bottom and top
b += 0.5 # Add 0.5 to the bottom
t -= 0.5 # Subtract 0.5 from the top
plt.ylim(b, t) # update the ylim(bottom, top) values
g.set_yticklabels(g.get_yticklabels(), rotation = 0)
g.set_xticklabels(g.get_yticklabels(), rotation = 90)
plt.savefig(r'Plot/Heatmap_Aligned.png')
#plt.show()
print('OK')


correlation_matrix = Corr_matrix.iloc[0,:]
correlation_matrix = np.sqrt(-Corr_matrix + 1)
print(correlation_matrix)
linked = linkage(correlation_matrix, 'single')
plt.figure(figsize = (40, 10))
dendrogram(linked,
           orientation = 'top',
           labels = list(Corr_matrix),
           distance_sort = 'descending',
           show_leaf_counts = True
           )
#plt.figure(figsize = (20,1))
plt.savefig('Plot/hierarchical map.png')
plt.show()
plt.close()
