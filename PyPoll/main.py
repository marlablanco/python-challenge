#import
import os
import csv

 #values and lists
total_votes=0
voter_id_list=[]
county_list=[]
candidate_list=[]
total_candidate_list=[]
previous_candidate=""

#open file and read
csvpath=os.path.join("Resources","election_data.csv")
with open(csvpath) as csvfile:

    #CSV reader specified delimiter and variable that holds contents
    csvreader=csv.reader(csvfile,delimiter=',')

    #skip header row
    csv_header=next(csvreader)
   
   #values
    stockham=0
    degette=0
    doane=0

    #headers
    ballot_id=csv_header.index("Ballot ID")
    county=csv_header.index("County")
    candidate_name=csv_header.index("Candidate")
   
    for row in csvreader:
        #total number of votes 
        total_votes=total_votes+1

        total_candidate_list.append(row[2])

        #candidates
        row_candidate=row[candidate_name]
        if row_candidate!=previous_candidate:
            candidate_list.append(row_candidate)
        previous_candidate=row_candidate

        if row[2]==candidate_list[0]:
            stockham=stockham+1
        elif row[2]==candidate_list[1]:
            degette=degette+1
        elif row[2]==candidate_list[2]:
            doane=doane+1
    

#candidate counts
stockham_count=total_candidate_list.count('stockham')
degette_count=total_candidate_list.count('degette')
doane_count=total_candidate_list.count('doane')

#percentages
stockham_percent=(stockham/total_votes)*100
degette_percent=(degette/total_votes)*100
doane_percent=(doane/total_votes)*100
percentage_list=[stockham_percent,degette_percent,doane_percent]

#percent formatting
stockham_percent_format=format(stockham_percent,'.3f')
degette_percent_format=format(degette_percent,'.3f')
doane_percent_format=format(doane_percent,'.3f')

#winner!
winner_percent=max(percentage_list)
winner_index=percentage_list.index(winner_percent)
winner=candidate_list[winner_index]


#print table headers
print("Election Results")
print("-------------------------")
print("Total Vote:"+str(total_votes))
print("-------------------------")
print("Charles Casper Stockham: "+str(stockham_percent_format)+"% ("+str(stockham)+")")
print("Diana DeGette: "+str(degette_percent_format)+"% ("+str(degette)+")")
print("Raymon Anthony Doane: "+str(doane_percent_format)+"% ("+str(doane)+")")
print("-------------------------")
print("Winner:"+str(winner))
print("-------------------------")

#write and export text file
poll_file=open("analysis/analysis.text","w")
poll_file.write("Election Results")
poll_file.write("-------------------------")
poll_file.write("Total Vote:"+str(total_votes))
poll_file.write("-------------------------")
poll_file.write("Charles Casper Stockham: "+str(stockham_percent_format)+"% ("+str(stockham)+")")
poll_file.write("Diana DeGette: "+str(degette_percent_format)+"% ("+str(degette)+")")
poll_file.write("Raymon Anthony Doane: "+str(doane_percent_format)+"% ("+str(doane)+")")
poll_file.write("-------------------------")
poll_file.write("Winner:"+str(winner))
poll_file.write("-------------------------")
poll_file.close()