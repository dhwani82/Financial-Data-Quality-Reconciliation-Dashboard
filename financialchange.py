import pandas as pd

system_a = pd.read_csv(r"d:\Projects\Financial Data Quality & Reconciliation Dashboard\system_a.csv")
system_b = pd.read_csv(r"d:\Projects\Financial Data Quality & Reconciliation Dashboard\system_b.csv")

merged = system_a.merge(
    system_b,
    on="Transaction_ID",
    how="left",
    suffixes=("_A", "_B")
)

merged["Missing_in_B"] = merged["Amount_B"].isna()

merged["Amount_Mismatch"] = (
    merged["Amount_A"] != merged["Amount_B"]
)

merged["Data_Issue"] = (
    merged["Missing_in_B"] | merged["Amount_Mismatch"]
)

merged.to_csv(r"d:\Projects\Financial Data Quality & Reconciliation Dashboard\reconciliation_report.csv", index=False)

print(merged.head())
print("Reconciliation report saved successfully.")