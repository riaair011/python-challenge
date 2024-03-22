
#text output
print("Financial Analysis")
print("----------------------------")

#importing necessary packages 
import os
import csv

#opening the file 
budget_csv=os.path.join("Resources","budget_data.csv")

#open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter =",")

    #skipping the first row
    csv_header= next(csv_file)

    
    months = []
    profit = []
    changes = []
    for row in csv_reader:
        months.append(row[0])
        profit.append(int(row[1]))
    
        #total months
    print(f"Total Months: {str(len(months))}")
       
    total_profit = sum(profit)
    print(f"Profit: ${str(total_profit)}")
        
    for val in range(1,len(profit)):
        diff= int(profit[val])-int(profit[val-1])
        changes.append(diff)
            
    average = sum(changes)/len(months)

    print(f"Average Change: ${str(average)}")

        
        #max
    max_change= max(changes)
    max_month = changes.index(max_change)
    print(f"Greatest Increase in Profits: {str(months[max_month])} (${str(max(changes))})")


        #print minimum
    min_prof = min(changes)
    min_month = changes.index(min_prof)
    time_min = months[min_month]
    print(f"Greatest Decrease in Profits: {str(time_min)} (${str(min_prof)})")

        


        