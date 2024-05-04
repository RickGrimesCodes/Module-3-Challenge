# The other superduper data analytics python code thats going to give us the election results
import os
import csv
# turning column 3 into a list, excluding the first row
pyPollCSV = os.path.join('Resources', 'election_data.csv' )
with open(pyPollCSV, 'r') as PyPoll:
    csvreader = csv.reader(PyPoll)
    next(csvreader, None)
    column3List = [row[2] for row in csvreader ]

rowCount =(len(column3List))

votecount = {}
# making a dictionary to store the votes count with a for if loop, Dr. A loves dictionaries.
for items in column3List:
    if items in votecount:
        votecount[items] += 1
    else:
        votecount[items] = 1
votecount = votecount
winner = max(votecount, key=votecount.get)
# another for loop that creates a entry with politician, vote percentage, and votecount, and dumps it into a 'temporary' output string.
outputTemp = ""
for items, votecount in votecount.items():
    outputTemp += (f"{items}: {((votecount/ rowCount)*100):,.2f}% ({votecount})\n")
# final touches
output = ("Election Results \n\n"
f"{"-"*30}\n\n"
f"Total Votes: {rowCount}\n\n"
f"{"-"*30}\n\n"
f"{outputTemp}\n"
f"{"-"*30}"
f"\n\nDING DING DING DING!!! WINNER!!!: {winner}"
)
# create a file and print
FileOutput = os.path.join('Analysis' , 'PyPollOutput.txt')
with open (FileOutput,'w') as file:
    file.write(output)
print(output)