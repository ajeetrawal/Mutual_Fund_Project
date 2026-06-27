import pandas as pd
from sqlalchemy import create_engine

# SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

# Load cleaned CSV files
files = {
    "nav_history": "data/processed/nav_history.csv",
    "investor_transactions": "data/processed/investor_transactions.csv",
    "scheme_performance": "data/processed/scheme_performance.csv"
}

for table_name, file_path in files.items():
    df = pd.read_csv(file_path)
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f"✅ Loaded {table_name} ({len(df)} rows)")

print("\n🎉 SQLite database created successfully!")