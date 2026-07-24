
print("\nWelcome to Smart Voting & Student Management System\n")
#step-3:Voting data input
votes=[]
total_voters=int(input("enter the no of voters: "))

for i in range(total_voters):
    print(f"{i+1} no voter's candidate information:  ")
    candidate_name= input("enter the name of candidate: ")
    votes.append(candidate_name)
print("\nall captured votes:",votes)

#step-4: Frequency counter using Dictionary

vote_counts={
    
}
for j in range(len(votes)):
    candidate=votes[j]
    if candidate in vote_counts.keys(): 
        vote_counts[candidate]+=1
    else:
        vote_counts[candidate]=1
print("\nvote count dictionary:", vote_counts)

#step-5 & 6: Display vote results and Winner Detection 
max_votes=0
winner=""

print("\n--- Display Vote Results ---")
for candidate, vote_received in vote_counts.items():
    print(f"{candidate}:{vote_received}") 
    
    if vote_received > max_votes:
        max_votes = vote_received
        winner = candidate

print(f"The winner is : {winner}")

#step-7: Searching Features

print("\n--- Search Candidate Data ---")
search_name = input("Enter candidate name to search their data: ")
candidate_list = list(vote_counts.keys()) 

found = False 
for k in range(len(candidate_list)):
    if candidate_list[k] == search_name:
        found = True
        break 
if found:
    print(f"Candidate '{search_name}' found! Total votes: {vote_counts[search_name]}")
else:
    print(f"Sorry, no data found for candidate '{search_name}'.")
