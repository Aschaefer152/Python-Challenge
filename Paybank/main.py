# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
# Method 2: Improved Reading using CSV module

with open(csvpath, newline="", encoding="utf-8") as csvfile:

   # CSV reader specifies delimiter and variable that holds contents
   csvreader = csv.reader(csvfile, delimiter=',')


   # Read the header row first (skip this step if there is now header)
   csv_header = next(csvreader)
 
   #create the variables to import the financial analysis total of 5 varibales
   total_months= []
   total_sum = []
   monthly_changes = []

   
   # Read each row of data after the header
   for row in csvreader:
       #total_months+=1
       #total_sum += int(row[1])
       #if error, append the total months and total profit to corresponding units
       total_months.append(row[0])
       total_sum.append(int(row[1]))


   # need to iterate through the profits = monthly change
   for i in range(len(total_sum)-1):

       #take the difference and append to monthly changes
       monthly_changes.append(total_sum[i+1]-total_sum[i])  

   #get the min and max
   max_increase = max(monthly_changes)
   max_decrease= min(monthly_changes)

   #assign min max to the date
   max_increase_date = monthly_changes.index(max(monthly_changes)) + 1
   max_decrease_date = monthly_changes.index(min(monthly_changes)) + 1

   #print the analysis
   print("Financial Analysis")
   print("--------------------------------------")
   print(f"Total Months: + {len(total_months)}")
   print(f"Total: $ + {sum(total_sum)}")
   print(f"Average Change: {round(sum(monthly_changes)/len(monthly_changes),2)}")
   print(f"Greatest Increase in Profits: {total_months[max_increase_date]} (${(str(max_increase))})")
   print(f"Greatest Decrease in Profits: {total_months[max_decrease_date]} (${(str(max_decrease))})")