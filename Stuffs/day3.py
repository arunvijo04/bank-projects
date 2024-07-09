import pandas as pd

# Read the original Excel file
original_file = 'path_to_your_file.xlsx'
df = pd.read_excel(original_file)

# Define the vertical column and the verticals of interest
vertical_column = 'Vertical'
verticals = ['Vertical1', 'Vertical2', 'Vertical3']  # Add more verticals if needed
preferred_verticals = ['Vertical1', 'Vertical2']  # The order defines the preference

# Define the columns you want to keep in the output files
columns_to_keep = ['Column1', 'Column2', 'Column3']  # Add the actual column names you need

# Function to filter and save data
def filter_and_save_data(df, vertical, filename):
    filtered_df = df[df[vertical_column] == vertical][columns_to_keep]
    filtered_df.to_excel(filename, index=False)

# Handle the preferred verticals
df_preferred = pd.DataFrame()
for vertical in preferred_verticals:
    df_current = df[df[vertical_column] == vertical]
    df = df[~df.index.isin(df_current.index)]  # Remove these rows from the main dataframe
    df_preferred = pd.concat([df_preferred, df_current])

# Save preferred verticals data
df_preferred = df_preferred[columns_to_keep]
df_preferred.to_excel('preferred_verticals_data.xlsx', index=False)

# Save remaining data
df_remaining = df[columns_to_keep]
df_remaining.to_excel('remaining_verticals_data.xlsx', index=False)

print("Data successfully saved into separate Excel files.")
