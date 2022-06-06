#question_7
l = list(map(int,input("Enter your list:").split()))
#defining a dictionary in which elements of list will be items and frequencies of elements will be values
s = {}

for n in l:
    if n in s:
        s[n] +=1
    else:
        s[n] = 1
max_freq = max(s.values())
answer = [i for i,f in s.items() if f == max_freq]
for a in answer:
    print(a,end =" ")          