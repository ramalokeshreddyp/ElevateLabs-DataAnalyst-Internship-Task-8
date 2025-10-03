import pandas as pd 

df = pd.read_csv("Sample - Superstore.csv", encoding="latin-1")

# Preview first row
print(df.head())
print(df.info())

# Remove Null Values
df.dropna(subset=['Order Date', 'Region', 'Category', 'Sales', 'Profit'], inplace = True)

# Remove Duplicates
df.drop_duplicates(inplace = True)

# Save Cleaned Dataset
df.to_csv("Superstore_cleaned.csv", index = False)