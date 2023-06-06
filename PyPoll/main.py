#import
import os
import csv
import numpy as np
#open file and read
with open("Resources/election_data.csv") as csvfile:

    #CSV reader specified delimiter and variable that holds contents
    csvreader=csv.reader(csvfile,delimiter=',')

    #skip header row
    csv_header=next(csvreader)

    #make lists
    voter_id_list=[]
    county_list=[]
    candidate_list=[]

    #fill lists
    for row in csvreader:
        id=row[0]
        county=row[1]
        candidate=row[2]
        voter_id_list.append(id)
        county_list.append(county)
        candidate_list.append(candidate)

#candidate counts
stockham=candidate_list.count('stockham')
degette=candidate_list.count('degette')
doane=candidate_list.count('doane')

#percentages
stockham_percent=(stockham/len(voter_id_list))*100
degette_percent=(degette/len(voter_id_list))*100
doane_percent=(doane/len(voter_id_list))*100

#percent formatting
stockham_percent_format=format(stockham_percent,'.3f')
degette_percent_format=format(degette_percent,'.3f')
doane_percent_format=format(doane_percent,'.3f')

#winner!
winner=mode(candidate_list)

#print table headers
print("Election Results")
print("-------------------------")
print("Total Vote:"+str(len(voter_id_list)))
print("-------------------------")
print("Charles Casper Stockham: "+str(stockham_percent_format)+"% ("+str(stockham)+")")
print("Diana DeGette: "+str(degette_percent_format)+"% ("+str(degette)+")")
print("Raymon Anthony Doane: "+str(doane_percent_format)+"% ("+str(doane)+")")
print("-------------------------")
print("Winner: Diana DeGette")
print("-------------------------")
