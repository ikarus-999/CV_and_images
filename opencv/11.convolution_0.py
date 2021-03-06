import numpy as np

mat0 = np.array([[0,1,0],[1,2,1],[0,1,0]])
mat1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(mat0)
print(mat1)

sigma = 0

for i in range(3):
    for j in range(3):
        sigma += mat0[i, j] * mat1[i, j]

print(sigma)

mat_mul = mat0 * mat1
print(mat_mul)
mat_mul = np.multiply(mat0, mat1)
print(mat_mul.sum())
