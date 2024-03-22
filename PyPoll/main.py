#text output
print("Election Results")
print("----------------------------")

#importing necessary packages 
import os
import csv

#opening the file 
budget_csv=os.path.join("Resources","election_data.csv")

#open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter =",")

    #skipping the first row
    csv_header= next(csv_file)

    votes = []
    for row in csv_file:
        #total votes
        votes.append(int(row[0]))
        total_votes = sum(votes)
        denom= len(votes)

print("----------------------------")

        #print statement
        #print("Total Votes:"str{tota_votes})
        CCD =[]
        DG =[]
        RRD = []
        
        if row[2]== "Charles Casper Stockham":
            CCD.append(row[0])
            num_ccd= sum(CCD)
            ccd_per = num_ccd/total_votes
            #print("Charles Casper Stockham:"str{ccd_per}"%","(" str{num_ccd})")")
        elif row[2]== "Diana DeGette":
            DG.append(row[0])
            num_DG = sum(DG)
            dg_per = num_DG/total_votes
        elif row[2]=="Raymon Anthony Doane":
            RRD.append(row[0])
            num_RRD = sum(RRD)
            RRD_per = num_RRD/total_votes
            winner = []
            winner.append(num_ccd,num_DG,num_RRD)
            max(winner)
            winner.index



