#question_15
#>>>space is also included 
#taking input of the string and converting it into a list
s = list(input("Enter your string:"))


count_alpha = 0
count_int = 0
count_char = 0
#iterating through each character and using if statements ,determining whether it is alphabet, interger or special character
for i in s:
    if i.isalpha() ==  True:
        count_alpha+=1
    elif i.isdigit() == True:
        count_int+=1
    else:
        count_char +=1
print("No of alphabet:",count_alpha)
print("No of integers:",count_int)
print("No of special characters:",count_char)  

#>>>space is also included as a special character
          