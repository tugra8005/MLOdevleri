import numpy as np

def powerIteration(matrix, num_iterations=100):
    columnCount = matrix.shape[0]
    vector = np.random.rand(columnCount)
    
    for _ in range(num_iterations):
        vectorNew = A @ vector
        
        vector = vectorNew / np.linalg.norm(vectorNew)
        
    eigenValue = (vector.T @ A @ vector) / (vector.T @ vector)
    
    return eigenValue, vector

A = np.array([[4.0, 1.0],
              [2.0, 3.0]])

manualEigenValue, manualEigenVector = powerIteration(A)
print(f"Dominant Özdeğer: {manualEigenValue:.4f}")
print(f"Dominant Özvektör: {manualEigenVector}\n")

numpyValue, numpyVector = np.linalg.eig(A)

maxIndex = np.argmax(numpyValue) 
numpyDominantValue = numpyValue[maxIndex]
numpyDominantVector = numpyVector[:, maxIndex] 

print(f"NumPy'ın Ürettiği Dominant Özdeğer: {numpyDominantValue:.4f}")
print(f"NumPy'ın Ürettiği Dominant Özvektör: {numpyDominantVector}\n")
