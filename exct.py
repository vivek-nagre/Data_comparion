import pandas as pd
df1 = pd.read_excel('Floor DEV.xlsx')
df2 = pd.read_excel('Floor POC.xlsx')

df_join = df1.merge(right = df2,
                    left_on = df1.columns.to_list(),
                    right_on = df2.columns.to_list(),
                    how = 'outer')

df1.rename(columns = lambda x : x + '_S')
df2.rename(columns = lambda x : x + '_T', inplace = True)


df_join = df1.merge(right = df2,
                    left_on = df1.columns.to_list(),
                    right_on = df2.columns.to_list(),
                    how = 'outer')

# sorting the excel record on matching (JOIN)
records_present_in_df1_not_in_df2 = df_join.loc[df_join[df2.columns.to_list()].isnull().all(axis = 1), df1.columns.to_list()]

records_present_in_df2_not_in_df1 = df_join.loc[df_join[df1.columns.to_list()].isnull().all(axis = 1), df2.columns.to_list()]


# present in SRC but not in TGT
print("Data presnt in SRC but not in TGT")
print(records_present_in_df1_not_in_df2)

df1.to_excel('diffrance.xlsx',sheet_name='Source_data')
df2.to_excel('diffrance.xlsx',sheet_name='Target_data')
# records_present_in_df1_not_in_df2.to_excel('diffrance.xlsx',sheet_name='differance')
output = df1.copy()
with pd.ExcelWriter('Tririga.xlsx') as writer:  
    df1.to_excel(writer, sheet_name='SRC_data',index=False)
    df2.to_excel(writer, sheet_name='TARGET',index=False)
    records_present_in_df1_not_in_df2.to_excel(writer, sheet_name='Differance',index=False)