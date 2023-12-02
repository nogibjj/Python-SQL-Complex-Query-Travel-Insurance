-- Query to analyze Travel Insurance Data by Income Group

-- CTE to categorize customers into income groups
WITH IncomeGroups AS (
    SELECT 
        id,
        CASE 
            WHEN AnnualIncome <= 500000 THEN 'Low Income'
            WHEN AnnualIncome > 500000 AND AnnualIncome <= 1000000 THEN 'Middle Income'
            ELSE 'High Income'
        END AS IncomeGroup
    FROM travel_insurance
)

-- Main Query to calculate insurance statistics by income group
SELECT 
    IG.IncomeGroup,
    COUNT(*) AS TotalCustomers,
    AVG(TI.Age) AS AverageAge,
    SUM(CASE WHEN TI.TravelInsurance = 1 THEN 1 ELSE 0 END) AS TotalInsured,
    ROUND((SUM(CASE WHEN TI.TravelInsurance = 1 THEN 1 ELSE 0 END) * 100.0) / COUNT(*), 2) AS InsuranceRate
FROM 
    travel_insurance TI
JOIN 
    IncomeGroups IG ON TI.id = IG.id
GROUP BY 
    IG.IncomeGroup
ORDER BY 
    TotalCustomers DESC;
