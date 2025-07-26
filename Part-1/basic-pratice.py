"""
✅ Practice Questions (Intermediate)
Reshape an array of shape (1, 12) to (3, 4)

Create a 3x3 matrix and subtract row-wise mean

Create an array with 20 random integers between 1 and 100 and filter values > 50

Multiply a (2x3) matrix with a (3x2) matrix

Count how many times each number appears in an array """
import numpy as np
arr1= np.array([[1,2,3],
                [4,5,6]])


arr2= np.array([[4,5],
                [6,7],
                [4,5]])



print((arr1@arr2))


prr = np.random.randint(0,11,size=20)
count =np.bincount(prr)
print(count)









