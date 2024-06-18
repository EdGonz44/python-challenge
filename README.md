# python-challenge

## PyBank
This folder contains the main script that analyzes the csv file held in the folder "Resources", 
and then outputs a csv file into the analysis folder.
### Main Script
The script used to make the financial analysis [Financial Analysis Script](https://github.com/EdGonz44/python-challenge/blob/main/PyBank/main.py)

The purpose of the main script is to create a financial analysis of the profit and losses of in stock values
over an interval of time using a csv file for reference. The script determine the total months in the time frame, as well as the total net profit made during this time frame. It then finds the change in profit between each months, and then determines the average 
change in profit over the entire timeframe. The script then uses this information to determine which months experienced
the greatest increase or decrease in profit change. The script then prints out a financial analysis descrbing the total months,
total net profit, average change in profit, and the months that experienced the greatest increase/decrease in profits and 
what those values were. It also writes the financial anlayis into a csv file and outputs it into the analysis folder.

### Resources
This folder contains the original csv file reference in our script.

### Analysis
This folder contains the outputted csv file created by the main script. The file contains in text the print statements
made in the main script: [Financial Analysis](https://github.com/EdGonz44/python-challenge/blob/main/PyBank/analysis/Analysis.csv)

## PyPoll
This folder contains the main script, a "Resources" folder, and an "Analysis" folder.

### Main Script
The script used to make the analysis of the election results. [Election Results Script](https://github.com/EdGonz44/python-challenge/blob/main/PyPoll/main.py)

The purpose of the main script in PyPoll was to determine the winner in an election based on voter count.
The script referenced a csv file containing the votes for each of the candidates in the race. 
The total number of ballots are counted, and the script isolates unique candidate names, and makes a list of them.
It then uses the list to determine how many votes each candidate received, and then the percentage they received from
the total number of votes. The script then uses this information to determine a winner, 
and then prints out the election results describing the above information. The script also writes a csv file that contains
the election results and outputs it into the analysis folder.

### Resources
This folder contains the original csv file reference in our script.

### Analysis
This folder contains the outputted csv file created by the main script. The fiel contains in text the print statements
made in the main script: [Election Results](https://github.com/EdGonz44/python-challenge/blob/main/PyPoll/analysis/Analysis.csv)

