import pandas as pd

original_file = 'data.xlsx'
df = pd.read_excel(original_file)

category_column = 'Vertical'
category1 = 'Commercial Vehicle & Construction Equipment'
category2 = 'Personal Loan'
category3 = 'Home Loans'
category4 = 'Educational Loans'
category5 = 'Staff Loans'
category6 = 'Two Wheeler'
category7 = 'MFI'
category8 = 'Healthcare Finance (HCF/EF/RML)'

columns_to_keep = ['BRANCH_CODE', 'BRANCH_NAME', 'ZONE','ACNUM','ACCNAME','PRODUCT_DESCRIPTION','DERIVEDLIMIT','BALANCE','REASON','DEFAULT_AMT','CLIENT_ID','UCIC_ID','DEFAULT_DAT','EMI','OPEN_DATE','NO_OD_DAYS','CLIENT_SMA','ACNT_SMATYPE','ASON','Vertical']

df_category1 = df[df[category_column] == category1]
df_category2 = df[df[category_column] == category2]
df_category3 = df[df[category_column] == category3]
df_category4 = df[df[category_column] == category4]
df_category5 = df[df[category_column] == category5]
df_category6 = df[df[category_column] == category6]
df_category7 = df[df[category_column] == category7]
df_category8 = df[df[category_column] == category8]

df_category1 = df_category1[columns_to_keep]
df_category2 = df_category2[columns_to_keep]
df_category3 = df_category3[columns_to_keep]
df_category4 = df_category4[columns_to_keep]
df_category5 = df_category5[columns_to_keep]
df_category6 = df_category6[columns_to_keep]
df_category7 = df_category7[columns_to_keep]
df_category8 = df_category8[columns_to_keep]

output_file1 = category1+'.xlsx'
output_file2 = category2+'.xlsx'
output_file3 = category3+'.xlsx'
output_file4 = category4+'.xlsx'
output_file5 = category5+'.xlsx'
output_file6 = category6+'.xlsx'
output_file7 = category7+'.xlsx'
output_file8 = category8+'.xlsx'


df_category1.to_excel(output_file1, index=False)
df_category2.to_excel(output_file2, index=False)
df_category3.to_excel(output_file3, index=False)
df_category4.to_excel(output_file4, index=False)
df_category5.to_excel(output_file5, index=False)
df_category6.to_excel(output_file6, index=False)
df_category7.to_excel(output_file7, index=False)
df_category8.to_excel(output_file8, index=False)

print("Data successfully saved into two separate Excel files.")
