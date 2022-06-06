#question_1
#taking input of the list
n = list(map(int,input("Enter Your List:").split()))
#taking input of second parameter
y = input("Enter Your second parameter(asc, desc, none): ")

if  y == "asc":
    #sorting in ascending order
    n.sort()
    print(n)
elif y == "desc":
    #sorting in descending order
    n.sort(reverse=True)
    print(n)
elif y == "none":
    print(n)
else :
    print("Second parameter not recognized , try again")


