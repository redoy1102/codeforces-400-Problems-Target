# Follow me: www.facebook.com/codewithredoy

import math
# for _ in range(int(input())):
#     ...
# a, b, c = map(int, input().split())
s = input()
# num = float(input())

y = "Yes"
main = s.split(" ")

sign = main[1]
a = int(main[0])
b = int(main[2])
res = int(main[4])

if sign == "+":
    if a + b == res:
        print(y)
    else:
        print(a+b)
elif sign == "-":
    if a - b == res:
        print(y)
    else:
        print(a-b)
else:
    if a * b == res:
        print(y)
    else:
        print(a*b)
