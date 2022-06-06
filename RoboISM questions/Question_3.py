#question_3
#taking input of first number
n1 = int(input("Enter first parameter: "))
#taking input of operation
op = input("Enter second parameter(+,-,*,/):")
#taking input of second number
n2 = int(input("Enter third parameter: "))
if op == "+":
    print(n1+n2)
elif op == "-":
    print(n1-n2)
elif op == "*":
    print(n1*n2)
elif op == "/":
    print(n1/n2)
else:
    print("2nd parameter not recognised")