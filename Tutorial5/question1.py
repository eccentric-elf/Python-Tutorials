
import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = A + B
C_transpose = np.transpose(C)
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Sum of A and B:\n", C)
print("Transpose of the result:\n", C_transpose)
