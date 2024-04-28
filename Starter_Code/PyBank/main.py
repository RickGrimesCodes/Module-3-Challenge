"Super duper data analytics machine calculator thingy python part 1"
import os
import csv

"here goes somthing maybe"
PyBankCSV = os.path.join('Resources' , 'budget_data.csv')
rowCount = 0
with open(PyBankCSV, 'r') as PyBanks:
    for line in PyBanks:
        rowCount += 1
rowCount -= 1
with open(PyBankCSV, 'r') as PyBanks:
    reader = csv.reader(PyBanks)
    next(reader, None)
    column2List = [row[1] for row in reader ]
column2List = [int(num.strip("'")) for num in column2List]
ProfitTotal = sum(column2List)
print(ProfitTotal)
print("Finacial Analysis")
print(rowCount)
print("-" * 25)

print("Total Months: ")
print("Total: ")
print("Average Change: ")
print("Greatest Increase in Profits: ")
print("Greatest Decrease in profits: ")