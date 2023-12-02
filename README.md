[![CI](https://github.com/zhuminghui17/python-template/actions/workflows/cicd.yml/badge.svg)](https://github.com/zhuminghui17/python-template/actions/workflows/cicd.yml)

## Overview
This Python script is designed to manage the Travel Insurance Prediction dataset using SQLite. It provides functionality to load the dataset into a SQLite database, and to perform Create, Read, Update, and Delete (CRUD) operations on the data.

## Features
- Database Initialization: Loads the Travel Insurance Prediction dataset into a SQLite database.
- CRUD Operations: Supports creating, reading, updating, and deleting records in the database.
- User-friendly Messages: Prints informative messages to the console for each operation, enhancing the user experience.

## Dataset Structure
The Travel Insurance Prediction dataset includes the following columns:
- Age
- Employment Type
- GraduateOrNot
- AnnualIncome
- FamilyMembers
- ChronicDiseases
- FrequentFlyer
- EverTravelledAbroad
- TravelInsurance

## Prerequisites
Before running the script, ensure you have the following installed:

- Python 3
- SQLite3
- Pandas (for reading the dataset)


## Getting Started
Setting Up the Environment:
- Ensure Python 3 is installed on your system.
- Install Pandas using pip install pandas if not already installed.
- Placing the Dataset:
    - Place your "TravelInsurancePrediction.csv" dataset in the same directory as the script.
- Running the Script:
- Run the script using Python. For example, python travel_insurance_script.py.

## Usage
The script defines the following functions:

- `load_travel_insurance()`: Loads the dataset into a SQLite database.
- `create_travel_insurance_entry(data)`: Creates a new entry in the database.
- `read_all_travel_insurance_entries()`: Reads all entries from the database.
- `read_travel_insurance_entry_by_id(entry_id)`: Reads a specific entry by ID.
- `update_travel_insurance_entry(entry_id, data)`: Updates an existing entry.
- `delete_travel_insurance_entry(entry_id)`: Deletes an entry from the database.

An example main() function demonstrates the usage of these functions.




