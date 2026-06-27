import pandas as pd

# Read CSV
df = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Sort by AMFI code and date
df = df.sort_values(["amfi_code", "date"])

# Forward fill missing NAV
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Remove duplicates
df = df.drop_duplicates()

# Keep only valid NAV
df = df[df["nav"] > 0]

# Save cleaned file
df.to_csv("data/processed/nav_history.csv", index=False)

print("✅ nav_history cleaned successfully!")
print(df.head())