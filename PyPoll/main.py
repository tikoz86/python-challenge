import os
import csv

csvpath = os.path.join("..", "PyPoll", 'election_data.csv')
with open(csvpath, 'r', newline = '', encoding = 'utf-8') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter= ",")
    total_votes = 0
    Khan = 0
    Correy = 0
    Li = 0
    OTooley = 0
    
    with open(csvpath, 'r', newline = '') as csvfile:
        csvreader=csv.reader(csvfile, delimiter = ",")
       
        header = next(csvreader)
    
        for i in csvreader:
            
            total_votes +=1
            
            if i[2] == "Khan":
                Khan +=1
            elif i[2] == "Correy":
                Correy +=1
            elif i[2] == "Li":
                Li +=1
            elif i[2] == "O'Tooley":
                OTooley +=1
                
        Khan_percentage = (Khan / total_votes * 100)
        Correy_percentage = (Correy / total_votes * 100)
        Li_percentage = (Li / total_votes * 100)
        OTooley_percentage = (OTooley / total_votes * 100)
        
        candidates = ["Khan", "Correy", "Li", "OTooley"]
        votes = [Khan, Correy, Li, OTooley]
        dictionary = dict(zip(candidates, votes))
        winner = max(dictionary, key = dictionary.get)
        
                

print("Election Results")
print("______________________")
print(f"Total Votes: {total_votes}")
print("______________________")
print(f"Khan: {Khan_percentage: .3f}% ({Khan})")
print(f"Correy: {Correy_percentage: .3f}% ({Correy})")
print(f"Li: {Li_percentage: .3f}% ({Li})")
print(f"O'Tooley: {OTooley_percentage: .3f}% ({OTooley})")
print("______________________")
print(f"Winner: {winner}")
print("______________________")

txtpath = os.path.join("..", "PyPoll", 'Results.txt')
with open(txtpath, 'w') as txtfile:
    print("Election Results", file=txtfile)
    print("______________________", file=txtfile)
    print(f"Total Votes: {total_votes}", file=txtfile)
    print("______________________", file=txtfile)
    print(f"Khan: {Khan_percentage: .3f}% ({Khan})", file=txtfile)
    print(f"Correy: {Correy_percentage: .3f}% ({Correy})", file=txtfile)
    print(f"Li: {Li_percentage: .3f}% ({Li})", file=txtfile)
    print(f"O'Tooley: {OTooley_percentage: .3f}% ({OTooley})", file=txtfile)
    print("______________________", file=txtfile)
    print(f"Winner: {winner}", file=txtfile)
    print("______________________", file=txtfile)
    