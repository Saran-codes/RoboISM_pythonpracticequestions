#question_13
#***the following code can only find the first occurence of digit with odd count****
#***example input = 2 2 3 5 4 4*****
l = list(map(int,input("Enter your array :").split(' ')))

for i in l:
    if l.count(i)%2 != 0:
        print(i)
        break


