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
    largestProfitMonthTracker = 0
    largestLoss = 0
    largestLossMonthTracker = 0

    # Define list to keep track of data between adjacent months
    changeProfitLoss = []

    # Iterate through remaining rows to calculate variable values.
    rows = [row for row in budget_data] # Create list where each element is a row
    for i in range(1, len(rows)): # Start at row 1 instead of row 0 because row 0 is the header

        # Define variable for the current row we're on
        row = rows[i]

        # Set numeric string value as ints to simplify future calculations
        row[1] = int(row[1])

        # Count number of months and net profit/loss
        numMonths += 1
        netProfitLoss += row[1]

        # Create a list of change in profit/loss values between adjacent months to be used in calculations below
        if i < len(rows)-1:
            nextrow = rows[i+1] # Define variable for the next row
            nextrow[1] = int(nextrow[1]) # Set numeric string values as ints to simplify calculation below
            initialAmount = row[1]
            endAmount = nextrow[1]
            changeProfitLossTracker = endAmount - initialAmount
            changeProfitLoss.append(changeProfitLossTracker) 
    
    # Find the average of the change in profit/loss list values.
    for i in range(len(changeProfitLoss)):
        sumProfitLossList += changeProfitLoss[i]
        averageProfitLossList = round(sumProfitLossList / len(changeProfitLoss), 2)

        # Iteratively store the largest profit
        if largestProfit <= changeProfitLoss[i]:
            largestProfit = changeProfitLoss[i]
            largestProfitMonthTracker = i+1
        
        # Iteratively store the largest loss
        if largestLoss >= changeProfitLoss[i]:
            largestLoss = changeProfitLoss[i]
            largestLossMonthTracker = i+1
    
    # Find the largest profit month and largest loss month
    largestProfitMonth = rows[largestProfitMonthTracker + 1][0]
    largestLossMonth = rows[largestLossMonthTracker + 1][0]

# Print financial analysis metrics to terminal
print("Financial Analysis")
print("------------------------")
print("Total Months: " + str(numMonths))
print("Total: $" + str(netProfitLoss))
print("Average Change: $" + str(averageProfitLossList))
print("Greatest Increase in Profits: " + str(largestProfitMonth) + " ($" + str(largestProfit) + ")")
print("Greatest Decrease in Profits: " + str(largestLossMonth) + " ($" + str(largestLoss) + ")")

# Open .txt file
f = open("financial_analysis.txt","w+")

# Print financial analysis metrics to .txt file
print("Financial Analysis", file = f)
print("------------------------", file = f)
print("Total Months: " + str(numMonths), file = f)
print("Total: $" + str(netProfitLoss), file = f)
print("Average Change: $" + str(averageProfitLossList), file = f)
print("Greatest Increase in Profits: " + str(largestProfitMonth) + " ($" + str(largestProfit) + ")", file = f)
print("Greatest Decrease in Profits: " + str(largestLossMonth) + " ($" + str(largestLoss) + ")", file = f)