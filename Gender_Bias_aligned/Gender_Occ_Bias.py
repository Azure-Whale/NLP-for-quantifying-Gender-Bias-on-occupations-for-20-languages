#  This programmer aims to analyze religion bias in countries within most used languages  #

"""Packages"""
import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from gensim.models import KeyedVectors
from gensim.models.wrappers import FastText
import codecs
import os
import gc

def Import(lang, path):
    Target_lang = lang
    # print(len(model.words))
    word_list = pd.read_csv(r'C:\Users\Night\Desktop\python_work\project\Religion\wordlists/gender_Translations/' + lang + '.csv')
    # model = FastText.load_fasttext_format("D:\Data\Word Embedding\Vectors/" + path)

    ##########  Import Word Lists  ##################

    word_list = np.array(word_list)
    occupations = []
    Islam = []  # man
    Christianity = []  #  woman   this is woman bias
    Terrorism = []
    LenOfMan = 20  # The length of lists for male and female
    LenOfWoman = 20  # The length of lists for male and female
    LenOfOcc = 100
    for i in range(0, LenOfMan):
        Islam.append(word_list[i][1])
    #print(Islam)
    for i in range(0, LenOfWoman):
        Christianity.append(word_list[i][2])
    Christianity.append(word_list[i][2])
    #print(Christianity)
    for i in range(0, LenOfOcc):
        Terrorism.append(word_list[i][0])
    #print(Terrorism)
    #model = FastText.load_fasttext_format("D:\Data\Word Embedding\Vectors/" + path, encoding='utf-8')
    print("model Loading")
    model = KeyedVectors.load_word2vec_format("D:\Data\Word Embedding\Vectors/" + path, encoding='utf-8')
    print("model loaded")
    return model, Islam, Christianity, Terrorism
def Get_filenames(dir):
    filenames = os.listdir(dir)
    return filenames
def Regression(List, lang):
    for i in range(len(List)):
        #index_array.append(List[i][0])
        bias_array.append(List[i][1])
    x=list(range(len(bias_array)))
    #y=sorted(bias_array)
    y=bias_array
    plt.grid()
    plt.figure(figsize=(15,20))
    plt.title(lang)
    plt.ylabel('Gender Occupation Bias')
    plt.title(lang)
    #sns.regplot(x, y)
    plt.scatter(x, y, alpha=0.6)
    figpath = "plot/" + lang +'.png'
    plt.savefig(figpath)


########################################################

def Religious_Bias(model, Islam, Christianity, Terrorism):
    '''Regious Bias is used to compute Christianity Bias, which means if the value is positive,
    it prefers Christianity'''

    '''Get corr word embedding values according to translation csv from we files'''
    Group_Isam_vec = []
    for item in Islam:
        try:
            Group_Isam_vec.append(model[item])
        except:
            continue
    Group_Isam_vec = np.array(Group_Isam_vec)
    missing = []

    # Get vectors of test word group
    Group_Christianity_vec = []
    for item in Christianity:
        try:
            Group_Christianity_vec.append(model[item])
        except:
            continue
    Group_Christianity_vec = np.array(Group_Christianity_vec)

    Terrorism_index=[] # Used to make an index ordered by terror word to plot regression
    Group_Terrorism_vec = []
    k=0
    for item in Terrorism:
        try:

            Group_Terrorism_vec.append(model[item]) # if the model can find corr embedding then record corr mark as well
            Terrorism_index.append(k)
            k += 1
        except:
            k += 1
            continue
    Group_Terrorism_vec = np.array(Group_Terrorism_vec)


    # Make sure the set of info is correct.
    #  Compute the average vectors for men and women group
    Isam = np.mean(np.array(Group_Isam_vec), axis=0)
    Christianity = np.mean(np.array(Group_Christianity_vec), axis=0)
    Bias=[]
    Bias_index=[] # Bias - index
    for i in range(0, len(Group_Terrorism_vec)):
        Bias.append((np.linalg.norm(np.subtract(Group_Terrorism_vec[i], Isam))) - (np.linalg.norm(
            np.subtract(Group_Terrorism_vec[i], Christianity))))
    for i in range(len(Bias)):
        item = Bias[i]
        item_index = Terrorism_index[i]
        Bias_index.append([item_index,item])
        #item = Bias[i]
        #Bias_index[item]=Terrorism_index[i]
    Avg_Bias = np.mean(Bias,axis=0)

    '''Test'''
    print('This is info of Occ')
    print(Bias_index)
    print('Final Bias')
    print(Avg_Bias)
    #Bias = np.linalg.norm(Isam) - np.linalg.norm(Christianity)
    # Plot Regression line


    return Avg_Bias,Bias_index



if __name__ == '__main__':
    #path_dict = pd.read_csv('Table/chosen langs.csv')  # dict for lang and their file names

    '''Loop'''
    All_vec = []

    '''Single Trail'''
    single_path = pd.read_csv(r'C:\Users\Night\Desktop\python_work\project\Religion\Table/single trail.csv')
    All_vec = list(single_path.iloc[:, 1])
    #All_vec = ['wiki.en.align.vec']
    Bias_array = []
    lang_array = []
    print(single_path)
    for i in range(len(All_vec)):  # Only process those vec which are in our lists
        if All_vec[i] in list(single_path.iloc[:, 1]):  # if we have the vec, we start processing
            print('#####Start Loading######')
            print(All_vec[i])
            for m in range(len(single_path)):  # get corresponding language name
                print(len(list(single_path.iloc[:, 1])),len(All_vec))
                #print(m,i)
                if single_path.iloc[m, 1] == All_vec[i]:
                    lang = single_path.iloc[m, 0]
                    path = single_path.iloc[m, 1]
                    print(lang, path)
                    print("Processing")
                    model, Male, Female, Terrorism = Import(lang, path)
                    temp_bias, bias_index = Religious_Bias(model, Male, Female, Terrorism)
                    # get records for Avg_bias - Country Plot
                    Bias_array.append(temp_bias)
                    lang_array.append(lang)
                    # Get records & plot for clustering
                    index_array=[]
                    bias_array=[]
                    for j in range(len(bias_index)):
                        index_array.append(bias_index[j][0])
                        bias_array.append(bias_index[j][1])
                    Df = {'index': index_array, 'bias':bias_array}
                    df = pd.DataFrame(Df)
                    DF_filepath = 'tables/' + lang + '.csv'
                    df.to_csv(DF_filepath, index=False)
                    Regression(bias_index, lang)
                    del model
                    gc.collect()
    try:
        Info_data = {'lang':lang_array,'Bias':Bias_array}
        Info = pd.DataFrame(Info_data)
        path_1 = 'tables/Bias_Country.png' # This is the path saving Bias-Countries Plot
        Info.to_csv(path_1)
    except:
        print('Error')


