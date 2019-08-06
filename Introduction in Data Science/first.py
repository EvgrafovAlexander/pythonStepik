import pandas as pd
import numpy as np

stud_perfomance = pd.read_csv('C:/Users/nemes/PycharmProjects/pythonStepik/titanic.csv')

#размерность
print(stud_perfomance.shape)

#типы данных
print(stud_perfomance.dtypes)

#информация о сете
print(stud_perfomance.info())
