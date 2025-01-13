

import pandas as pd

df1 = pd.read_excel('test01.xlsx',engine='openpyxl',sheet_name='students')
df2 = pd.read_excel('test01.xlsx',engine='openpyxl',sheet_name='midterm')
df3 = pd.read_excel('test01.xlsx',engine='openpyxl',sheet_name='final')

#그냥 이어붙이기

df23 = pd.concat([df2,df3])
print(df23,end='\n\n')