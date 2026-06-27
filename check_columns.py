# # import pandas as pd

# # df = pd.read_csv("data/raw/01_fund_master.csv")

# # print("\nUnique Fund Houses:")
# # print(df["fund_house"].unique())

# # print("\nCategories:")
# # print(df["category"].unique())

# # print("\nSub Categories:")
# # print(df["sub_category"].unique())

# # print("\nRisk Categories:")
# # print(df["risk_category"].unique())
# import pandas as pd

# files = [
#     "02_nav_history.csv",
#     "08_investor_transactions.csv",
#     "07_scheme_performance.csv"
# ]

# for file in files:
#     print("\n" + "="*50)
#     print(file)

#     df = pd.read_csv(f"data/raw/{file}")

#     print("Columns:")
#     print(df.columns.tolist())
import pandas as pd
import os

folder = "data/raw"

for file in sorted(os.listdir(folder)):
    if file.endswith(".csv"):
        print("\n" + "="*60)
        print(file)
        df = pd.read_csv(os.path.join(folder, file))
        print(df.columns.tolist())