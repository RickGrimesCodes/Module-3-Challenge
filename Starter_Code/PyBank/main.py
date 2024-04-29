"Super duper data analytics machine calculator thingy python part 1"
import os
import csv

"here goes somthing maybe"
PyBankCSV = os.path.join('Resources' , 'budget_data.csv')
with open(PyBankCSV, 'r') as PyBanks:
    csvreader2 = csv.reader(PyBanks)
    next(csvreader2, None)
    column2List = [row[1] for row in csvreader2 ]
column2List = [int(num.strip("'")) for num in column2List]
rowCount = len(column2List)
ProfitTotal = sum(column2List)
ProfitMax = max(column2List)
ProfitMin = min(column2List)

changes = [column2List[i+1] - column2List[i] for i in range(len(column2List)-1)]
averageChange = sum(changes) / len(changes)
output = ()
        f"\n Finacial Analysis \n"
        f" - {* 25}\n"
        f"\nTotal Months: {rowCount}"
        f"\nTotal: ${ProfitTotal}"
        f"\nAverage Change: ${averageChange}.2f""
        f"\nGreatest Increase in Profits: ${ProfitMax}"
        f"\nGreatest Decrease in profits: ${ProfitMin}")
