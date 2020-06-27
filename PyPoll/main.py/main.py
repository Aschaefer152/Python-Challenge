# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv


csvpath = os.path.join('Resources', 'election_data.csv')
# Method 2: Improved Reading using CSV module

#create lists
total_votes=0
candidate_list= []
vote_counts=[]

#open csv

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header
    line = next(csvreader,None)

    #go to each line
    for line in csvreader:

        #total # of votes
        total_votes= total_votes + 1

        #who they votes for
        candidate= line[2]

        # add to vote total
        if candidate in candidate_list:
            candidate_total=candidate_list.index(candidate)
            vote_counts[candidate_total] = vote_counts[candidate_total] +1
        #or create a new spot
        else:
            candidate_list.append(candidate)
            vote_counts.append(1)

    vote_percentage=[]
    max_votes = vote_counts[0]
    max_index=0
    #calculate the vote_percentage(percentage of votes) for each candidate
    for count in range(len(candidate_list)):
        vote_percentage = vote_counts[count]/total_votes * 100
        vote_percentage.append(vote_percentage)

        #find winner
        if vote_counts[count] > max_votes:
            max_votes = vote_counts[count]
            print(max_votes)
            max_index = count

    winner = candidate_list[max_index]

    #print election results
    print("Election Results")
    print("----------------------")
    print(f"Total Votes : {total_votes}")
    for count in range(len(candidate_list)):
        print(f"{candidate_list[count]}: {vote_percentage[count]}% ({vote_counts[count]})")
    print("----------------------")
    print(f"Winner: {winner}")
    print("----------------------")

