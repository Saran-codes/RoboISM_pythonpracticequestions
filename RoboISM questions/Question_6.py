#question_6
#taking input of lower and upper ranges
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for num in range(lower,upper+1):
    for i in range(2,num):
        if num%i == 0:
            break
    else:
        #printing primes
        print(num)


