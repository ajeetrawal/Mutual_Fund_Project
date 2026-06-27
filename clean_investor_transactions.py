import pandas as pd

# Read CSV
df = pd.read_csv("data/raw/08_investor_transactions.csv")

# Convert transaction date
df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors="coerce")

# Standardize transaction type
df["transaction_type"] = df["transaction_type"].str.strip().str.title()

mapping = {
    "Sip": "SIP",
    "Lumpsum": "Lumpsum",
    "Redemption": "Redemption"
}

df["transaction_type"] = df["transaction_type"].replace(mapping)

# Keep only amount > 0
df = df[df["amount_inr"] > 0]

# Keep valid KYC status
valid_kyc = ["Verified", "Pending", "Rejected"]
df = df[df["kyc_status"].isin(valid_kyc)]

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned file
df.to_csv("data/processed/investor_transactions.csv", index=False)

print("✅ investor_transactions cleaned successfully!")
print(df.head())