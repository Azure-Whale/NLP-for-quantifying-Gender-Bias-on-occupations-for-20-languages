#  This programmer aims to analyze religion bias in countries within most used languages  #

"""Packages"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from gensim.models import KeyedVectors
import os
import gc
import sys
import seaborn as sns

'''Figure our which nature group words you want to choose'''
# tranlation_file_path = 'wordlists/religion_Translations/'
tranlation_file_path = 'D:\Data\Bias_Project_Translation\gender_Translations/'
Gender = True
Religion = False

'''Set correspoding plot name'''
Plot_Name = 'Gender_Occ_Bias'
# Bias_Name = 'Religion_Terrorism_Bias'
# Bias_Name = 'Gender_Occ_Bias'
# Bias_Name = 'Religion_Terrorism_Bias'

Index_refer_Nature = pd.read_csv(r'D:\Data\Bias_Project_Translation\Index_Reference_Nature_Words.csv')

Plot_path = "Results/"


def Import(language_name, embedding_name):
    '''Import translated word-lists and load embedding model'''

    word_list = pd.read_csv(tranlation_file_path + language_name + '.csv')
    ##########  Import Word Lists  ##################

    # word_list = np.array(word_list)
    # Group1 = []  # man
    # Group2 = []  #  woman   this is woman bias
    # Nature = []
    # The length for each wordlists
    # LenOfGroup1 = word_list.iloc[:,1].count()
    # LenOfGroup2 = word_list.iloc[:,2].count()
    # LenOfNatrual = word_list.iloc[:,0].count()
    bool_Nature = pd.notnull(word_list.iloc[:, 0])
    bool_Group1 = pd.notnull(word_list.iloc[:, 1])
    bool_Group2 = pd.notnull(word_list.iloc[:, 2])
    Group_Nature = word_list[bool_Nature].iloc[:, 0].tolist()
    # print(word_list.iloc[:,0])
    # print()
    # print(word_list[bool_Nature].iloc[0])
    # print('K',Group_Nature)
    Group1 = word_list[bool_Group1].iloc[:, 1].tolist()
    Group2 = word_list[bool_Group2].iloc[:, 2].tolist()
    '''
    word_list = np.array(word_list)
    for i in range(0, LenOfGroup1):
        Group1.append(word_list[i][0])
    #print(Islam)
    for i in range(0, LenOfGroup2):
        Group2.append(word_list[i][1])
    Group2.append(word_list[i][1])
    #print(Christianity)
    for i in range(0, LenOfNatrual):
        Nature.append(word_list[i][2])
    #print(Terrorism)
    '''
    # model = FastText.load_fasttext_format("D:\Data\Word Embedding\Vectors/" + path, encoding='utf-8')
    # print("Import")
    model = KeyedVectors.load_word2vec_format("D:\Data\Word Embedding\Vectors/" + embedding_name, encoding='utf-8')
    print("Importation Successfully")
    return model, Group1, Group2, Group_Nature


def Get_filenames(dir):
    '''Return filenames as a list'''
    filenames = os.listdir(dir)
    return filenames


def Scatter_Polt(translated_index_bias, language):
    '''If you want to plot a regression, just choose what you prefer'''
    '''
    if Gender:
        tag = index_bias[j][0]
        tran = Index_refer_Nature['occupation'][tag]
        tran_array.append(tran)
    else:
        tag = index_bias[j][0]
        tran = Index_refer_Nature['terrorism'][tag]
        tran_array.append(tran)
    '''

    # for i in range(len(index_bias)):
    # bias_array.append(index_bias[i][1])

    x_value = translated_index_bias.iloc[:, 1].tolist()
    # y=sorted(bias_array)
    y_value = translated_index_bias.iloc[:, 2].tolist()
    # plot grid
    plt.figure(figsize=(20, 15))  # set size of your figure
    plt.title(language)  # give a title to your figure
    plt.ylabel(Plot_Name)
    plt.xticks(rotation=90)
    # sns.regplot(x, y)
    plt.plot(x_value, y_value, color='blue', label='Woman Bias')
    plt.scatter(x_value, y_value)
    # sns.pointplot(x=x_value, y=y_value)
    # plt.scatter(x, y, alpha=0.6)
    plt.grid()
    # plt.label='Woman Bias'
    plt.legend(loc='upper left')
    figpath = Plot_path + language + '.png'
    plt.savefig(figpath)

########################################################

def Bias_computation(embedding, Group1, Group2,
                     Nature_Words):  # Group1 -(man/Islam)  Group2 -(woman/Christian)  Nature -(Occupation/Terrorism)
    """Return average bias"""

    '''Get corr word embedding values according to translation csv from we files'''
    Group1_vec = []
    for item in Group1:
        try:
            Group1_vec.append(embedding[item])
        except:
            continue
    Group1_vec = np.array(Group1_vec)

    # Get vectors of test word group
    Group2_vec = []
    for item in Group2:
        try:
            Group2_vec.append(embedding[item])
        except:
            continue
    Group2_vec = np.array(Group2_vec)

    Nature_index = []  # Used to make an index ordered by nature word to plot regression
    Group_Nature_vec = []
    index = 0
    for item in Nature_Words:
        try:
            Group_Nature_vec.append(embedding[item])  # if the
            # model can find corr embedding then record corr mark as well
            Nature_index.append(index)
            tran = Index_refer_Nature['occupation'][index]

            index += 1
        except:
            index += 1
            continue
    Group_Nature_vec = np.array(Group_Nature_vec)

    # Make sure the set of info is correct.
    #  Compute the average vectors for group1 and group2
    Group1 = np.mean(Group1_vec, axis=0)
    Group2 = np.mean(Group2_vec, axis=0)
    Bias = []
    Index_Bias = []  # Bias - index
    '''Calculation Method'''
    for i in range(0, len(Group_Nature_vec)):
        Bias.append((np.linalg.norm(np.subtract(Group_Nature_vec[i], Group1))) - (np.linalg.norm(
            np.subtract(Group_Nature_vec[i], Group2))))  # Group 2 Bias
    '''Sum up Results'''
    for i in range(len(Bias)):
        item = Bias[i]
        item_index = Nature_index[i]
        Index_Bias.append([item_index, item])  # Recording each word's bias and index
    Avg_Bias = np.mean(Bias, axis=0)  # Calculating the mean of all bias for one languages

    '''Test'''
    print('This is translation of calculated Nature words:')
    print(Index_Bias)
    print('Average Bias:')
    print(Avg_Bias)

    return Avg_Bias, Index_Bias


if __name__ == '__main__':
    # path_dict = pd.read_csv('Table/chosen langs.csv')  # dict for lang and their file names

    '''Loop'''
    embeddings = []
    '''Set path reference'''
    Reference = pd.read_csv(r"D:\Data\Bias_Project_Translation\Path Reference.csv")  # languages/paths/trans  0/1/2
    embeddings = list(Reference.iloc[:, 1])  # Extract list of file paths
    Bias_array = []  # It store all the average bias for each languages
    lang_array = []  # It store all the language name for each languages
    # print(Reference)
    for i in range(len(embeddings)):  # Only process those vec which are in our lists
        try:
            if embeddings[i] in list(Reference.iloc[:, 1]):  # if we have the vec, we start processing
                print('#####Starting it######')
                print(embeddings[i])
                for m in range(len(Reference)):  # get corresponding language name
                    # print(len(list(Reference.iloc[:, 1])), len(embeddings))
                    # print(m,i)
                    if Reference.iloc[m, 1] == embeddings[i]:
                        languages = Reference.iloc[m, 0]
                        embedding = Reference.iloc[m, 1]
                        # print(lang, path)
                        # print("Processing")
                        model, Word_Group1, Word_Group2, Nature_Words = Import(languages, embedding)
                        temp_bias, bias_index = Bias_computation(model, Word_Group1, Word_Group2, Nature_Words)
                        # get records for Avg_bias - Country Plot
                        Bias_array.append(temp_bias)
                        lang_array.append(languages)
                        # Get records & plot for clustering
                        index_array = []
                        bias_array = []
                        tran_array = []
                        for j in range(len(bias_index)):
                            index_array.append(bias_index[j][0])  # index
                            bias_array.append(bias_index[j][1])  # bias
                            if Gender:
                                tag = bias_index[j][0]
                                tran = Index_refer_Nature['occupation'][tag]
                                tran_array.append(tran)
                            else:
                                tag = bias_index[j][0]
                                tran = Index_refer_Nature['terrorism'][tag]
                                tran_array.append(tran)
                        DF_filepath = Plot_path + languages + '.csv'
                        Summary = {'index': index_array, 'trans': tran_array, 'bias': bias_array}
                        df = pd.DataFrame(Summary)
                        print(df)
                        df = df.sort_values(by="bias", ascending=True)
                        print(df)
                        # DF_filepath = Plot_path + languages + '.csv'
                        df.to_csv(DF_filepath, index=False)
                        Scatter_Polt(df, languages)
                        del model
                        gc.collect()
                        # exit(1)
        except:
            print(embeddings[i], 'Error!!!!!!!!!!!!!!!!')
            print(sys.exc_info()[0])
            # exit(1)
            continue
    #  Making Avg_bias - Country Plot
    try:
        Info_data = {'lang': lang_array, 'Bias': Bias_array}
        Info = pd.DataFrame(Info_data)
        path_1 = 'Results/Bias_Country.csv'  # This is the path saving Bias-Countries Plot
        Info.to_csv(path_1)
    except:
        print('Error')
