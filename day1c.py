import pandas as pd

input_file = 'data.xlsx'  
data = pd.read_excel(input_file)

sme_mappings_file = 'sme_mappings.xlsx'
sme_mappings = pd.read_excel(sme_mappings_file)

lap = ['LAP']
sme = ['SME & MSME']
wsb = ['WSB']

lap_data = data[data['Vertical'].isin(lap) & ~data['CLIENT_ID'].isin(data[data['Vertical'].isin(sme)]['CLIENT_ID'])]
lap_data.to_excel('LAP.xlsx', index=False)

wsb_data = data[data['Vertical'].isin(sme) & data['CLIENT_ID'].isin(data[data['Vertical'].isin(wsb)]['CLIENT_ID']) | data['Vertical'].isin(wsb)]
wsb_data.to_excel('WSB.xlsx', index=False)

sme_data = data[data['CLIENT_ID'].isin(sme_mappings['CLIENT_ID'])]
sme_data.to_excel('SME.xlsx', index=False)

msme_old_data = data[(data['Vertical'].isin(sme)) & ~data['CLIENT_ID'].isin(sme_mappings['CLIENT_ID']) & data['CLIENT_ID'].isin(data[data['Vertical'].isin(wsb)]['CLIENT_ID'])]
msme_new_data = data[(data['Vertical'].isin(sme)) & ~data['CLIENT_ID'].isin(sme_mappings['CLIENT_ID']) & (data['PRODUCT_DESCRIPTION'].str.startswith('MSME'))]

msme_old_data.to_excel('MSME_Old.xlsx', index=False)
msme_new_data.to_excel('MSME_New.xlsx', index=False)

print('All files sorted and saved successfully!')
