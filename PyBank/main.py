import os
import csv
# csvpath = os.path.join('..', 'Resources', 'contacts.csv')

csvpath = os.path.join('..', 'PyBank','Resources', 'budget_data.csv')
# output_path = os.path.join('..', 'PyBank',"analysis", "analysis.csv")

months = 0
net_profit = 0
monthly_profit_change = 0
rate_holder = 0
profit_holder = 0
pos_profit = 0
neg_profit = 0
rate_change = 0
average_profit = 0
greatest_inc = 0
greatest_dec = 0

month_extreme_inc = str
month_extreme_dec = str
number_extreme_dec = 0
number_extreme_inc = 0
monthly_note = []
monthly_data = []
change_data = []



    
with open(csvpath) as csvfile:
    

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # csv_header = next(csvreader)
    # print(csvreader)

    csv_header = next(csvreader)
    for row in csvreader:
        monthly_note.append(row[0])
        monthly_data.append(row[1])
    
    monthly_number = [eval(i) for i in monthly_data]

    months = 0
    for row in monthly_number:
        months = months + 1
    
    for row in monthly_number:
        monthly_profit_change = row
        net_profit = net_profit + monthly_profit_change
    
    for row in monthly_number:
        rate_holder = row
        rate_change = rate_holder - profit_holder
        profit_holder = row 
        change_data.append(rate_change)
    # print(change_data)
    
    profit_holder= 0 

    for row in change_data:
        rate_change = row
        if profit_holder == 0:
            profit_holder = rate_change
        
        elif rate_change > 0:
            profit_holder = rate_change
            pos_profit = pos_profit + profit_holder
        
        else:
            profit_holder = rate_change
            neg_profit = neg_profit + profit_holder


    average_profit = (pos_profit + neg_profit) / (len(change_data) - 1)
    average_profit = round(average_profit,2)

    month_with_rate = list(zip(monthly_note, change_data))

    for row in month_with_rate:
        rate_holder = row[1]
        if rate_holder > greatest_inc:
            greatest_inc = rate_holder
            month_extreme_inc = row[0]
            number_extreme_inc = row[1]

        elif rate_holder < greatest_dec:
            greatest_dec = rate_holder
            month_extreme_dec = row[0]
            number_extreme_dec = row[1]

        else:
            rate_holder = row[1]
            

    print("Financial Analysis")
    print("---------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${net_profit}")
    print(f"Average Change: ${average_profit}")
    print(f"Greatest Increase in Profits: {month_extreme_inc} ({number_extreme_inc})")
    print(f"Greatest Decrease in Profits: {month_extreme_dec} ({number_extreme_dec})")

    # Specify the file to write to
output_path = os.path.join("..", "PyBank", "analysis","Analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline= '') as csvfile:


    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=' ')


    # Write the first row (column headers)
    # csvwriter.writerow(['First Name', 'Last Name', 'SSN'])
    csvwriter.writerow(["Financial","Analysis"])
    csvwriter.writerow(["---------------------"])
    csvwriter.writerow(["Total", "Months", months])
    csvwriter.writerow(["Total", (f"${net_profit}")])
    csvwriter.writerow(["Average", "Change", (f"${average_profit}")])
    csvwriter.writerow(["Greatest", "Increase", "In", "Profits:", month_extreme_inc, (f"${number_extreme_inc}")])
    csvwriter.writerow(["Greatest", "Decrease", "in", "Profits:", month_extreme_dec, (f"${number_extreme_dec}")])
  



   
        

    

    








