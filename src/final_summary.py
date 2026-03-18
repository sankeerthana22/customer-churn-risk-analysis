import pandas as pd

overall = pd.read_csv("data/churn_overview_summary.csv")
contract = pd.read_csv("data/churn_rate_by_contract.csv")
internet = pd.read_csv("data/churn_rate_by_internet_service.csv")
payment = pd.read_csv("data/churn_rate_by_payment_method.csv")
model_results = pd.read_csv("data/churn_model_comparison.csv")
tenure = pd.read_csv("data/churn_tenure_charge_summary.csv")

top_contract = contract.sort_values("churn_rate", ascending=False).iloc[0]
lowest_contract = contract.sort_values("churn_rate", ascending=True).iloc[0]
best_model = model_results.sort_values("roc_auc", ascending=False).iloc[0]
highest_payment = payment.sort_values("churn_rate", ascending=False).iloc[0]
highest_internet = internet.sort_values("churn_rate", ascending=False).iloc[0]

summary = pd.DataFrame({
    "insight": [
        "Overall churn rate",
        "Highest churn contract type",
        "Lowest churn contract type",
        "Highest churn internet service",
        "Highest churn payment method",
        "Best model by ROC-AUC"
    ],
    "value": [
        f"{overall.loc[overall['metric']=='churn_rate_pct', 'value'].iloc[0]}%",
        f"{top_contract['Contract']} ({top_contract['churn_rate']}%)",
        f"{lowest_contract['Contract']} ({lowest_contract['churn_rate']}%)",
        f"{highest_internet['InternetService']} ({highest_internet['churn_rate']}%)",
        f"{highest_payment['PaymentMethod']} ({highest_payment['churn_rate']}%)",
        f"{best_model['model']} ({best_model['roc_auc']})"
    ]
})

summary.to_csv("data/churn_business_summary.csv", index=False)

print("Saved: data/churn_business_summary.csv")
print(summary)
print("\nTenure / Monthly Charges summary:")
print(tenure)
