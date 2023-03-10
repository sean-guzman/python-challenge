import os
import csv

months = []
profit_loss = []
profit_loss_change = []

os.chdir(os.path.dirname(__file__))
budgetpath = os.path.join('Resources', 'budget_data.csv')

with open(budgetpath) as budgetfile:

    budgetreader = csv.reader(budgetfile, delimiter=',')
    budgetheader = next(budgetreader)

    # Move csv data into lists
    for row in budgetreader:
        months.append(row[0])
        profit_loss.append(row[1])

total = 0
current_change = 0
previous_change = 0

for i in profit_loss:
    
    # Calculate profit/loss total
    total = total + int(i)
    
    # Calculate profit/loss change from month to month
    if profit_loss.index(i) == 0:
        
        previous_change = int(i)
        profit_loss_change.append(0)
 
    else:
        current_change = int(i)
        profit_loss_change.append(int(current_change - previous_change))
        previous_change = current_change

# Calculate profit/loss change total
total_change = 0
for i in profit_loss_change:
    total_change = total_change + int(i)

# Calculate profit/loss change average
average_change = 0
average_change = round(total_change/int(len(profit_loss_change)-1),2)

# Search for max and min profit change and cross reference its index to find month
increase = 0
decrease = 0

increase_month = 0
decrease_month = 0

increase = max(profit_loss_change)
decrease = min(profit_loss_change)
increase_month = months[profit_loss_change.index(increase)]
decrease_month = months[profit_loss_change.index(decrease)]

print("\n")
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {increase_month} ${increase}")
print(f"Greatest Decrease in Profits: {decrease_month} ${decrease}")
print("----------------------------")

results_path = os.path.join("analysis", "results.txt")

with open(results_path, 'w') as results_file:

    results_file.write("Financial Analysis\n")
    results_file.write("----------------------------\n")
    results_file.write(f"Total Months: {len(months)}\n")
    results_file.write(f"Total: ${total}\n")
    results_file.write(f"Average Change: ${average_change}\n")
    results_file.write(f"Greatest Increase in Profits: {increase_month} ${increase}\n")
    results_file.write(f"Greatest Decrease in Profits: {decrease_month} ${decrease}\n")
    results_file.write("----------------------------")
