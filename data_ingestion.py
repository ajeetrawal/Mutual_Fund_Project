import pandas as pd
import os

folder = "data/raw"

csv_files = [f for f in os.listdir(folder) if f.endswith(".csv")]

for file in csv_files:
    print("\n" + "="*60)
    print("FILE:", file)

    df = pd.read_csv(os.path.join(folder, file))

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())