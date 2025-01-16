a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

def gcd(a,b):
    if b > a:
        a,b=b,a
    return find_gcd(a,b)

def find_gcd(a,b):
    if a == 0 or b == 0:
        return a + b
    return find_gcd(b,a % b)

print(gcd(a,b))


