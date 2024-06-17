import os
import csv
# csvpath = os.path.join('..', 'Resources', 'contacts.csv')

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
# output_path = os.path.join('..', 'PyBank',"analysis", "analysis.csv")


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)







