def GCD(a,b):
    if a < b:
        a,b = b,a

    if a == 0 or b == 0:
        return a + b
    else:
        return GCD(b,a % b)

print(GCD(192,270))
