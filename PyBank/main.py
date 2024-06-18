import os
import csv
# Create path needed to open resources folder and access
# csv with budget data.

csvpath = os.path.join('..', 'PyBank','Resources', 'budget_data.csv')

# Declare variables and necessary lists.
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


# Open csvfile with csvpath
    
with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

   
# Isolate the header from the csv 
    csv_header = next(csvreader)

    # Run a loop that seperates the columns in the data into two columns:
    # one for the dates when stocks were sold, one for the profits/losses
    # made on that date.
    for row in csvreader:
        monthly_note.append(row[0])
        monthly_data.append(row[1])
    
    # Convert the string values in the list for monthly_data and convert
    # them into integers
    monthly_number = [eval(i) for i in monthly_data]

    # Loop through the list for monthly_number and count the total number of
    # iterations. The count of iterations will act as the count of months.
    for row in monthly_number:
        months = months + 1
    
    # Loop through the list for monthly_number, and update the monthly_profit_change
    # variable to equal the current iteration in the list. 
    # Find the total net profit by adding the monthly_profit change to 
    # net_profit (which was initialized at 0) and then update net_profit to equal the sum. 
    for row in monthly_number:
        monthly_profit_change = row
        net_profit = net_profit + monthly_profit_change
    
    # Iterate through the monthly_number list. Update rate_holder to equal 
    # the current iteration value and then find the difference between
    # rate_holder and profit_holder. Update profit_holder to equal the current
    # iteration value. This will determine the change in value between iterations,
    # and then append the value of rate_change to the empty list: change_data.
    for row in monthly_number:
        rate_holder = row
        rate_change = rate_holder - profit_holder
        profit_holder = row 
        change_data.append(rate_change)
   
    # Reset profit_holder for the next loop
    profit_holder= 0 

    # Loop through change_data list and set rate_change equal to current iteration
    # value. Use conditionals to determine if the the iteration value is positive
    # or negative, with the first conditional setting used to dismiss the first value
    # due to it not technically having rate change since it was the first value.
    # The other conditionals will then add positive or negative iteration values to a 
    # growing sum of their respecitve integer types.
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

    # Find average change in profit by finding the difference between the sum
    # of all the positive and negative changes in profit, and then dividing them
    # by the total size of the change_data list minus one in order to dismiss the first 
    # list value that is not necessary. Then convert average_profit into 
    # a rounded integer by two decimal points.
    average_profit = (pos_profit + neg_profit) / (len(change_data) - 1)
    average_profit = round(average_profit,2)


    # Combine the lists of monthly_note which holds the dates of each stock change
    # and the change in profits between months that occured on that date into a tuple.
    month_with_rate = list(zip(monthly_note, change_data))

    # Loop the the tuple and update the rate_holder to equal the stock change
    # of that iteration in the tuple. Use conditionals to determine if the current
    # iteration has a stock change value that was larger, or lower, than the variable
    # holding the largest positive or negative change in stock change value. 
    # If either conditions are met, then the variable holding greatest inc/dec
    # will update to equal the current iteration value, and the month and change value
    # of that iteration will be updated to a variable holding the month and respective
    # change value that experienced the greatest inc/dec in stock change value.
    # Otherwise the loop re-updated rate_holder to current iteration and moves to next 
    # iteration.

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
            
    # Print statements that describe a Financial Analysis of the total months,
    # total net profit, average change in profit, and the months that experienced
    # the greatest change in stock value with the change in parenthesis.
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


    # Use csvwriter to write the print statements onto a csvfile.
    csvwriter.writerow(["Financial","Analysis"])
    csvwriter.writerow(["---------------------"])
    csvwriter.writerow(["Total", "Months", months])
    csvwriter.writerow(["Total", (f"${net_profit}")])
    csvwriter.writerow(["Average", "Change", (f"${average_profit}")])
    csvwriter.writerow(["Greatest", "Increase", "In", "Profits:", month_extreme_inc, (f"${number_extreme_inc}")])
    csvwriter.writerow(["Greatest", "Decrease", "in", "Profits:", month_extreme_dec, (f"${number_extreme_dec}")])
  



   
        

    

    








