from urllib.request import urlopen
import numpy as np

filename = input()
f = urlopen(filename)

matrix = np.loadtxt(f, skiprows=1, delimiter=",")
print(matrix.mean(axis=0))
