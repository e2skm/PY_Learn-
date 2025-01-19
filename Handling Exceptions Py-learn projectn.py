# Handling Exceptions 101- PY-learn projectn
## Create variables to store values
age = 0
approvedMembers,  youngins = [], []
## Define a function to check whether age is over 17 or not
def is_approved_or_young(age):
    if age > 17:
      approvedMembers.append(age)
    else:
        youngins.append(age) 
    return approvedMembers, youngins 
## Create a loop to get member ages  
for x in range(8):
    while True: ### Infinite looping for invalid data
        try:
            print(f"Enter member {x + 1}'s age")
            age = int(input())
            approvedMembers, youngins = is_approved_or_young(age)
            break ### Terminate while loop in the case of valid data
        except ValueError:
            print('Invalid Input! enter a whole number for age')
## Display output 
print(f'{len(approvedMembers)} Members are approved to enter {approvedMembers}')
print(f'The following {len(youngins)} members should go home {youngins}')
    
            
            
    