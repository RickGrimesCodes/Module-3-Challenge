"Super duper data analytics machine calculator thingy python part 1"
import os
import csv

"here goes somthing... maybe"
PyBankCSV = os.path.join('Resources' , 'budget_data.csv')
with open(PyBankCSV, 'r') as PyBanks:
    csvreader = csv.reader(PyBanks)
    next(csvreader, None)
    column2List = [row[1] for row in csvreader ]
column2List = [int(num.strip("'")) for num in column2List]
rowCount = len(column2List)
ProfitTotal = sum(column2List)
ProfitMax = max(column2List)
ProfitMin = min(column2List)

changes = [column2List[i+1] - column2List[i] for i in range(len(column2List)-1)]
averageChange = sum(changes) / len(changes)
output =(
    f"\nFinacial Analysis \n"
    f"{'-'*25}"
    f"\nTotal Months: {rowCount}\n"
    f"Total: ${ProfitTotal}\n"
    f"Average Change: ${averageChange:,.2f}\n"
    f"Greatest Increase in Profits: ${ProfitMax}\n"
    f"Greatest Decrease in profits: ${ProfitMin}\n"
    )

print(output)
FileOutput = os.path.join('Analysis' , 'PyBankOutput.txt')
with open (FileOutput,'w') as file:
    file.write(output)
