#import
import os
import csv

#for calculations between months
import numpy as np

changes=[]
month_count=0
max_change=0
max_month=""
min_change=0
min_month=""

#open file and read
with open("Resources/budget_data.csv") as csvfile:

    #CSV reader specified delimiter and variable that holds contents
    csvreader=csv.reader(csvfile,delimiter=',')

    #skip header row
    csv_header=next(csvreader)

   #empty lists
    total_months=[]
    total_profits=[]

#fill lists
    for row in csvreader:
        months=row[0]
        profits=int(row[1])
        total_months.append(months)
        month_count=month_count+1
        total_profits.append(profits)
        if month_count>1:
            change=profits-previous
            changes.append(change)
            if change>max_change:
                max_change=change
                max_month=months
            if change<min_change:
                min_change=change
                min_month=months
        previous=profits

#monthly changes

average=sum(changes)/len(changes)
average_change=format(average,'.2f')


#print table
print("Financial Analysis")
print("----------------------------")
print("Total Months:"+str(month_count))
print("Total: $"+str(sum(total_profits)))
print("Average Change: $"+str(average_change))
print("Greatest Increase in Profits:"+str(max_month)+"($"+str(max_change)+")")
print("Greatest Decrease in Profits:"+str(min_month)+"($"+str(min_change)+")")

#write and export text file
bank_file=open("analysis/analysis.text","w")
bank_file.write("Financial Analysis")
bank_file.write("----------------------------")
bank_file.write("Total Months:"+str(month_count))
bank_file.write("Total: $"+str(sum(total_profits)))
bank_file.write("Average Change: $"+str(average_change))
bank_file.write("Greatest Increase in Profits:"+str(max_month)+"($"+str(max_change)+")")
bank_file.write("Greatest Decrease in Profits:"+str(min_month)+"($"+str(min_change)+")")
bank_file.close()
