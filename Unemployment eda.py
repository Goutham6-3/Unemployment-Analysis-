# --- Import necessary libraries ---
import pandas as pd

# --- Step 1: Load the dataset ---
# Change the path if your file is stored somewhere else
df = pd.read_csv("Unemployment in India.xlsx.csv")

# --- Step 2: Understand the data ---
# Display first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Show basic information about columns & data types
print("\nDataset info:")
print(df.info())

# Show summary statistics (helps spot weird values)
print("\nSummary statistics:")
print(df.describe(include='all'))

# --- Step 3: Check for missing values ---
print("\nMissing values in each column:")
print(df.isnull().sum())

# --- Step 4: Rename columns if needed (make them simpler & lowercase) ---
# This helps avoid errors later
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

print("\nColumns after renaming:")
print(df.columns)

# --- Step 5: Drop duplicates (if any) ---
df = df.drop_duplicates()
print(f"\nShape after dropping duplicates: {df.shape}")

# --- Step 6: Fix data types if needed ---
# For example, if 'date' column is object, convert it to datetime
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

# --- Step 7: Handle missing values ---
# This depends on the data: you could drop them or fill them.
# Let's drop rows with missing unemployment rate for now.
if 'unemployment_rate' in df.columns:
    df = df.dropna(subset=['unemployment_rate'])

# --- Step 8: Final check ---
print("\nFinal dataset info:")
print(df.info())

print("\nFirst few cleaned rows:")
print(df.head())

# --- Step 9: Save cleaned data to new file ---
df.to_csv("cleaned_unemployment_data.csv", index=False)
print("\nCleaned data saved as 'cleaned_unemployment_data.csv'")