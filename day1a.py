import pandas as pd

original_file = 'data.xlsx'
df = pd.read_excel(original_file)

category_column = 'Vertical'
categories_group1 = ['Commercial Vehicle & Construction Equipment', 'Healthcare Finance (HCF/EF/RML)']
categories_group2 = ['Home Loans', 'Educational Loans', 'Personal Loan']

categories = [
    'Agri & MFI', 'Auto Loans', 'Credit Card', 'Other Retail',
    'LDR/ODFD', 'Staff Loans', 'Two Wheeler', 'MFI',
    'LAP', 'SME & MSME', 'WSB'
]

columns_to_keep = ['BRANCH_CODE', 'BRANCH_NAME', 'ZONE', 'ACNUM', 'ACCNAME', 'PRODUCT_DESCRIPTION',
                   'DERIVEDLIMIT', 'BALANCE', 'REASON', 'DEFAULT_AMT', 'CLIENT_ID', 'UCIC_ID',
                   'DEFAULT_DAT', 'EMI', 'OPEN_DATE', 'NO_OD_DAYS', 'CLIENT_SMA', 'ACNT_SMATYPE', 'ASON', 'Vertical']

df_categories = {cat: df[df[category_column] == cat] for cat in categories}
df_categories['LAP'] = df[df[category_column].str.contains('LAP', na=False)]
df_categories['SME & MSME'] = df[df[category_column] == 'SME & MSME']
df_categories['WSB'] = df[df[category_column] == 'WSB']

sme_client_ids = set(df_categories['SME & MSME']['CLIENT_ID'])
wsb_client_ids = set(df_categories['WSB']['CLIENT_ID'])
all_sme_wsb_client_ids = sme_client_ids.union(wsb_client_ids)

lap_client_ids = set(df_categories['LAP']['CLIENT_ID'])
non_sme_lap_client_ids = lap_client_ids.difference(sme_client_ids)
df_categories['LAP'] = df[df['CLIENT_ID'].isin(non_sme_lap_client_ids) & df[category_column].str.contains('LAP', na=False)]

multi_vertical_client_ids = df[df['CLIENT_ID'].isin(all_sme_wsb_client_ids)]['CLIENT_ID']
df_categories['WSB'] = df[df['CLIENT_ID'].isin(multi_vertical_client_ids) & df[category_column].str.contains('WSB', na=False)]

for cat in df_categories:
    df_categories[cat] = df_categories[cat][columns_to_keep]

for cat, data in df_categories.items():
    output_file = cat.replace(' ', '_') + '.xlsx'
    data.to_excel(output_file, index=False)

print("Data successfully saved into separate Excel files.")
