import math

def good(a):
    gcd = a[0]
    for i in range(1, len(a)):
        gcd = math.gcd(gcd, a[i])
    return gcd <= len(a)

def is_beautiful(a):
    if not good(a):
        return False
    for i in range(2, len(a)+1):
        prefix = a[:i]
        gcd = prefix[0]
        for j in range(1, len(prefix)):
            gcd = math.gcd(gcd, prefix[j])
        if gcd > len(prefix):
            return False
    return True

def betf(a):
    freq = {}
    for x in a:
        freq[x] = freq.get(x, 0) + 1
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] != a[j]:
                a[i], a[j] = a[j], a[i]
                if is_beautiful(a):
                    return True
                a[i], a[j] = a[j], a[i]
    return False

for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()][:n]
    
    res = betf(a)
    
    if res:
        print("YES")
    else:
        print("NO")