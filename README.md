# Customer Churn Prediction & Retention Strategy

An end-to-end data analytics and machine learning project analyzing telecom customer churn behavior, predicting high-risk customers, and translating findings into retention-focused business decisions.

---

## Executive Summary

Customer churn is a direct threat to recurring revenue and long-term customer value.

This project moves beyond descriptive churn analysis by:

- identifying key behavioral and contractual drivers of churn
- building a logistic regression model to predict churn probability
- estimating revenue at risk from high-risk customers
- recommending prioritized retention actions

### Headline Findings

- **ROC-AUC:** 0.8421
- **Recall:** 78.88%
- **370** customers identified as high-risk
- **$23,961.83** estimated monthly revenue at risk
- **$2,396.18** potential monthly revenue saved if 10% of high-risk customers are retained

---

## Business Problem

The telecom business needs to understand:

- which customers are most likely to churn
- what factors drive churn risk
- how churn risk translates into revenue exposure
- which retention actions should be prioritized first

Without this visibility, retention spending is broad, inefficient, and less likely to protect high-value customers.

---

## Objectives

1. Identify the strongest drivers of churn
2. Predict churn probability at the customer level
3. Estimate business impact of churn risk
4. Recommend data-driven retention strategies

---

## Dataset

- **Source:** Telco Customer Churn dataset
- **Records:** 7,043 customers
- **Features:** demographics, services, billing, contract type, churn status

Key variables include:

- `Contract`
- `tenure`
- `MonthlyCharges`
- `PaymentMethod`
- `InternetService`
- `Churn`

---

## Analytical Approach

### 1. Data Preparation
- cleaned and validated customer records
- converted `TotalCharges` to numeric
- removed non-informative identifiers
- prepared categorical and numeric features for modeling

### 2. Exploratory Churn Analysis
- churn rate by contract type
- churn rate by payment method
- churn rate by internet service
- average tenure and monthly charges by churn status

### 3. Predictive Modeling
- logistic regression model
- stratified train/test split
- balanced class weighting
- preprocessing pipeline with one-hot encoding and imputation

---

## Model Performance

| Metric | Value |
|--------|-------|
| Accuracy | 73.74% |
| Precision | 50.34% |
| Recall | 78.88% |
| ROC-AUC | 0.8421 |

### Interpretation

The model performs well for retention use cases:

- high recall helps capture most likely churners
- moderate precision is acceptable when retention campaigns can tolerate some false positives
- ROC-AUC of 0.8421 indicates strong separation between churn and non-churn customers

In this context, missing a true churner is more costly than contacting a customer who may not churn.

---

## Key Drivers of Churn

### Higher Churn Risk
- month-to-month contracts
- fiber optic internet users
- electronic check payment method
- customers without online security
- customers without tech support

### Lower Churn Risk
- two-year contracts
- customers with support and bundled services

These patterns suggest that contract structure, support services, and billing behavior are central to churn risk.

---

## Estimated Business Impact

The model identified **370 high-risk customers** with churn probability greater than or equal to 70%.

| Metric | Value |
|--------|-------|
| Average Monthly Revenue per Customer | $64.76 |
| Monthly Revenue at Risk | $23,961.83 |
| Potential Monthly Revenue Saved (10% retained) | $2,396.18 |

### Strategic Insight

Even modest retention improvements can protect meaningful recurring revenue. This makes churn prediction useful not just for analysis, but for revenue-focused decision-making.

---

## Strategic Decision Insight

The business faces a critical tradeoff:

- invest more in acquiring new customers
- invest more in retaining existing customers

Given the volume of revenue attached to high-risk customers, this analysis suggests that:

> **Retention-focused investment is likely to deliver higher ROI than equivalent acquisition spend.**

---

## Prioritized Action Plan

### 1. Convert Month-to-Month Customers
- highest churn-risk segment
- strongest contract-related intervention opportunity

### 2. Target High-Risk Customers Using Churn Scores
- focus campaigns on customers with the highest predicted churn probability
- improve retention efficiency and reduce wasted effort

### 3. Improve Service Bundle Retention
- promote online security and tech support bundles
- address service-related churn drivers

---

## Dashboard

### Customer Churn Risk Dashboard

![Customer Churn Risk Dashboard](images/telco-customer-churn-dashboard.png)

This dashboard highlights:

- overall churn KPIs
- churn concentration across contract types
- churn patterns by payment method and internet service
- business-facing segment insights for retention planning

### Tableau Deliverable

- `dashboard/telco-customer-churn-dashboard.twbx`

---

## Project Outputs

- `outputs/tables/churn_model_metrics.csv`
- `outputs/tables/churn_confusion_matrix.csv`
- `outputs/tables/churn_classification_report.csv`
- `outputs/tables/top_15_churn_drivers.csv`
- `outputs/tables/customer_churn_scored_sample.csv`
- `outputs/tables/churn_business_impact_summary.csv`
- `models/churn_model_summary.json`

---

## SQL Analysis

SQLite queries were used to validate core churn metrics and segment-level business questions, including:

- total customers
- churned customers
- overall churn rate
- churn rate by contract type
- churn rate by payment method

See `sql/churn_analysis.sql`.

---

## Analytical Considerations

- the dataset does not include acquisition channel or customer satisfaction data
- results are observational rather than causal
- churn behavior may vary over time or across unobserved factors
- model performance may differ across customer subsegments

---

## Conclusion

This project transforms churn analysis from a descriptive dashboard into a decision-support system by combining:

- churn segmentation
- predictive modeling
- business impact estimation
- retention prioritization

The core conclusion is clear:

**Targeted retention actions can materially reduce revenue loss and should be prioritized over broad, untargeted churn interventions.**
