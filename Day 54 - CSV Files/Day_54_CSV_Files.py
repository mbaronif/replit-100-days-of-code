"""
As the CSV file is different from the proposed exercise, different
calculations will be made. Therefore, the output will be different
from the proposed exercise as well.
"""

import csv
# Writing to a CSV file

#We have to add the full path for the file to be accessed.
with open("/Users/marianabaronifontana/Projects/replit-100-days-of-code/Day 54 - CSV Files/January.csv") as file:   
    reader = csv.DictReader(file)
    for row in reader:
        #Some exercises to test the code:
        #print(row)
        #print(row["Date"], row["Net Total"])
        #print(row["Date"], row["Net Total"], row["Income"], row["Expenditure"])


        #To do:
        #Find the total income and expenditure for the month of January.
        #Find the average income and expenditure for the month of January.
        #Find the total income and expenditure for each day of the month.
        #Find the average income and expenditure for each day of the month.