import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
data=pd.read_csv("C:/Users/navde/OneDrive - Amrita vishwa vidyapeetham/Desktop/Amritafiles/Sem4/MachineLearning/accident.csv") 
#The feature from dataset which I choose is ‘Age’ 
plt.hist(data['Age'], bins=10, edgecolor='black', alpha=0.7) 
plt.title(f'Distribution of Age feature') 
plt.xlabel('Age') 
plt.ylabel('Frequency') 
plt.show() 
mean=np.mean(data['Age']) 
variance=np.var(data['Age']) 
print(f"Mean of Age feature- {mean}") 
print(f"Variance of Age feature- {variance}")