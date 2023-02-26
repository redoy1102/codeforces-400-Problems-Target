# Follow me: www.facebook.com/codewithredoy
import math
# for _ in range(int(input())):
#     ...
# a, b = map(str, input().split())
# s = input()

num = float(input())
i = "Interval"
oi = "Out of Intervals"

if 0.0 <= num <= 25.0:
    print(i, "[0,25]")
elif 25.0 < num <= 50.0:
    print(i, "(25,50]")
elif 50.0 < num <= 75.0:
    print(i, "(50,75]")
elif 75.0 < num <= 100.0:
    print(i, "(75,100]")
else:
    print(oi)
