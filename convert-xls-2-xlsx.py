import os
import pandas as pd
from xls2xlsx import XLS2XLSX

# Specify the folder containing .xls files
current_dir = os.getcwd()
folder_path = os.path.join(current_dir, 'Week_230122')

# Get a list of all files in the folder
file_list = os.listdir(folder_path)

# Loop through the files and convert .xls to .xlsx
for file in file_list:
    if file.endswith('.xls'):
        # Create the full file paths for input and output files
        input_file_path = os.path.join(folder_path, file)
        output_file_path = os.path.splitext(input_file_path)[0] + '.xlsx'
        
        # Convert xls to xlsx
        x2x = XLS2XLSX(input_file_path)
        x2x.to_xlsx(output_file_path)

        # Optionally, you can remove the original .xls file
        os.remove(input_file_path)

print("Conversion complete!")