import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt


def Scatter_Polt(translated_index_bias, Title):
    '''If you want to plot a regression, just choose what you prefer'''

    x_value = translated_index_bias.iloc[:, 0].tolist()
    # y=sorted(bias_array)
    y_value = translated_index_bias.iloc[:, 1].tolist()
    # plot grid
    plt.figure(figsize=(20, 15))  # set size of your figure
    plt.title(Title)  # give a title to your figure
    plt.ylabel('Woman Bias')
    plt.xticks(rotation=90)
    # sns.regplot(x, y)
    plt.plot(x_value, y_value, color='blue', label='Woman Bias')
    plt.scatter(x_value, y_value)
    # sns.pointplot(x=x_value, y=y_value)
    # plt.scatter(x, y, alpha=0.6)
    plt.grid()
    # plt.label='Woman Bias'
    plt.legend(loc='upper left')
    figpath = 'Results/Summary/Average bias for each occ.png'
    plt.savefig(figpath)


Index_refer_Nature = pd.read_csv(r'D:\Data\Bias_Project_Translation\Index_Reference_Nature_Words.csv')
occupations = Index_refer_Nature.iloc[:, 1].tolist()
terrorism = Index_refer_Nature.iloc[:, 3].tolist()

Gender_Results = os.listdir(r'C:\Users\Night\Desktop\python_work\project\Gender_Occ_Bias\Results/')
Religion_Results = os.listdir(r'C:\Users\Night\Desktop\python_work\project\Religion_Terrorism_Bias\Results/')
R = []
for occ in occupations:  # Get occupation list from reference table
    occ_avg = []

    for f in Gender_Results:  # for each occupation, we try to search their corr bias in each languages files
        if f[-3:] == 'csv' and f != 'Bias_Country.csv':   # Only need languages csv and pass irrelevant csv
            lang = pd.read_csv(
                r'C:\Users\Night\Desktop\python_work\project\Gender_Occ_Bias\Results/' + f)  # Load occ in each language
            set_occ = list(lang.iloc[:, 1])   # Extra all occ set of single languages
            if occ in set_occ:     # Search the set, if it has the occ we want, append its bias to single occ biases
                bias = lang[lang['trans'] == occ].iloc[:, 2]
                bias = float(bias)
                occ_avg.append(bias)
    Mean = np.mean(occ_avg)  # After get all bias, get its mean
    if Mean != Mean:
        exit(1)
    R.append([occ, Mean]) # Transfer it into df
R = pd.DataFrame(R, columns=['Occ', 'Bias'])
print(R)
R = R.sort_values(by='Bias', ascending=True)
Scatter_Polt(R, 'Average Bias')
R.to_csv('Results/Summary/Average bias for each occ.csv')
