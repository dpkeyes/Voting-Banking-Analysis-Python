# Import modules
import csv

# Set up election data csv to be more easily read, so I can search through it
with open('election_data.csv', 'r', newline = '') as csvfile: # define the file and what constitutes a new line
    election_data = csv.reader(csvfile, delimiter=',') # make the file a more readable object

    # Define variables and initial values
    numVotes = 0 # total number of votes in election
    winner = str # winning candidate

    # Define lists to keep track of certain
    candidate = [] # list of candidates that received at least one vote
    candidateVotes = [] # list of votes per candidate in candidate[] list
    candidatePercentage = [] # list of percentages of votes for each candidate in candidate[] list

    # Iterate through rows to calculate variable values.
    rows = [row for row in election_data] # create list where each element is a row
    for i in range(1, len(rows)): # start at row 1 instead of row 0 because row 0 is the header

        # Define variable for the current row we're on
        row = rows[i]

        # Check if candidate is new. If new, append lists of tracking data. If not new, update counters.
        if row[2] not in candidate:
            candidate.append(row[2]) # adds the new candidate to our candidate list
            candidateVotes.append(int(1)) # adds a new element of 1 for 'first vote' to candidateVotes list
        
        else: 
            for j in range(len(candidate)):
                if row[2] == candidate[j]:
                    candidateVotes[j] += 1

        # Count number of votes
        numVotes += 1
    
    # Calculate percentage votes for each candidate
    for i in range(len(candidateVotes)):
        candidatePercentage.append(round(float((candidateVotes[i]/numVotes)*100),3))
    
    # Output the winner of the election
    for i in range(len(candidatePercentage)):
        if candidatePercentage[i] >= candidatePercentage[0]:
            winner = candidate[i]

# Print the length of the candidate list so I can set up my print functions appropriately below. Then commented it out beause I don't want to show the list explicitly.
# print(len(candidate))

# Print election results to terminal
print("Election results")
print("------------------------")
print("Total Votes: " + str(numVotes))
print("------------------------")
print(str(candidate[0]) + ": " + str(candidatePercentage[0]) + "% (" + str(candidateVotes[0]) + ")")
print(str(candidate[1]) + ": " + str(candidatePercentage[1]) + "% (" + str(candidateVotes[1]) + ")")
print(str(candidate[2]) + ": " + str(candidatePercentage[2]) + "% (" + str(candidateVotes[2]) + ")")
print(str(candidate[3]) + ": " + str(candidatePercentage[3]) + "% (" + str(candidateVotes[3]) + ")")
print("------------------------")
print("Winner: " + str(winner))
print("------------------------")

# Open .txt file
f = open("election_results.txt","w+")

# Print election results to .txt file
print("Election results", file = f)
print("------------------------", file = f)
print("Total Votes: " + str(numVotes), file = f)
print("------------------------", file = f)
print(str(candidate[0]) + ": " + str(candidatePercentage[0]) + "% (" + str(candidateVotes[0]) + ")", file = f)
print(str(candidate[1]) + ": " + str(candidatePercentage[1]) + "% (" + str(candidateVotes[1]) + ")", file = f)
print(str(candidate[2]) + ": " + str(candidatePercentage[2]) + "% (" + str(candidateVotes[2]) + ")", file = f)
print(str(candidate[3]) + ": " + str(candidatePercentage[3]) + "% (" + str(candidateVotes[3]) + ")", file = f)
print("------------------------", file = f)
print("Winner: " + str(winner), file = f)
print("------------------------", file = f)
