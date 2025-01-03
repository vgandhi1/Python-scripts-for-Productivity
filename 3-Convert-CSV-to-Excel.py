import os
import pandas as pd

def csv_to_excel_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'): 
            csv_file = os.path.join(folder_path, filename)
            excel_file = os.path.join(folder_path, filename.replace('.csv', '.xlsx'))
            
            try:
                df = pd.read_csv(csv_file)
                df.to_excel(excel_file, index=False)
                print(f"Converted: {csv_file} -> {excel_file}")
            except Exception as e:
                print(f"Failed to convert {csv_file}: {e}")

csv_to_excel_folder(r"/path/to/your/folder")
