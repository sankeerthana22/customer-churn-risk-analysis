import pandas as pd
from pathlib import Path

input_path = Path("data/raw_telco_customer_churn.csv")
output_path = Path("data/customer_churn_cleaned.csv")

df = pd.read_csv(input_path)

# Standardize TotalCharges
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# Fill missing TotalCharges with 0 for customers with very low tenure/new accounts
df["TotalCharges"] = df["TotalCharges"].fillna(0)

# Standardize target
df["Churn_Flag"] = df["Churn"].map({"Yes": 1, "No": 0})

# Clean text columns
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].astype(str).str.strip()

df.to_csv(output_path, index=False)

print("Cleaned file saved:", output_path)
print("Shape:", df.shape)
print("Missing values:")
print(df.isna().sum()[df.isna().sum() > 0])
print("\nChurn distribution:")
print(df["Churn"].value_counts())
