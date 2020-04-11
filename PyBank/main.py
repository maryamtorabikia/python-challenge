import os
import csv

# Location of budget_data.csv:
budget_csv = os.path.join ('Resources','budget_data.csv')

# Reading the csv file:
with open (budget_csv,'r',newline='') as budget:
	budget_reader = csv.reader (budget,delimiter=',')
	header = next(budget_reader)


	total = 0
	total_amount = 0
	proff_loss_1=0
	changes_1=0
	increase=0
	decrease=0
	sum = 0
	changes_list = []
	
	for row in budget_reader:
		
	#Calculating the Total Months:
		total+= 1
		
	#Calculating the Total Amount of Profit/Losses:
		total_amount += int(row[1])
		
			
	#Calculating the Changes of Profit/Losses:
		changes = int(row[1])-int(proff_loss_1)

	#Calculating the Greatest Increase in Profits:	
		if (changes > increase):
			increase = changes
			date_increase=row[0]
			
	#Calculating the Greatest Decrease in Profits:		
		if (changes < decrease):
			decrease = changes
			date_decrease=row[0]
			
		proff_loss_1 = row[1]
		changes_1 = changes
		
	#Creating a list of all Profit/losses Changes:
		changes_list.append(changes)
	
	#Calculating the total of Changes:
		sum += changes
	
	# Calculating the Average of Changes in Proft/Losses over the entire period.
	average =(sum - (int(changes_list[0]))) / (int(len(changes_list))-1)
	
		
		
# Printing Financial Analysis:		
	print("Financial Analysis")	
	print("-------------------------------")
		
# Printing Total Months:
	print(f"Total Months: {total}")
	
# Printing Total amount of Profit/Losses:	
	print(f"Total: ${total_amount}")
	
# Printing the Average of Changes in Proft/Losses over the entire period:	
	print (f"Average Changes: ${round((average),2)}")
	
# Printing the Greatest Increase in Profits:	
	print (f"Greates Increase in Profits: {date_increase} (${increase})")

# Printing the Greatest Decrease in Losses:
	print (f"Greates Decrease in Losses: {date_decrease} (${decrease})")




	
# Location of Output file in txt format:
Pybank = os.path.join ('Budget_analyzes.txt')


# Writing the output file as Budget_analyzes.txt:
with open (Pybank,'w') as budget_analyzes:
	
# Inputing Financial Analysis:		
	budget_analyzes.write("Financial Analysis\n")	
	budget_analyzes.write("-------------------------------\n")
		
# Inputing Total Months:
	budget_analyzes.write(f"Total Months: {total}\n")
	
# Inputing Total amount of Profit/Losses:	
	budget_analyzes.write(f"Total: ${total_amount}\n")
	
# Inputing the Average of Changes in Proft/Losses over the entire period:	
	budget_analyzes.write(f"Average Changes: ${round((average),2)}\n")
	
# Inputing the Greatest Increase in Profits:	
	budget_analyzes.write(f"Greates Increase in Profits: {date_increase} (${increase})\n")

# Inputing the Greatest Decrease in Losses:
	budget_analyzes.write(f"Greates Decrease in Losses: {date_decrease} (${decrease})\n")
	
