import pandas as pd

# Read CSV
df = pd.read_csv("data/raw/07_scheme_performance.csv")

# Convert return columns to numeric
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Expense ratio should be between 0.1% and 2.5%
df = df[
    (df["expense_ratio_pct"] >= 0.1) &
    (df["expense_ratio_pct"] <= 2.5)
]

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned file
df.to_csv("data/processed/scheme_performance.csv", index=False)

print("✅ scheme_performance cleaned successfully!")
print(df.head())