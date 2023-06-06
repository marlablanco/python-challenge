#import
import os
import csv

#for calculations between months
import numpy as np

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
        total_profits.append(profits)
   
#define functions to be used
def max(array,n):
    max=array[0]

    for i in range(1,n):
        if array[i]>max:
            max=array[i]
    return max

def min(array,n):
    min=array[0]

    for i in range(1,n):
        if array[i]<min:
            min=array[i]
    return min


#calculate profit and loss
n=len(total_profits)
largest_profit=max(total_profits,n)
largest_loss=min(total_profits,n)

if row[1]==str(largest_profit):
   profit_month=row[0]
if row[1]==str(largest_loss):
    loss_month=row[0]


#monthly changes
monthly_changes=np.diff(total_profits)

average=sum(monthly_changes)/len(monthly_changes)
average_change=format(average,'.2f')

m=len(monthly_changes)
greatest_increase=max(monthly_changes,m)
greatest_loss=min(monthly_changes,m)

#print table
print("Financial Analysis")
print("----------------------------")
print("Total Months:"+str(len(total_months)))
print("Total: $"+str(sum(total_profits)))
print("Average Change: $"+str(average_change))
print("Greatest Increase in Profits:"+str(profit_month)+"($"+str(greatest_increase)+")")
print("Greatest Decrease in Profits:"+str(loss_month)+"($"+str(greatest_loss)+")")
