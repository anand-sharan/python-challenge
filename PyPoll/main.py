# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Get Current working directory of main.py file
cwd = os.getcwd()

# Set path for file

csvpath = os.path.join(cwd, "Resources", "election_data.csv")
csvpath = os.path.normcase(csvpath)
csvpath = os.path.normpath(csvpath)

election_output_file = os.path.join(cwd, "analysis","output.csv")
election_output_file = os.path.normcase(election_output_file)
election_output_file = os.path.normpath(election_output_file)

# Create dictionary and list variables to iterate through each row
total_votes_cast = 0
election_data = {}
candidates = []
unique_candidates = []
unique_candidate_vote_count = []
unique_candidate_percent_of_votes = []
winners = []

# Read the data file and print output
with open(csvpath,'r',encoding="utf-8") as election_csv_file:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(election_csv_file, delimiter=',')

    # Skip the header row first
    csv_header = next(csvreader)
    
    # Uncomment below line to print the stored csv_header
    print(f"CSV Header: {csv_header}")

# Load dictionary variable from the election_date.csv source file
# count total votes casted in the election
with open(csvpath,'r', newline="") as election_data_file:
    election_data = csv.DictReader(election_data_file)
    for row in election_data:
        candidates.append(row["Candidate"])
        total_votes_cast += 1

# Assign list of unique candidates
unique_candidates = list(set(candidates))

# Count each candidate's votes and percentage of votes
for i in unique_candidates:
    unique_candidate_vote_count.append(int(0))
    unique_candidate_percent_of_votes.append(float(0))    
    for j in candidates:
        if i == j:
            unique_candidate_vote_count[unique_candidates.index(i)] += 1
    if total_votes_cast > 0:
        unique_candidate_percent_of_votes[unique_candidates.index(i)] = 100*(unique_candidate_vote_count[unique_candidates.index(i)] / total_votes_cast)

# Find the maximum number of votes casted to a candidate
max_votes=max(unique_candidate_vote_count)

#Search for candidates who have maximum votes and append them into winners list
for k in range(len(unique_candidates)):
    if unique_candidate_vote_count[k]==max_votes:
        winners.append(unique_candidates[k])

# Assign Voting Results Column Headers into list variable
voting_results_col_header = ["  Election Results",
                             "  ----------------------------",
                             "  Total Votes:",
                             "  ----------------------------"
                            ]

# Assign Unique candidate names to Column Headers
for l in range(len(unique_candidates)):
    voting_results_col_header.append("  " + unique_candidates[l] + ":")

# Assign election's winner names to Column Headers
voting_results_col_header.append("  -------------------------")
voting_results_col_header.append("  Winner:")
voting_results_col_header.append("  -------------------------")

# Assign total votes cast results values into voting results list variable
voting_results_col_val = [   "",
                             "",
                             total_votes_cast,
                             ""
                         ]

# Assign voting results values into voting results list variable
for m in range(len(unique_candidates)):
    voting_results_col_val.append("%.3f%%" % (unique_candidate_percent_of_votes[m]) + " (" + str(unique_candidate_vote_count[m]) + ")")

voting_results_col_val.append("")

# Assign names into voting results list variable
winners_list = ""
for n in range(len(winners)):
    if winners_list:
        winners_list += ", " + winners[n]
    else:
        winners_list = winners[n]

# Assign winners into voting results list variable
voting_results_col_val.append(winners_list)

voting_results_col_val.append("")

# Zip all two lists together into tuples for writing to file
voting_results_file = list(zip(voting_results_col_header, voting_results_col_val))

# Writing to file
with open(election_output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # print out to file:
    for o, p in voting_results_file:
        print(o, p, end='\n', file=datafile)

# Zip all two lists together into tuples for writing to file
voting_results_ter = list(zip(voting_results_col_header, voting_results_col_val))

# print out to terminal:
for r, s in voting_results_ter:
    print(r, s, end='\n')
