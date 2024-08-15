import csv


total_votes = 0
candidates = {}
winner = ""
winner_votes = 0


with open("election_data.csv") as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)  


    for row in csvreader:
        total_votes += 1
        
        candidate = row[2]
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1
    
    
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes})")
        
        if votes > winner_votes:
            winner = candidate
            winner_votes = votes


with open('election_results.txt', 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")

    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")
