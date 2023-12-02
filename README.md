[![CI](https://github.com/zhuminghui17/python-template/actions/workflows/cicd.yml/badge.svg)](https://github.com/zhuminghui17/python-template/actions/workflows/cicd.yml)

# Travel Insurance Data Analysis

## Overview
This project analyzes a Travel Insurance dataset using SQLite and Python. It involves creating complex SQL queries to extract meaningful insights from the data, such as customer demographics and insurance purchase rates. The project includes scripts for executing these queries and a testing suite to ensure query accuracy and reliability.

## Project Structure
- `TravelInsurancePrediction.csv`: The dataset containing travel insurance data.
- `query.sql`: Contains the complex SQL query used for data analysis.
- `query.py`: A Python script to execute the SQL query from query.sql and handle database interactions.
- `README.md`: This file, explaining the project setup and usage.

## Setup
1. Database Setup
- Ensure SQLite is installed on your system.
- Place the TravelInsurancePrediction.csv file in your project directory.

2.Python Environment
Python 3.x is required.
Install necessary Python packages:
```
pip install sqlite3
```

## Usage
1. Loading Data into SQLite
Use your preferred method to import TravelInsurancePrediction.csv into a SQLite database.

2. Running the Query
Execute query.py to run the SQL query stored in query.sql and view the results:
```python query.py```

## Example Result
Upon executing query.py, you can expect output similar to the following, which shows a breakdown of customers by income group:
```
('High Income', 891, 29.375982042648708, 459, 51.52)
('Middle Income', 730, 30.134246575342466, 191, 26.16)
('Low Income', 366, 29.33606557377049, 61, 16.67)
```
These results represent the income group, total number of customers, average age, total number of insured customers, and insurance rate (in percentage) for each group.

## Explanation and Expected Results:
1. Common Table Expression (CTE) - IncomeGroups:
    - This part of the query creates a temporary table named IncomeGroups to classify customers into different income groups based on their AnnualIncome.
    - Customers with an annual income of up to 500,000 are categorized as 'Low Income', those between 500,000 and 1,000,000 as 'Middle Income', and above 1,000,000 as 'High Income'.

2. Main Query:
- The main query performs a JOIN operation between the travel_insurance table and the IncomeGroups CTE using the id column.
- It then groups the data by the IncomeGroup defined in the CTE.

3. Aggregations and Calculations:
- TotalCustomers: Counts the total number of customers in each income group.
- AverageAge: Calculates the average age of customers in each group.
- TotalInsured: Sums the number of customers who have purchased travel insurance (where TravelInsurance is 1) in each group.
- InsuranceRate: Calculates the percentage of customers in each group who have purchased travel insurance. This is done by dividing the TotalInsured by TotalCustomers and multiplying by 100 for percentage. It is then rounded to two decimal places.

4. Sorting:
- The results are ordered by TotalCustomers in descending order, showing the groups with the most customers first.


### Expected Results:
The query will output a table with each income group and the following columns: TotalCustomers, AverageAge, TotalInsured, and InsuranceRate. This will provide insights into how income levels correlate with age, the number of customers, and their likelihood of purchasing travel insurance.