import numpy as np



# 1. Dot Method

# two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Dot Method example 1
C = np.dot(A, B)
print("Dot product using np.dot:")
print(C)

# Dot Method example 2
C = A @ B
print("Dot product using @ operator:")
print(C)

# Dot Method example 3
C = np.matmul(A, B)
print("Dot product using np.matmul:")
print(C)




# 2. Transpose Method

import numpy as np

# matrix
A = np.array([[1, 2], [3, 4], [5, 6]])

# example 1
A_T = np.transpose(A)
print("Transpose using np.transpose:")
print(A_T)

# example 2
A_T = A.T
print("Transpose using .T attribute:")
print(A_T)

# example 3
A_T = np.swapaxes(A, 0, 1)
print("Transpose using np.swapaxes:")
print(A_T)




#  3. linalg.inv method

import numpy as np

# square matrix
A = np.array([[1, 2], [3, 4]])

# Example 1
A_inv = np.linalg.inv(A)
print("Inverse using np.linalg.inv:")
print(A_inv)

# Example 2
I = np.eye(A.shape[0])
A_inv = np.linalg.solve(A, I)
print("Inverse using np.linalg.solve:")
print(A_inv)

# Example 3
A_inv = np.linalg.pinv(A)
print("Inverse using np.linalg.pinv:")
print(A_inv)



# 4. linalg.det method

import numpy as np

# square matrix
A = np.array([[1, 2], [3, 4]])

# Example 1
det_A = np.linalg.det(A)
print("Determinant using np.linalg.det:")
print(det_A)

# Example 2
sign, logdet = np.linalg.slogdet(A)
det_A = sign * np.exp(logdet)
print("Determinant using np.linalg.slogdet:")
print(det_A)

# Example 3
eigenvalues = np.linalg.eigvals(A)
det_A = np.prod(eigenvalues)
print("Determinant using eigenvalues:")
print(det_A)



# 5. Flatten method

import numpy as np

# matrix
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Example 1
A_flat = A.flatten()
print("Flatten using np.ndarray.flatten:")
print(A_flat)

# Example 2
A_flat = np.ravel(A)
print("Flatten using np.ravel:")
print(A_flat)

# Example 3
A_flat = A.reshape(-1)
print("Flatten using np.reshape:")
print(A_flat)

