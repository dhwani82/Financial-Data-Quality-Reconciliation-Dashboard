import pandas as pd
import numpy as np

np.random.seed(42)

n = 100

system_a = pd.DataFrame({
    "Transaction_ID": range(1, n+1),
    "Amount": np.random.randint(100, 1000, n),
    "Date": pd.date_range("2024-01-01", periods=n),
    "Status": "SUCCESS"
})

system_b = system_a.copy()

for i in np.random.choice(n, 10):
    system_b.loc[i, "Amount"] += np.random.randint(-100, 100)

system_b = system_b.drop(np.random.choice(system_b.index, 5))

system_a.to_csv(r"d:\Projects\Financial Data Quality & Reconciliation Dashboard\system_a.csv", index=False)
system_b.to_csv(r"d:\Projects\Financial Data Quality & Reconciliation Dashboard\system_b.csv", index=False)

print(system_a.head())
print(system_b.head())
print("CSVs saved successfully.")