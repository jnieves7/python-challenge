#!/usr/bin/env python
# coding: utf-8

# In[115]:


import csv
import os
file_to_load = os.path.join(".", "Resources", "budget_data.csv")
file_to_output = os.path.join(".", "budget_analysis.txt")

total_months = 0
total_net = 0

net_change_list = []

month_of_changes= []

greatest_increase = [" ", 0]
greatest_decrease = [" ", 99999999999999]


with open(file_to_load) as financial_data:
    csvreader = csv.reader(financial_data, delimiter=',')
    csv_header = next(csvreader)
    #print(f"Header: {csv_header}")


    first_row = next(csvreader)
    #print(first_row[1])
    #total_net = total_net + int(first_row[1])
    #print(total_net)

    previous_net = int(first_row[1])

    total_months = total_months + 1

    
    for row in csvreader:
        
        #Calculate Total Months
        total_months = total_months + 1
        #print(row)

        #Calculate Net Profits
        total_net = total_net + int(row[1])
        #print(total_net)


        #Calculate the Average Change
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list.append(net_change)


        #Calculate the Greatest Increase in Profits
        if(net_change > greatest_increase[1]):
            greatest_increase [0] = row[0]
            greatest_increase [1] = net_change

        if(net_change < greatest_decrease[1]):
            greatest_decrease [0] = row[0]
            greatest_decrease [1] = net_change


        #Calculate the Greatesst Decrease in Profits
net_monthly_average = sum(net_change_list)/len(net_change_list)

    
output = (
    f"Financial Analysis\n"
    f"------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Net: ${total_net}\n"
    f"Average Change: ${net_monthly_average:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)
print(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
   


# In[ ]:





# In[ ]:




