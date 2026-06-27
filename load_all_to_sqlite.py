import pandas as pd
from sqlalchemy import create_engine
import os

# SQLite Database
engine = create_engine("sqlite:///bluestock_mf.db")

# Processed folder
folder = "data/processed"

# Sabhi CSV files load karo
for file in os.listdir(folder):
    if file.endswith(".csv"):
        table_name = file.replace(".csv", "")
        df = pd.read_csv(os.path.join(folder, file))

        df.to_sql(table_name, engine, if_exists="replace", index=False)

        print(f"✅ {table_name} loaded ({len(df)} rows)")

print("\n🎉 All datasets loaded into SQLite successfully!")