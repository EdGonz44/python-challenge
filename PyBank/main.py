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
monthly_note = []
monthly_data = []
change_data = []


# def total_months(monthly_note):
#     months = 0
#     for row in monthly_note:
#         months = months + 1
   
   
    

# def total_net_profit(monthly_data):
#     net_profit = 0
#     monthly_profit_change = 0
#     for row in monthly_data:
#         monthly_profit_change = int(row)
#         net_profit = net_profit + monthly_profit_change
    
    

# def average_profit_change():
#     average_profit = total_net_profit / total_months
#     print(f"Average Change: ${average_profit}")


    
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

    

        
   
    # for i  in enumerate(monthly_number)
    #     profit_holder = i
    #     monthly_profit_change = next(i)

#    for row in change_data:
#         rate_change = row
#         if profit_holder > 0:
#             rate_change = profit_holder
#             pos_profit = pos_profit + rate_change

#         elif profit_holder < 0:
#             rate_change = profit_holder
#             neg_profit = neg_profit + rate_change


    # print(change_data[79])
    # print(len(change_data))
        


    # for row in monthly_number:
    #     monthly_profit_change = row
    #     profit_holder = next(row)
    # #     if 
    # #     rate_change.append(profit_holder - monthly_profit_change)
    # # print(rate_change)
        
   




    # print(f"negative total: {neg_profit}")
    # print(f"positive total profit: {pos_profit}")

    print(f"Total Months: {months}")
    print(f"Total: ${net_profit}")
    print(f"Average Change: ${average_profit}")


    # print(f"CSV Header: {csv_header}")
    
    # for row in csvreader:
    #     print(row[0])

    # total_months(csv_lists)
    # total_net_profit(csv_lists)
    
   
        

    

    








