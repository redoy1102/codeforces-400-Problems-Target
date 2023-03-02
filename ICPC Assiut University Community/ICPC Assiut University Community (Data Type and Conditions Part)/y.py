# Follow me: www.facebook.com/codewithredoy

import math
# for _ in range(int(input())):
#     ...
a, b, c, d = map(int, input().split())
# s = input()
# num = int(input())

mul = str(a*b*c*d)
rev = mul[::-1]
print(rev[1]+rev[0])

