'''
Simple utility to convert CSV to Parquet format and back to pandas DataFrame.
Parquet advantages:
- Better compression
- Preserves data types
- Faster read/write
- Works well with big data tools

Requirements: pandas, pyarrow
pip install pandas pyarrow
'''

import pandas as pd
import os

# Load CSV file
df_csv = pd.read_csv('final_data.csv')

# Save as Parquet 
df_csv.to_parquet('final_data.parquet', compression='snappy')

# Load Parquet back
df_parquet = pd.read_parquet('final_data.parquet')

# Compare file sizes
csv_size = os.path.getsize('final_data.csv')
parquet_size = os.path.getsize('final_data.parquet')
print(f"CSV size: {csv_size/1024:.2f} KB")
print(f"Parquet size: {parquet_size/1024:.2f} KB")
print(f"Compression ratio: {csv_size/parquet_size:.2f}x")

# Usage Example:
print("\nFirst few rows:")
print(df_parquet.head())
print("\nData types:")
print(df_parquet.dtypes)