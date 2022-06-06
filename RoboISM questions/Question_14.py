#quesion_14
def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

a, b = map(int,input("Enter both numbers: ").split(" "))

print("GCD of the numbers is", gcd(a,b))
