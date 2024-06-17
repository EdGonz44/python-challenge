import os
import csv


csvpath = os.path.join("..","PyPoll","Resources","election_data.csv")

total_number_votes = 0
stockham_count = 0
degette_count = 0
doane_count = 0
mistaken_count = 0
stockham_fraction = 0
degette_fraction = 0
doane_fraction = 0
result_decider = 0
result_compare = 0
winner_name = str
candidate_glossary = []
ballot_check = []
county_check = []
candidate_check = []
candidate_votes = []
candidate_fraction = 0
candidate_percentage = []




with open(csvpath) as csvfile:
    

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        ballot_check.append(row[0])
        county_check.append(row[1])
        candidate_check.append(row[2])

    for row in ballot_check:
        total_number_votes = total_number_votes + 1
    
    candidate_with_votes = set(candidate_check)

    unique_candidate_glossary = list(candidate_with_votes)
    sorted_candidates = sorted(unique_candidate_glossary)
   
  

    for row in candidate_check:
        if row == sorted_candidates[0]:
            stockham_count = stockham_count + 1
        elif row == sorted_candidates[1]:
            degette_count = degette_count + 1
        elif row == sorted_candidates[2]:
            doane_count = doane_count + 1
        else:
            mistaken_count = mistaken_count + 1
    
    candidate_votes = [stockham_count, degette_count, doane_count]


    for row in candidate_votes:
        candidate_fraction = (row / total_number_votes) * 100
        candidate_fraction = round(candidate_fraction, 3)
        candidate_percentage.append(candidate_fraction)
    
    # month_with_rate = list(zip( ,candidate_percentage))
    election_results = list(zip(sorted_candidates,candidate_percentage))

    for row in election_results:
        result_compare = row[1]
        if result_compare > result_decider:
            result_decider = result_compare
            winner_name = row[0]
        else:
            continue
    



    print("Election Results")
    print("--------------------")
    print(f"Total Votes {total_number_votes}")
    print("--------------------")
    print(f"{sorted_candidates[0]}: {candidate_percentage[0]}% ({stockham_count})")
    print(f"{sorted_candidates[1]}: {candidate_percentage[1]}% ({degette_count})")
    print(f"{sorted_candidates[2]}: {candidate_percentage[2]}% ({doane_count})")
    print(f"Winner: {winner_name}")


# Specify the file to write to
output_path = os.path.join("..", "PyPoll", "analysis","Analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline= '') as csvfile:


    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=' ')


    csvwriter.writerow(["Election","Results"])
    csvwriter.writerow(["---------------------"])
    csvwriter.writerow(["Total", "Votes:", {total_number_votes}])
    csvwriter.writerow(["--------------------"])
    csvwriter.writerow(["Charles", "Casper", "Stockham", f"{candidate_percentage[0]}%", f"({stockham_count})"])
    csvwriter.writerow(["Diana", "DeGette", f"{candidate_percentage[1]}%", f"({degette_count})"])
    csvwriter.writerow(["Raymon", "Anthony", "Doane:", f"{candidate_percentage[2]}%", f"({doane_count})"])
    csvwriter.writerow(["--------------------"])
    csvwriter.writerow(["Winner:",])


