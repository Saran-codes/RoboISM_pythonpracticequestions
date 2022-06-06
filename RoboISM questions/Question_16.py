#question_16
def isPrime(n):
    for i in range(2, int(n**(1/2))+1):
        if n%i == 0:
            return False
    return True


N = int(input("Enter no of primes(>0):"))
#as we already know 2 is a prime number
print(2,end=" ")
num=3
while N>1:
    if isPrime(num) == True:
        print(num,end=" ")
        N -= 1
    #we check for only odd numbers as even numbers cant be prime    
    num += 2   
        
