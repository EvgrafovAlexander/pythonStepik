import pandas as pd
import numpy as np

stud_perfomance = pd.read_csv('C:/Users/nemes/PycharmProjects/pythonStepik/StudentsPerformance.csv')

print(stud_perfomance.shape)

print(stud_perfomance.head())

stud_perfomance_lunch_free = stud_perfomance.loc[stud_perfomance.lunch  == 'free/reduced']
stud_perfomance_lunch_standard = stud_perfomance.loc[stud_perfomance.lunch  == 'standard']
print(stud_perfomance.loc[stud_perfomance.lunch  == 'free/reduced'])

print((stud_perfomance.lunch == 'free/reduced').mean())

print(stud_perfomance_lunch_standard.describe())
print(stud_perfomance_lunch_free.describe())

#print(stud_perfomance.describe())