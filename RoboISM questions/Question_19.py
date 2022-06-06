#importing random module
import random
#generating a random number and converting it into a string , then taking it in form of list
code = list(str(random.randint(0000,9999)))
#as the above function can also generate values like 1, 20, 132; to convert them into four digit strings we add zeroes before them
#the following code does it:
if len(code) == 3:
    code.insert(0,'0')
    print(code)
if len(code) == 2:
    code.insert(0,'0')    
    code.insert(1,'0')
if len(code) == 1:
    code.insert(0,'0')    
    code.insert(1,'0') 
    code.insert(2,'0')   
  
#maximum number of tries    
trys = 10

for i in range(0,trys):
    count = 0
    #taking input of guess from user
    guess = list(input("Enter your guess:"))
    
    #finding if any characters in guess match with that of code
    for l in guess:
        if code.count(l) >0:
            count +=1
    #as the code may have all same digits, we may get wrong result, so we decrese count by 1 in that case
    if code[0] == code[1] and code[1] == code[2] and code[2] == code[3]:
        count = count-1  
    #as the guess may have all same digit, we may get wrong result, so we decrease count by 1 in that case       
    if guess[0] == guess[1] and guess[1] == guess[2] and guess[2] == guess[3]:
        count = count-1         
    #if code exactly same as guess for loop breaks and game ends
    if guess == code:
        print("R")  
        break
    #if guess has all same characters that of code but with different arrangements, prints "Y"
    elif count == 4:
        print("Y")
    #none of the above case:    
    else:
        print("B")        

    