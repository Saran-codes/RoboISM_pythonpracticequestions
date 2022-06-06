# question_11
# taking input of pallindrome in form of list
s = list(input("Enter your Pallindrome:"))
# making copy of the above list
a = s.copy()
# reversing the copy list
a.reverse()
# comparing both list to find out whether given string is pallindrome
if a == s:
    print("It is a Pallindrome")
else:
    print("It is not a Pallindrome")
