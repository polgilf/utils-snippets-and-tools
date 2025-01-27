import pandas as pd

# File paths
file_path = 'productes-beneficiari-2014-04-07.csv'
output_path = 'cleaned_file.csv'
column_name = 'Producte'  # Replace with the column name to clean

# Load the CSV file
df = pd.read_csv(file_path)

# Clean the specified column
if column_name in df.columns:
    df[column_name] = df[column_name].str.replace(r'<span class="baixa">', '', regex=True)
    df[column_name] = df[column_name].str.replace(r'</span>', '', regex=True)

# Save the cleaned CSV file
df.to_csv(output_path, index=False)

print(f"Cleaned CSV file saved to {output_path}")