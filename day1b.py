import pandas as pd

input_file = 'data.xlsx'  
data = pd.read_excel(input_file)

group1 = ['Commercial Vehicle & Construction Equipment', 'Healthcare Finance (HCF/EF/RML)']
group2 = ['Home Loans', 'Educational Loans', 'Personal Loan']
group3 = ['Agri & MFI', 'Auto Loans', 'Credit Card', 'Other Retail', 'Staff Loans', 'Two Wheeler', 'MFI']
lap = ['LAP']
sme = ['SME & MSME']
wsb = ['WSB']

def save_group_to_excel(group, group_name):
    group_data = data[data['Vertical'].isin(group)]
    output_file = group_name+'.xlsx'
    group_data.to_excel(output_file, index=False)

save_group_to_excel(group1, 'Commercial_Healthcare')
save_group_to_excel(group2, 'Home_Education_Personal')

vertical_data1 = data[data['Vertical'] == 'LDR/ODFD']
vertical_data1.to_excel('LDR-ODFD.xlsx', index=False)

for vertical in group3:
    vertical_data = data[data['Vertical'] == vertical]
    output_file =vertical+'.xlsx'
    vertical_data.to_excel(output_file, index=False)

lap_data = data[data['Vertical'].isin(lap) & ~data['CLIENT_ID'].isin(data[data['Vertical'].isin(sme)]['CLIENT_ID'])]
sme_data = data[data['Vertical'].isin(sme) & ~data['CLIENT_ID'].isin(data[data['Vertical'].isin(wsb)]['CLIENT_ID'])]
wsb_data = data[data['Vertical'].isin(wsb) & data['CLIENT_ID'].isin(data[data['Vertical'].isin(sme)]['CLIENT_ID'])]

lap_data.to_excel('LAP.xlsx', index=False)
sme_data.to_excel('SME_MSME.xlsx', index=False)
wsb_data.to_excel('WSB.xlsx', index=False)
print('SMA file sorted successfully!')
