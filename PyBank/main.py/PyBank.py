import csv
with open ("budget_data.csv") as csvfile:
    csvreader = csv.reader(csvfile)
    print(csvreader)
    csv_header = next(csvreader)
    total_months = 0
    net_total = 0
    changes = []
    greatest_increase = -9999.9
    greatest_increase_month= ""
    greatest_decrease = 9999999999.99
    greatest_decrease_month = ""

    #greatest_decrease = 
    # = total_months + 1
    #print(total_months)
    #Jan-10,1088983
    #Feb-10,-354534
    # -354534- 1088983= -1355589
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        #print(row)
        total_months = total_months + 1
        net_total += int(row[1])
        if total_months > 1:
            change = int(row[1]) - previous_row_value
            changes.append(change) 
            if greatest_increase<change
            :
                greatest_increase=change
                greatest_increase_month = str(row[0])
            if greatest_decrease>change:
                greatest_decrease=change
                greatest_decrease_month = str(row[0])
        previous_row_value = int(row[1])
    
    print(" List changes :", changes)
    average_change = sum(changes) / len(changes)
    print(total_months)
    print(net_total)
    print(average_change)
    print(greatest_increase)
    print(greatest_increase_month)
    print(greatest_decrease)
    print(greatest_decrease_month)
# Define the output values
output_values = {
    "Total Months": total_months,
    "Total": f"${net_total}",
    "Average Change": f"${average_change:.2f}",
    "Greatest Increase in Profits": f"{greatest_increase_month} (${greatest_increase})",
    "Greatest Decrease in Profits": f"{greatest_decrease_month} (${greatest_decrease})"
}

# Open a new text file in write mode
with open("output_file.txt", "w") as file:
    # Write the formatted output to the file
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    for key, value in output_values.items():
        file.write(f"{key}: {value}\n")
