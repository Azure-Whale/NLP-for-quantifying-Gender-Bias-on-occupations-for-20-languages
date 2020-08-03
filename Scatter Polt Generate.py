# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file = pd.read_csv(r"C:\Users\Night\Desktop\python_work\project\Religion\Plot\Coun-Bias.csv")
# file=pd.read_csv(r'C:\Users\Night\Desktop\python_work\Religion\mapping.xlsx')
print(file)
# a=input()
xlabel = 'Countries'
ylabel = 'Woman Bias'
x_axis = file.iloc[:, 0]
y_axis = file.iloc[:, 1]
path = 'D:/Data/'


def Polt(xlabel, ylabel, x_axis, y_axis):

    plt.figure(figsize=(15, 10))
    plt.grid()
    plt.title('Religion Bias')
    plt.xlabel('Index')
    plt.ylabel('Value')
    # sns.regplot(x=Difference_Index, y=Bias)
    plt.scatter(x_axis, y_axis, alpha=0.6, color='red')
    plt.xticks()
    plt.xticks(rotation=90)
    plt.savefig(path+'sample.png')
    plt.show()
    plt.cla()


'''Please enter your parameters then the poly would save to your target path'''
Polt(xlabel, ylabel, x_axis, y_axis)
