# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print("Financial Analysis")
    print("--------------------------------------")

    #create the variables to import the financial analysis total of 5 varibales
    total_months=0
    total_s = 0
    #average_change = 0
    #great_in = 0
    #great_de = 0
    
    # Read each row of data after the header
    for row in csvreader:
        total_months+=1
        total_s= sum()

    print("Total Months :" + str(total_months))
    print("Total :" + int(total_s))