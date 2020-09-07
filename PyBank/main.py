# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Get Current working directory of main.py file
cwd = os.getcwd()

# Set path for file

csvpath = os.path.join(cwd, "Resources", "budget_data.csv")
csvpath = os.path.normcase(csvpath)
csvpath = os.path.normpath(csvpath)

output_file = os.path.join(cwd, "analysis","output.csv")
output_file = os.path.normcase(output_file)
output_file = os.path.normpath(output_file)


# Lists variables to iterate through each row
months = []
profit_and_loss = []
monthly_profit_and_loss_change = []

# Read the data file and print output
with open(csvpath,'r',encoding="utf-8") as bugdet_csv_file:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(bugdet_csv_file, delimiter=',')

    # Skip the header row first
    csv_header = next(csvreader)
    
    # Uncomment below line to print the stored csv_header
    print(f"CSV Header: {csv_header}")
    
    # Read each row of data after the header and add values to the list variables
    for row in csvreader:
        
        # Add each row in the file to list variables
        months.append(row[0])
        profit_and_loss.append(float(row[1]))
        
    # Utlize list comprehension to calculate monthly profit and loss change
    for i in range(len(profit_and_loss)-1):
        monthly_profit_and_loss_change.append(round(profit_and_loss[i+1]-profit_and_loss[i],1))
    
    # Fetch the Greatest increase in profits and Greatest decrease in losses
    grtst_incr_in_profits = max(monthly_profit_and_loss_change)
    grtst_decr_in_losses = min(monthly_profit_and_loss_change)
    
    # Search the index greatest increase in profits and greatest decrease in losses month and year
    grtst_incr_in_profits_mnth_and_yr = monthly_profit_and_loss_change.index(grtst_incr_in_profits) + 1
    grtst_decr_in_profits_mnth_and_yr = monthly_profit_and_loss_change.index(grtst_decr_in_losses) + 1
    
    # Assign Financial analysis Key Performance Indicators Column Headers
    fin_analysis_kpi = ["  Total Months:",
                        "  Total:",
                        "  Average Change:",
                        "  Greatest Increase in Profits:",
                        "  Greatest Decrease in Profits:"
                       ]
    
    # Calulate the Financial analysis Key Performance Indicators Values into a list variable: 
    fin_analysis_kpi_values = [
                                len(months),
                                "$" + str(sum(profit_and_loss)),
                                "$" + str(round(sum(monthly_profit_and_loss_change)/len(monthly_profit_and_loss_change),2)),
                                str(months[grtst_incr_in_profits_mnth_and_yr]) +
                                " ($" + str(grtst_incr_in_profits) + ")",
                                str(months[grtst_decr_in_profits_mnth_and_yr]) +
                                " ($" + str(grtst_decr_in_losses) + ")"
                              ]

# Zip all two lists together into tuples for writing to file
fin_results_file = list(zip(fin_analysis_kpi, fin_analysis_kpi_values))

# Writing to file
#with open(output_file, "w") as datafile:
#    writer = csv.writer(datafile)
#    for j, k in fin_results_file:
#        print(j, k, end='\n', file=datafile)

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["  Financial Analysis"])
    writer.writerow(["  ----------------------------"])    

    # print out to file:
    for j, k in fin_results_file:
        print(j, k, end='\n', file=datafile)

# Zip all two lists together into tuples for printing to terminal
fin_results_ter = list(zip(fin_analysis_kpi, fin_analysis_kpi_values))
    
# print  out to terminal:
print("  Financial Analysis")
print("  ----------------------------")

# print out to terminal:
for l, m in fin_results_ter:
    print(l, m, end='\n')
