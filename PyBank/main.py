import os
import csv

#sets file
csvpath = os.path.join("..", "PyBank", 'budget_data.csv')

#declaring variables
total_months = []
total_profit = []
profit_change = []

#open and read file
with open(csvpath, 'r', newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")

#skips the headers
    header = next(csvreader)

#loops through file and appends the appropriate lists    
    for i in csvreader:
        total_months.append(i[0])
        total_profit.append(int(i[1]))
        
    for j in range(1, len(total_profit)):
        profit_change.append(total_profit[j]-total_profit[j-1])

#calculates max and min    
greatest_increase = max(profit_change)
greatest_decrease = min(profit_change)

#calculates greatest increase and decrease
greatest_increase_month = profit_change.index(max(profit_change)) + 1
greatest_decrease_month = profit_change.index(min(profit_change)) + 1

#prints the results
print("Financial Analysis")
print("_________________________")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: ${round(sum(profit_change) / len(profit_change), 2)}")
print(f"Greatest Increase In Profits: {total_months[greatest_increase_month]} (${(str(greatest_increase))})")
print(f"Greatest Decrease In Profits: {total_months[greatest_decrease_month]} (${(str(greatest_decrease))})")

#sets output file
txtpath = os.path.join("..", "PyBank", 'Analysis.txt')

#opens and writes the results
with open(txtpath, 'w') as txtfile:
    print("Financial Analysis", file=txtfile)
    print("_________________________", file=txtfile)
    print(f"Total Months: {len(total_months)}", file=txtfile)
    print(f"Total: ${sum(total_profit)}", file=txtfile)
    print(f"Average Change: ${round(sum(profit_change) / len(profit_change), 2)}", file=txtfile)
    print(f"Greatest Increase In Profits: {total_months[greatest_increase_month]} (${(str(greatest_increase))})", file=txtfile)
    print(f"Greatest Decrease In Profits: {total_months[greatest_decrease_month]} (${(str(greatest_decrease))})", file=txtfile)    
