#!/usr/bin/env python
# coding: utf-8

# In[112]:


import csv
import os

file_to_load = os.path.join(".", "Resources", "election_data.csv")
file_to_output = os.path.join(".", "election_analysis.txt")

total_votes = 0

candidate_list = []
candidate_votes = {}
winning_candidate = " "
winning_count = 0



with open(file_to_load) as election_data:
    
    csvreader = csv.reader(election_data, delimiter=',')
    csv_header = next(csvreader)

    
    first_row = next(csvreader)

    total_votes = total_votes + 1
    
    for row in csvreader:
        
        #Calculate Total Votes
        total_votes = total_votes + 1


        #Candidates who received votes
        candidate_name = row[2]

        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)

            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

print(candidate_votes)


        
        

        
with open(file_to_output, "w") as txt_file:

    election_results = (
        f"Election Results\n"
        f"-----------------\n"
        f"Total Votes: {total_votes}\n"
        f"-----------------\n"
)

    print(election_results)
    txt_file.write(election_results)

    for candidate in candidate_votes:
        
        votes = candidate_votes[candidate]
        vote_percentage = float(votes)/float(total_votes) * 100

        if(votes> winning_count):
            winning_count = votes
            winning_candidate = candidate

        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        
        
        print(voter_output)

        txt_file.write(voter_output)

    winning_candidate_summary = (
        f"-----------------\n"
        f"Winning: {winning_candidate}\n"
        f"-----------------\n"
)
    txt_file.write(winning_candidate_summary)


# In[ ]:





# In[ ]:




