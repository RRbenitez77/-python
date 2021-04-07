import os
import csv

#Declare file Location path.join
budget_data = os.path.join("resources","budget_data.csv")

# Create empty list for rows
#def print_profit_losses(budget_data):
total_months = []
total_net_profit_losses = []
Change_in_profit_losses= []
monthly_profit_change = []
Greatest_decrease_losses_date_amount= []
max_increase_months = []
Financial_Analysis= []

#Open and Read csv 
with open(budget_data, 'r') as csv_file_1:

    # Store the contents of budget_data.csv
    csv_reader = csv.reader(csv_file_1,delimiter=",")

    #skip header labels 
    header = next (csv_reader)

    #Iterate through the rows stored in file
    for row in csv_reader:

        #Append with Total months and Total profit/losses
        total_months.append(row[0])
        total_net_profit_losses.append(int(row[1]))
        
        #Iterate through the profits for monthly change 
        for i in range(len(total_net_profit_losses)-1):
         monthly_profit_change.append(total_net_profit_losses[i +1]-total_net_profit_losses[i])

        #Find the monthly profit change with maximum and minimum 
        #max_increase_months = monthly_profit_change.index(max(monthly_profit_change))+1 
        #max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) +1

    #Print Statements loop through

    print (f"Financial Analysis")
    print (f".................................")
    print (f"Total Months: {len(total_months)}")
    print (f"Total:{sum(total_net_profit_losses)}")
    print (f"Average Change : {round(sum(monthly_profit_change)/len(monthly_profit_change) ,2)}")
    #print (f"Greatest Increase in Profits:{total_months[max_increase_months]} (${(int(max_increase_value))})")
    #print (f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(int(max_decrease_value))})")

#Output files
output_file =path("resources," "Financial_Analysis.txt")

with open(output_file,"w") as file: 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------")  
    file.write("\n")
    file.write(f"Total Months:{len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_net_profit_losses)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in profits:{total_months[max_increase_months]} (${(str(max_increase_value))})")
    file.write("\n")
    #file.write(f"Greatest Decrease in profits: {[total_months[max_decrease_month]} (${(str(max_decrease_value))})")