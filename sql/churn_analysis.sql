-- Total customers
SELECT COUNT(*) AS total_customers
FROM churn_data;

-- Total churned customers
SELECT COUNT(*) AS churned_customers
FROM churn_data
WHERE Churn = 'Yes';

-- Overall churn rate
SELECT ROUND(
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
    2
) AS churn_rate_percentage
FROM churn_data;

-- Churn rate by contract type
SELECT
    Contract,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS churn_rate_percentage
FROM churn_data
GROUP BY Contract
ORDER BY churn_rate_percentage DESC;

-- Churn rate by payment method
SELECT
    PaymentMethod,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS churn_rate_percentage
FROM churn_data
GROUP BY PaymentMethod
ORDER BY churn_rate_percentage DESC;
