# Customer Churn Prediction & Retention Strategy

An end-to-end data analytics and machine learning project analyzing customer churn behavior and developing a predictive model to identify high-risk customers and drive retention-focused business decisions.

---

## Executive Summary

Customer churn represents a direct threat to recurring revenue and long-term customer lifetime value.

This project moves beyond descriptive churn analysis by:

- identifying key behavioral and contractual drivers of churn
- building a predictive model to estimate churn probability
- quantifying revenue at risk
- translating insights into prioritized retention strategies

Key finding:

> High-risk customers represent approximately **$23,961.83 in monthly revenue at risk**, indicating that targeted retention strategies can deliver significant financial impact.

---

## Business Problem

The business is experiencing customer churn but lacks:

- visibility into which customers are most likely to churn
- understanding of what factors drive churn behavior
- a framework to prioritize retention efforts

---

## Objectives

1. Identify key drivers of customer churn
2. Predict churn probability at the customer level
3. Quantify business impact of churn risk
4. Recommend data-driven retention strategies

---

## Dataset

- Source: Telco Customer Churn dataset
- Records: 7,043 customers
- Features: customer demographics, services, billing, contract type

---

## Analytical Approach

### 1. Data Preparation
- cleaned missing and inconsistent values
- converted `TotalCharges` to numeric
- encoded categorical variables
- removed non-informative identifiers

### 2. Exploratory Analysis
- churn rates by contract, payment method, and services
- tenure and monthly charge behavior
- segment-level churn patterns

### 3. Predictive Modeling
- logistic regression model
- stratified train/test split
- class imbalance handled via weighting
- pipeline with preprocessing and modeling

---

## Model Performance

| Metric | Value |
|--------|-------|
| Accuracy | 73.74% |
| Precision | 50.34% |
| Recall | 78.88% |
| ROC-AUC | 0.8421 |

### Interpretation

The model demonstrates strong ability to identify customers likely to churn.

- High **recall (78.88%)** ensures most churners are captured
- Moderate precision is acceptable in retention scenarios
- ROC-AUC of **0.8421** indicates strong predictive separation

---

## Key Drivers of Churn

The model identifies the following as the most influential factors:

### High Churn Risk
- month-to-month contracts
- fiber optic internet users
- electronic check payment method
- lack of online security and tech support

### Lower Churn Risk
- two-year contracts
- customers with bundled services and support

---

## Estimated Business Impact

The model identifies **370 high-risk customers** with churn probability greater than or equal to 70%.

| Metric | Value |
|--------|-------|
| Average Monthly Revenue per Customer | $64.76 |
| Monthly Revenue at Risk | $23,961.83 |
| Potential Revenue Saved (10% retention) | $2,396.18 |

### Insight

Even modest improvements in retention can generate meaningful revenue protection.

---

## Strategic Decision Insight

The business faces a critical tradeoff:

- invest in acquiring new customers
- invest in retaining existing customers

Given the concentration of revenue among high-risk customers, this analysis suggests:

> **Retention-focused investment is likely to deliver higher ROI than equivalent acquisition spend.**

---

## Model Use for Decision-Making

With strong recall and ROC-AUC:

- the model is effective for identifying high-risk customers
- false positives are acceptable given retention campaign economics
- missing a churner is more costly than targeting a non-churner

---

## Prioritized Action Plan

### 1. Convert Month-to-Month Customers
- highest churn segment
- offer incentives for long-term contracts
- highest impact opportunity

### 2. Target High-Risk Customers
- use churn probability scoring
- focus retention efforts on top-risk segments
- improves campaign efficiency

### 3. Improve Service Bundles
- promote security and support services
- reduce churn driven by service dissatisfaction

---

## Project Outputs

- `outputs/tables/churn_model_metrics.csv`
- `outputs/tables/top_15_churn_drivers.csv`
- `outputs/tables/customer_churn_scored_sample.csv`
- `outputs/tables/churn_business_impact_summary.csv`
- `models/churn_model_summary.json`

---

## Analytical Considerations

- dataset does not include acquisition channel data
- results are observational, not causal
- customer behavior may vary seasonally
- model performance may vary across segments

---

## Conclusion

This project demonstrates how churn analysis can be transformed into a decision-making system by combining:

- behavioral analysis
- predictive modeling
- business impact estimation
- strategic prioritization

The results show that targeted retention strategies can materially reduce revenue loss and improve long-term customer value.
