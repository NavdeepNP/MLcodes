import pandas as pd
import numpy as np

df=pd.read_excel("C:/Users/navde/OneDrive - Amrita vishwa vidyapeetham/Desktop/Amritafiles/Sem4/MachineLearning/Lab Session Data.xlsx", sheet_name="Purchase data",usecols="A:E")

A = df.iloc[:, :-1]
C = df.iloc[:, -1]

A = A.apply(pd.to_numeric, errors='coerce')
A.fillna(0, inplace=True)

dimensionality = A.shape[1]
print("Dimensionality of the vector space:", dimensionality)

# Computing number of vectors in the vector space (Number of rows in A)
num_vectors = A.shape[0]
print("Number of vectors in the vector space:", num_vectors)

#Computing the rank of A
rank = np.linalg.matrix_rank(A)
print("Rank of Matrix A:", rank)

#Computing the pseudo-inverse of A
pinv = np.linalg.pinv(A)

# Computing the cost
X = np.dot(pinv, C)
X = np.round(X).astype(int)
print("Estimated cost of products:\n", X)