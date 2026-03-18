# Customer Churn Risk Analysis

## Overview
This project analyzes telecom customer churn data to quantify overall churn risk, identify high-risk customer segments, and present business-ready insights through a Tableau dashboard. The workflow includes data cleaning, segmentation analysis, metric computation, and visualization.

## Dataset
The dataset represents telecom customer information, including contract type, tenure, payment method, internet service, and churn status.  
- Source: Telco Customer Churn dataset (public dataset)  
- Size: ~7,000 customer records  
- Key fields: churn status, contract type, tenure, monthly charges  

## Business Problem
Customer churn directly impacts revenue and growth. Businesses need to understand:
- how many customers are leaving
- the overall churn rate
- which customer segments are most at risk  

This enables targeted retention strategies and reduces revenue loss.

## Objectives
- Measure total customers
- Calculate churned customers
- Compute overall churn rate
- Identify churn patterns across contract types
- Build a business-friendly dashboard for decision-making

## Methodology
1. Data ingestion from raw CSV dataset  
2. Data cleaning and preprocessing using Python  
3. Feature segmentation (contract, payment method, internet service)  
4. Aggregation of churn metrics  
5. Export of processed datasets  
6. Dashboard creation in Tableau  

## Tools Used
- Python  
- Pandas  
- Tableau 
- SQLite  
- CSV  

## Dashboard Preview
![Telco Customer Churn Dashboard](images/telco-customer-churn-dashboard.png)

## Key Insights
- Total customers: **7,043**  
- Churned customers: **1,869**  
- Overall churn rate: **26.54%**  
- Month-to-month contracts have significantly higher churn rates  
- Long-term contracts reduce churn risk  

## Project Files
- `dashboard/telco-customer-churn-dashboard.twbx` — Tableau dashboard  
- `images/telco-customer-churn-dashboard.png` — dashboard preview  
- `src/` — data cleaning, segmentation, analysis, and summary scripts  
- `data/` — raw and processed datasets  

## How to Use
- Open the Tableau workbook:  
  `dashboard/telco-customer-churn-dashboard.twbx`  
- Review processed data in `data/processed/`  
- Inspect analysis scripts in `src/`  

## Conclusion
Customer churn is a significant business risk in the telecom dataset, with month-to-month customers contributing disproportionately to churn. The dashboard provides a clear, business-oriented view of churn metrics and supports data-driven retention strategies.

## Business Recommendations
- Encourage migration from month-to-month to longer-term contracts through incentives or bundled pricing.
- Introduce targeted retention offers for high-risk segments identified in the dashboard.
- Monitor churn trends by contract and payment method to prioritize intervention strategies.

## Data Dictionary (Key Fields)
- `Churn` — whether the customer has churned (Yes/No)  
- `Contract` — contract type (Month-to-month, One year, Two year)  
- `tenure` — number of months the customer has stayed  
- `MonthlyCharges` — monthly billing amount  
- `PaymentMethod` — customer payment type  
- `InternetService` — type of internet service  

## Limitations
- Dataset size is limited (~7k records), which may not fully represent large-scale telecom behavior.  
- Analysis is primarily descriptive and does not include advanced causal inference.  
- External factors (competitor pricing, customer satisfaction) are not included.

## How to Reproduce
1. Review raw dataset in `data/raw/`  
2. Run preprocessing and analysis scripts in `src/`  
3. Open Tableau dashboard:
   `dashboard/telco-customer-churn-dashboard.twbx`  
4. Validate outputs using files in `data/processed/`


## SQL Analysis
SQLite queries were used to validate core churn metrics and perform segment-level aggregation.

Key SQL analyses include:
- total customer count
- churned customer count
- overall churn rate
- churn rate by contract type
- churn rate by payment method

See `sql/churn_analysis.sql` for the query set used in this project.
