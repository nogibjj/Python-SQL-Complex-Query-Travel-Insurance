import csv
import sqlite3

# Load the TravelInsurancePrediction dataset into the SQLite database
def load_travel_insurance(dataset="TravelInsurancePrediction.csv"):
    conn = sqlite3.connect('travel_insurance.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS travel_insurance')
    cursor.execute('''
    CREATE TABLE travel_insurance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Age INTEGER,
        EmploymentType TEXT,
        GraduateOrNot TEXT,
        AnnualIncome INTEGER,
        FamilyMembers INTEGER,
        ChronicDiseases INTEGER,
        FrequentFlyer TEXT,
        EverTravelledAbroad TEXT,
        TravelInsurance INTEGER
    )
    ''')
    with open(dataset, 'r', encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cursor.execute('''
                INSERT INTO travel_insurance (
                    Age, EmploymentType, GraduateOrNot, AnnualIncome, 
                    FamilyMembers, ChronicDiseases, FrequentFlyer, 
                    EverTravelledAbroad, TravelInsurance
                ) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                row["Age"], row["Employment Type"], row["GraduateOrNot"], row["AnnualIncome"],
                row["FamilyMembers"], row["ChronicDiseases"], row["FrequentFlyer"],
                row["EverTravelledAbroad"], row["TravelInsurance"]
            ))
    conn.commit()
    conn.close()
    print("Data loaded successfully!")

# CRUD functions for the TravelInsurancePrediction dataset
def create_travel_insurance_entry(data):
    with sqlite3.connect('travel_insurance.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO travel_insurance (
                Age, EmploymentType, GraduateOrNot, AnnualIncome, 
                FamilyMembers, ChronicDiseases, FrequentFlyer, 
                EverTravelledAbroad, TravelInsurance
            ) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', data)
        conn.commit()
        print("Entry created successfully!")

def read_all_travel_insurance_entries():
    with sqlite3.connect('travel_insurance.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM travel_insurance")
        return cursor.fetchall()

def read_travel_insurance_entry_by_id(entry_id):
    with sqlite3.connect('travel_insurance.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM travel_insurance WHERE id=?", (entry_id,))
        entry = cursor.fetchone()
    if entry:
        print(f"Entry found: {entry}")
    else:
        print("Entry not found.")
    return entry

def update_travel_insurance_entry(entry_id, data):
    with sqlite3.connect('travel_insurance.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE travel_insurance 
            SET Age=?, EmploymentType=?, GraduateOrNot=?, AnnualIncome=?, 
                FamilyMembers=?, ChronicDiseases=?, FrequentFlyer=?, 
                EverTravelledAbroad=?, TravelInsurance=?
            WHERE id=?
        ''', data + (entry_id,))
        conn.commit()
        print("Entry updated successfully!")

def delete_travel_insurance_entry(entry_id):
    with sqlite3.connect('travel_insurance.db') as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM travel_insurance WHERE id=?", (entry_id,))
        conn.commit()
        print("Entry deleted successfully!")

def main():
    load_travel_insurance()
    create_travel_insurance_entry((25, 'Private Sector', 'Yes', 500000, 4, 0, 'No', 'No', 1))
    update_travel_insurance_entry(1, (26, 'Private Sector', 'Yes', 600000, 5, 1, 'Yes', 'Yes', 0))
    print(read_travel_insurance_entry_by_id(1))
    delete_travel_insurance_entry(1)

if __name__ == "__main__":
    main()
