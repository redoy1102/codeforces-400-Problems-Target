def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

res = gcd(48, 36)
print(res)