from os import write
import pandas as pd
import  numpy as np
import datacompy
import re
import sys 
df1=pd.read_excel('Floors DEV.xlsx')
df2=pd.read_excel('Floors POC.xlsx')

# dfDiff = df2.copy()

compare = datacompy.Compare(
df1,df2,join_columns='(triNameTX)',df1_name='SRC_DATA',
df2_name='TGT_DATA')
text_report=compare.report()

# print(text_report)
report_file=open('Floor.txt','w',encoding="utf-8")
report_file.write(text_report)
report_file.close()

'''
data=compare.report().split("-----------------------------------------------\n\n")[-2]

# print(data)
loop=(data).split('\n')
while("" in loop) :
    loop.remove("")
empty_list=[]
for x in range(len(loop)):
    s=re.sub("\s\s+" , " ", loop[x])
    fin=s.replace(' ',',').split(',')
    empty_list.append(fin)
# empty_list[-].pop()    
df = pd.DataFrame(empty_list)
df.drop(df.tail(1).index,inplace=True)
writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')

# df.fillna(0,inplace=True)

df.to_excel(writer, sheet_name='welcome', index=False,header=None)
writer.save()

# # # validated file
file=pd.read_excel('test.xlsx').replace(np.nan or np.NaT,' ',regex=True)

# loop to remove the special symbol
for column in file.columns:
      file[column] = file[column].astype(str).str.replace(r'[&^&]',' ',regex=True)
      file[column] = file[column].astype(str).str.replace(r'\s\s+',' ',regex=True)
     
# store the validated excel 
writer = pd.ExcelWriter('validated.xlsx', engine='xlsxwriter')
file.to_excel(writer, sheet_name='valid', index=False)
# file.drop(tail)
# file.drop(file.tail(1).index,inplace=True)
file = file.iloc[: , :-1]
writer.save()
print(file)
'''