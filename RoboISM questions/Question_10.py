# question_10
num1 = int(input("Enter your first number:"))
num2 = int(input("Enter your second number:"))
print(num1, num2)
num1 ^= num2
num2 ^= num1
num1 ^= num2
print(num1, num2)
