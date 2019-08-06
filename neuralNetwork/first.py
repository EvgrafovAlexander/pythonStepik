#основные операции
import numpy as np

a = np.array([[1,2,3], [4,5,6]])  # создаём массив
print(a)  # смотрим на массив

print(a.shape)  # смотрим на форму массива

mat = 2 * np.eye(3, 4) + np.eye(3, 4, k=1)
#print(mat.reshape(1))

str, col = mat.shape
print(mat.reshape(str * col, 1))

