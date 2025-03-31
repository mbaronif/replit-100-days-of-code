"""
As the CSV file is different from the proposed exercise, different
calculations will be made. Therefore, the output will be different
from the proposed exercise as well.
"""

import csv
# Writing to a CSV file

income = 0
expenditure = 0
netTotal = 0

#We have to add the full path for the file to be accessed.
with open("/Users/marianabaronifontana/Projects/replit-100-days-of-code/Day 54 - CSV Files/January.csv") as file:   
    reader = csv.DictReader(file)
    # Prompts the user for a date in the format DD/MM/YYYY.
    #selected_date = input("Enter the date (DD/MM/YYYY): ")
    
    for row in reader:
        income += float(row["Income"])
        expenditure += float(row["Expenditure"])
        netTotal += float(row["Net Total"])

    #Total Income
    print(f"\nTotal Income: ${income}")
    #Total Expenditure
    print(f"Total Expenditure: ${expenditure}")
    #Net total
    print(f"Net Total: ${netTotal}")
    #January's average income
    print(f"Average Income: ${income/31}")
    #January's average expenditure
    print(f"Average Expenditure: ${expenditure/31}")
    #January's average net total
    print(f"Average Net Total: ${netTotal/31}")
    print()

    file.seek(0)  # Reset file pointer to the beginning. It's necessary to reinitialize the reader
    # Find the total income for the selected date.
    reader = csv.DictReader(file)  # Reinitialize the reader
    for row in reader:
        print(f"Date: {row['Date']} Income: ${row['Income']}")
            