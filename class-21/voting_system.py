candidates=[]
voters=[]
num_of_candidates=int(input("Enter the number of candidates: "))
num_of_voters=int(input("Enter the number of voters: "))

for i in range(num_of_candidates):
    print(f"enter the candidate no {i+1}  info:  ")
    candidate_name=input("Name: ")
    candidate_age=input("age: ")
    candidate_income=input(" Yearly income: ")
    candidate={
        "id":i+1,
        "name":candidate_name,
        "age":candidate_age,
        "yearly_income":candidate_income,
        "total_vote":0
    }
    candidates.append(candidate)
    
for i in range(num_of_voters):
    print(f"enter the voter no {i+1} info:  ")
    voter_name=str(input("Name: "))
    voter_age=int(input("age: "))
    gender=str(input("gender: "))
    
    voter={
        "id":i+1,
        "name":voter_name,
        "age":voter_age,
        "gender":gender,
        "has_casted":False
    }
    voters.append(voter)
    
for i in range(num_of_voters):
    candidate_id=int(input(f"enter the candidate id for voter no {i+1}: "))
    for j in range(num_of_candidates):
        if candidates[j]["id"]==candidate_id:
            candidates[j]["total_vote"]+=1
    voters[i]["has_casted"]=True
for i in range(num_of_candidates):
    print(candidates[i])