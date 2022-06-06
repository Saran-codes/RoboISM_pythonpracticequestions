#question_2
s = list((input("Enter Credit Card number: ")))
i = 0
while len(s)-i>4:
    #making all the elements except last four asterisk
    s[i] = "*"
    i = i+1
#joining the list back to form string
print("Hidden number:","".join(s))