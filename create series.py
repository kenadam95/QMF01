import csv 

portfolio = []

with open('HOSE.csv') as csvfile:    
	csvReader = csv.reader(csvfile)    
	for row in csvReader:        
		portfolio.append(row[0])

portfolio[0]="AAA"        
print(portfolio)