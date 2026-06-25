import pandas as pd

master = pd.read_csv("data/raw/01_fund_master.csv")
nav = pd.read_csv("data/raw/02_nav_history.csv")

master_codes = set(master["amfi_code"])
nav_codes = set(nav["amfi_code"])

missing_codes = master_codes - nav_codes

print("Total AMFI Codes in Fund Master:", len(master_codes))
print("Total AMFI Codes in NAV History:", len(nav_codes))
print("Missing Codes:", len(missing_codes))

if len(missing_codes) > 0:
    print("\nMissing Code List:")
    print(list(missing_codes)[:20])
else:
    print("\nAll AMFI Codes Found ✅")