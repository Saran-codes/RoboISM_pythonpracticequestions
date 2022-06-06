#question_5
s = list(map(int,input("Enter your list:").split()))
#applying sort function so that same values come side by side in list
s.sort()
i=0
a=0
while i<len(s)-1:
    if s[i] == s[i+1]:
        a = s[i]
        break
    i=i+1
print("Repeated element:",a)




























