import os
import csv

#Declare file Location path.join
poll_data = os.path.join("resources","election_data.csv")

# Create empty list for rows
#def print_profit_losses(budget_data):
total_votes = 0
total_candidate = []
Candidate_votes= {}


#Open and Read csv 
with open(poll_data, 'r') as csv_file_1:

    # Store the contents of budget_data.csv
    csv_reader = csv.reader(csv_file_1,delimiter=",")

    #skip header labels 
    header = next (csv_reader)

    #Iterate through the rows stored in file
    for row in csv_reader:
        total_votes += 1
        current_candidate= row[2]
        if current_candidate not in total_candidate:
            total_candidate.append(current_candidate)
            Candidate_votes[current_candidate]=1
        else:
            Candidate_votes[current_candidate]+=1
print(total_candidate)
print(total_votes)
print(Candidate_votes)     
win_count=0
win_candidate=""
for row in total_candidate: 
    current_count=Candidate_votes[row]
    if current_count > win_count: 
        win_count= current_count
        win_candidate= row
print(win_candidate)               
print(win_count)