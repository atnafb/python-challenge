import os 
import csv

# Define the file paths for the CSV file and the output file
file_path = os.path.join("Resources", "election_data.csv")
analysis_file = os.path.join('analysis', 'analysis_file.txt')

# Declaring variables
total_votes = 0  # initializing the total vote counter to 0 
candidates = []  # List to store candidate names 
candidatesVotes = {}  # Dictionary to store the votes each candidate receives
winning_candidate = "" # Variable to stor the name of the winning candidate 
max_votes = 0  # Variable to track the maximum votes

# Read the CSV file
with open(file_path) as election_data: # Open the csv file 
    reader = csv.DictReader(election_data)  # Interpret the file as a CSV

    for row in reader:  # Loop through each row in the CSV
        total_votes += 1  # sum total number of votes

        candidate_name = row["Candidate"]  # Get the candidate name from the "Candidate" column 

        # If candidate is new, add to list and initialize thier vote count 
        if candidate_name not in candidates:
            candidates.append(candidate_name) # add candidate to the list 
            candidatesVotes[candidate_name] = 1 # Start vote count 
        else:
            candidatesVotes[candidate_name] += 1 # if candidate arleady in the list, increment thier vote count 

# Format output for each candidate
candidate_results = "" # String to accumulate formatted resualts for each candidate 
for candidate, vote_count in candidatesVotes.items():
    # Calculate the percentage of votes each candidate received
    percentage = (vote_count / total_votes) * 100 # Caluculate the vote perecnetage for each candidate 
    candidate_results += f"{candidate}: {percentage:.3f}% ({vote_count})\n" # format and append candidate's result 
    
    # Determine the winning candidate
    if vote_count > max_votes: # If the candidate's vote count is the highest 
        max_votes = vote_count # update the max_vote with this candidate's count 
        winning_candidate = candidate # Set this candidate as the winning candidate 

# Prepare the final output
output = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
    f"{candidate_results}" #iclude all formated candidate result 
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"-------------------------\n"
)
print(output)

# Write output to file
with open(analysis_file, "w") as textFile:
    textFile.write(output) # write the output string to the analysis file
