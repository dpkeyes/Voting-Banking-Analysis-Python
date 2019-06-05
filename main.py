# Import modules
import csv

# Set up budget data csv to be more easily read, so I can search through it
with open('budget_data.csv', 'r', newline = '') as csvfile: # define the file and what constitutes a new line
    budget_data = csv.reader(csvfile, delimiter=',') # make the file a more readable object

    # Define variables and initial values
    numMonths = 0
    netProfitLoss = 0
    initialAmount = 0
    endAmount = 0
    changeProfitLossTracker = 0
    sumProfitLossList = 0
    averageProfitLossList = 0
    largestProfit = 0
    largestLoss = 0

    # Define list to keep track of data between adjacent months
    changeProfitLoss = []

    # Iterate through remaining rows to calculate variable values.
    rows = [row for row in budget_data] # Create list where each element is a row
    for i in range(1, len(rows)):

        # Define variable for the current row we're on
        row = rows[i]

        # Set numeric values as ints to simplify future calculations
        row[1] = int(row[1])

        # Count number of months and net profit/loss
        numMonths += 1
        netProfitLoss += row[1]

        # Create a list of change in profit/loss values between adjacent months to be used in calculations below
        if i < len(rows)-1:
            nextrow = rows[i+1] # Define variable for the next row
            initialAmount == row[1]
            endAmount == nextrow[1]
            changeProfitLossTracker = endAmount - initialAmount
            changeProfitLoss.append(changeProfitLossTracker) #################### This code is not functioning properly
    
    # Find the average of the change in profit/loss list values
    for i in range(len(changeProfitLoss)):
        sumProfitLossList += changeProfitLoss[i]
    averageProfitLossList == sumProfitLossList / len(changeProfitLoss)

    # Print values of variables
    print(numMonths)
    print(netProfitLoss)
    print(changeProfitLoss[5])