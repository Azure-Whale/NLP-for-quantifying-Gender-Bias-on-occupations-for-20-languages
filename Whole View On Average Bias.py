import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#files=os.listdir(r'C:\Users\Night\Desktop\python_work\project\Religion_Terrorism_Bias\Results')

file = pd.read_csv(r'C:\Users\Night\Desktop\python_work\project\Gender_Occ_Bias\Results\Bias_Country.csv')
sorted_file = file.sort_values(by='Bias',ascending=True)
print(file)
plt.figure(figsize=(10,15))
plt.xticks(rotation=90)
plt.title('Woman Bias')
plt.plot(sorted_file['lang'],sorted_file['Bias'],color='green',label='Woman_Occ_bias')
plt.scatter(sorted_file['lang'],sorted_file['Bias'],color='red')
plt.grid()
plt.legend()

plt.savefig('Results/Result.png')