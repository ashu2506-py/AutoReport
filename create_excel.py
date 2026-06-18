import pandas as pd

df = pd.read_csv("sample_data/sales.csv")

df.to_excel("sample_data/sales.xlsx", index=False)

print("Excel file created successfully!")