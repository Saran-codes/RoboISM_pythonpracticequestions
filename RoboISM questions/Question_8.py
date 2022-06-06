# question_8
# taking input of string as a list
n = list(input("Enter your string:"))

# removing spaces from the list
p = n.count(" ")
for i in range(0, p):
    n.remove(" ")

# sorting the list so numbers come before other characters
n.sort()

# finding the index position where integers end in sorted list
a = 0
for i in range(0, len(n)-1):
    if n[i].isdigit() == False:
        a = i-1
        break

# finding sum of all the INTEGERS
s = 0
for i in range(0, a+1):
    s = s+int(n[i])
print(s)
