import pandas as pd
from pathlib import Path

df = pd.read_csv("data/customer_churn_cleaned.csv")

output_dir = Path("data")
output_dir.mkdir(exist_ok=True)

overall = pd.DataFrame({
    "metric": ["total_customers", "churned_customers", "churn_rate_pct"],
    "value": [len(df), int(df["Churn_Flag"].sum()), round(df["Churn_Flag"].mean() * 100, 2)]
})

contract_churn = (
    df.groupby("Contract", as_index=False)["Churn_Flag"]
    .mean()
    .rename(columns={"Churn_Flag": "churn_rate"})
)
contract_churn["churn_rate"] = (contract_churn["churn_rate"] * 100).round(2)

internet_churn = (
    df.groupby("InternetService", as_index=False)["Churn_Flag"]
    .mean()
    .rename(columns={"Churn_Flag": "churn_rate"})
)
internet_churn["churn_rate"] = (internet_churn["churn_rate"] * 100).round(2)

payment_churn = (
    df.groupby("PaymentMethod", as_index=False)["Churn_Flag"]
    .mean()
    .rename(columns={"Churn_Flag": "churn_rate"})
)
payment_churn["churn_rate"] = (payment_churn["churn_rate"] * 100).round(2)

tenure_summary = (
    df.groupby("Churn", as_index=False)
    .agg(avg_tenure=("tenure", "mean"), avg_monthly_charges=("MonthlyCharges", "mean"))
)
tenure_summary["avg_tenure"] = tenure_summary["avg_tenure"].round(2)
tenure_summary["avg_monthly_charges"] = tenure_summary["avg_monthly_charges"].round(2)

overall.to_csv(output_dir / "overall_churn_summary.csv", index=False)
contract_churn.to_csv(output_dir / "churn_by_contract.csv", index=False)
internet_churn.to_csv(output_dir / "churn_by_internet_service.csv", index=False)
payment_churn.to_csv(output_dir / "churn_by_payment_method.csv", index=False)
tenure_summary.to_csv(output_dir / "churn_tenure_monthlycharges_summary.csv", index=False)

print("Saved:")
print("- data/churn_overview_summary.csv")
print("- data/churn_rate_by_contract.csv")
print("- data/churn_rate_by_internet_service.csv")
print("- data/churn_rate_by_payment_method.csv")
print("- data/churn_tenure_charge_summary.csv")

print("\nOverall churn summary:")
print(overall)

print("\nChurn by contract:")
print(contract_churn.sort_values("churn_rate", ascending=False))
