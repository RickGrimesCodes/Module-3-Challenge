"The other superduper data analytics python code thats going to give us the election results"
import os
import csv
"turning column 3 into a list, excluding the first row"
pyPollCSV = os.path.join('Resources', 'election_data.csv' )
with open(pyPollCSV, 'r') as PyPoll:
    csvreader = csv.reader(PyPoll)
    next(csvreader, None)
    column3List = [row[2] for row in csvreader ]
"making a dictionary to store the votes count with a for if loop"
rowCount =(len(column3List))
votecount = {}

for items in column3List:
    if items in votecount:
        votecount[items] += 1
    else:
        votecount[items] = 1
outputTemp = ""
for items, votecount in votecount.items():
    outputTemp += (f"{items}: {(votecount/ rowCount)*100}% ({votecount})\n")
print(outputTemp)