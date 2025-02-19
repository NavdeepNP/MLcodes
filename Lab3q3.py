import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("C:/Users/navde/OneDrive - Amrita vishwa vidyapeetham/Desktop/Amritafiles/Sem4/MachineLearning/accident.csv")
feature1=data.iloc[0][['Age', 'Speed_of_Impact']].values
feature2=data.iloc[1][['Age', 'Speed_of_Impact']].values
p=np.arange(1, 11)
distances = []
for i in p:
    d=np.sum(np.abs(feature1-feature2)**i) ** (1/i)
    distances.append(d)
    print(f"Distances are- {d}")
plt.plot(p, distances, marker='o')
plt.title('Minkowski Distance vs. p')
plt.xlabel('p (Order of Minkowski Distance)')
plt.ylabel('Distance')
plt.show()