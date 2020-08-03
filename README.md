# Gender-Bias-on-occupations-for-20+-languages
## Goal
Applied multiple word embeddings such as Fasttext, Word2vec and Glove to quantify gender bias existing in occupations over 100+ countries(20+ languages) through 20 years from now. Quantified bias would be used to study the potential bias and undiscovered stereotypes. Here, I only present results of gender bias on occupations.
## Data Collection
You may chekc our data here: http://data.statmt.org/news-crawl/
The data is mainly the scripted news materials from different newspaper all over the world and it was categorized as multiple languages, we had chosen 20+ languages after considering the size of the text collected for each languages and the quality after we had measured preliminarily
## Data preprocesssing
Given clean data, I used nltk to tokenize, lemmatize and filter the data.
## Method to quantify the gender bias
To observe the gender bias, we need an area or topic to present the difference between male and female. The occupations could perfectly present the bias nowadays, though we actually measure the bias on multiple other topics and I only present a single part of topics I had studied.
1. Select groups of words about occupations, male and female related words, such as (driver, football player..),(male, boy..) and (female, girl..)
2. Train multiple word embedding models based on the data collected for each language, say English.word2vec, English.fasttext, English.golve....
3. After days of training, we may get multiple models for each language and get corresponding word vectors through these models.
4. We took average as the word vector of a group of words. Then we get word vectors for male, female.In the meanwhile, we also get the word vector for each occupation we had selected.
5. At last, we may calculate the distance(Euclidean distance) to quantify the distance between two words/concepts. The smaller the distance is, the closer the correlation of these two words are.
6. To find a reference to measure our results, we take the recognized gender bias data from the United Nation. The more results matched, the better the results of the model is.(After tested, we chose word2vec)
7. To study the distribution and difference of gender bias, we applied hierarchical clustering into Pearson Coefficient for results from each language. By the way, we found that the biases are well connected to the area and cultures, which means that the same culture may share the same bias and the same financial situation may share the same state of bias as well.

## Results
The results have been visualized within matplotlib, and I also attached them as excel.
To compelte the visualization we need to a reference language which is English, we automatly translate all the words into English within Google Translator API
### Gender bias quantify for serveral languages
Chinese
![Chinese](https://github.com/Azure-Whale/NLP-for-quantifying-Gender-Bias-on-occupations-for-20-languages/blob/master/Results/Chinese.png)
English
![English](https://github.com/Azure-Whale/NLP-for-quantifying-Gender-Bias-on-occupations-for-20-languages/blob/master/Results/English.png)
Dutch
![Dutch](https://github.com/Azure-Whale/NLP-for-quantifying-Gender-Bias-on-occupations-for-20-languages/blob/master/Results/Dutch.png)
Finnish
![Finnish](https://github.com/Azure-Whale/NLP-for-quantifying-Gender-Bias-on-occupations-for-20-languages/blob/master/Results/Finnish.png)
Hindi
![Hindi](https://github.com/Azure-Whale/NLP-for-quantifying-Gender-Bias-on-occupations-for-20-languages/blob/master/Results/Hindi.png)
### Correlation Analysis within Heatmap
![heatmap](https://github.com/Azure-Whale/NLP-for-quantifying-Gender-Bias-on-occupations-for-20-languages/blob/master/Table/Visualization/Revised_HeatMap.png)
### Clustering based on similar scores
![Clustering](https://github.com/Azure-Whale/NLP-for-quantifying-Gender-Bias-on-occupations-for-20-languages/blob/master/Table/hierarchical%20map_39.png)
## Conclusion
1.languages used among poor countries may had significant bias while languages used among developed countries may have relative fair gender balance
2.languages share the same culture and have the same bias. Say, bias from languages from Asia are similar and so do the Latin languages.
3.Bias from different languages vary from countries to countries. Some areas have significant gender bias on occupations.

