import os
import pandas as pd
import glob

path = os.getcwd() + "\downloads"
all_files = glob.glob(path + "/*.xlsx")
all_data = []

for file in all_files:
    df = pd.read_excel(file)
    all_data.append(df)

merged_df = pd.concat(all_data, ignore_index=True)
merged_df.drop_duplicates(subset=['Dátum', 'Nap', 'Év', 'Hozam (%)'], keep='first', inplace=True)
merged_df.sort_values(by='Dátum', inplace=True)
merged_df.to_excel('merged_file.xlsx', index=False)