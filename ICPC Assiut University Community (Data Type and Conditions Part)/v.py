# Follow me: www.facebook.com/codewithredoy

import math
# for _ in range(int(input())):
#     ...
# a, b, c = map(int, input().split())
s = input()
# num = float(input())

r = "Right"
w = "Wrong"
main = s.split(" ")

sign = main[1]
a = int(main[0])
b = int(main[2])

if sign == "<":
    if a < b:
        print(r)
    else:
        print(w)
elif sign == ">":
    if a > b:
        print(r)
    else:
        print(w)
else:
    if a == b:
        print(r)
    else:
        print(w)
