import pandas as pd
import os

# Create processed folder if it doesn't exist
os.makedirs("data/processed", exist_ok=True)

# ----------------------------
# 01_fund_master.csv
# ----------------------------
df = pd.read_csv("data/raw/01_fund_master.csv")

df["launch_date"] = pd.to_datetime(df["launch_date"], errors="coerce")
df = df.drop_duplicates()

df.to_csv("data/processed/fund_master.csv", index=False)
print("✅ fund_master cleaned")

# ----------------------------
# 03_aum_by_fund_house.csv
# ----------------------------
df = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.drop_duplicates()

df.to_csv("data/processed/aum_by_fund_house.csv", index=False)
print("✅ aum_by_fund_house cleaned")

# ----------------------------
# 04_monthly_sip_inflows.csv
# ----------------------------
df = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

df = df.drop_duplicates()

df.to_csv("data/processed/monthly_sip_inflows.csv", index=False)
print("✅ monthly_sip_inflows cleaned")

# ----------------------------
# 05_category_inflows.csv
# ----------------------------
df = pd.read_csv("data/raw/05_category_inflows.csv")

df = df.drop_duplicates()

df.to_csv("data/processed/category_inflows.csv", index=False)
print("✅ category_inflows cleaned")

# ----------------------------
# 06_industry_folio_count.csv
# ----------------------------
df = pd.read_csv("data/raw/06_industry_folio_count.csv")

df = df.drop_duplicates()

df.to_csv("data/processed/industry_folio_count.csv", index=False)
print("✅ industry_folio_count cleaned")

# ----------------------------
# 09_portfolio_holdings.csv
# ----------------------------
df = pd.read_csv("data/raw/09_portfolio_holdings.csv")

df["portfolio_date"] = pd.to_datetime(df["portfolio_date"], errors="coerce")
df = df.drop_duplicates()

df.to_csv("data/processed/portfolio_holdings.csv", index=False)
print("✅ portfolio_holdings cleaned")

# ----------------------------
# 10_benchmark_indices.csv
# ----------------------------
df = pd.read_csv("data/raw/10_benchmark_indices.csv")

df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.drop_duplicates()

df.to_csv("data/processed/benchmark_indices.csv", index=False)
print("✅ benchmark_indices cleaned")

print("\n🎉 Remaining datasets cleaned successfully!")