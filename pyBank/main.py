import os  # Importing the os module to use its functions
import csv # Importing the csv file 

# Define the file paths for csv file and the output file 
file_path = os.path.join("Resources", "budget_data.csv")
analysis_file = os.path.join("analysis", "analysis_file.txt")

# Initialize variables
num_months = 0  # Counter for the total number of months
total_profit_loss = 0  # Accumulator for total profit or loss
current_value = None  # Holds the current month's profit/loss value (start as None)
monthly_profits_list = []  # List to store monthly profit/loss changes

# Variables to track greatest increase and decrease
greatest_increase = {"date": "", "amount": 0}
greatest_decrease = {"date": "", "amount": 0}

# Read the CSV
with open(file_path, mode="r") as budget_data:  # The file is open as read mode
    reader = csv.DictReader(budget_data)  # Interpret the file as a CSV

    for row in reader:  # Loop through each row in the CSV
        num_months += 1  # Increment month counter
        total_profit_loss += int(row["Profit/Losses"])  # Accumulate the profit/loss 

        # Calculate the monthly change, if possible
        if current_value is not None:
            monthly_change = int(row["Profit/Losses"]) - current_value  # Calculate the change
            monthly_profits_list.append(monthly_change)  # Append the change to the list

            # Update greatest increase
            if monthly_change > greatest_increase["amount"]:
                greatest_increase["amount"] = monthly_change # update the ammount of the greatest increase 
                greatest_increase["date"] = row["Date"] # update the date of the greatest increase 

            # Update greatest decrease
            if monthly_change < greatest_decrease["amount"]:
                greatest_decrease["amount"] = monthly_change #update the amount of the greatest decrease 
                greatest_decrease["date"] = row["Date"] #update the date of greatest decrease 
        
        # Update current_value for the next iteration
        current_value = int(row["Profit/Losses"])

# Calculate average change
if len(monthly_profits_list) > 0: # check if the list of monthly profits has any entries 
    average_change = sum(monthly_profits_list) / len(monthly_profits_list) # calculate the average change 
else:
    average_change = 0 # if no change esist, set averge change to 0

# Format output
output = (
    f"\nFinancial Analysis \n"
    f"---------------------- \n"
    f"\nTotal Months = {num_months}\n" 
    f"\nTotal = ${total_profit_loss}\n"
    f"\nAverage Change = ${average_change:.2f}\n"
    f"\nGreatest Increase in Profits = {greatest_increase['date']} (${greatest_increase['amount']})\n"
    f"\nGreatest Decrease in Profits = {greatest_decrease['date']} (${greatest_decrease['amount']})\n"
)

print(output) # print the formatted output to the terminal 

# Write output to file
with open(analysis_file, "w") as textFile:
    textFile.write(output) # write the output string to the analysis file 
