#Computing the pseudo-inverse of A
pinv = np.linalg.pinv(A)
# Computing the cost
X = np.dot(pinv, C)
X = np.round(X).astype(int)
print("Estimated cost of products:/n", X)
