# Follow me: www.facebook.com/codewithredoy
import math
# for _ in range(int(input())):
#     ...
# a, b = map(str, input().split())
x = input()

if "+" in x:
    res = x.split("+")
    print(int(res[0])+int(res[1]))
elif "-" in x:
    res = x.split("-")
    print(int(res[0]) - int(res[1]))
elif "*" in x:
    res = x.split("*")
    print(int(res[0]) * int(res[1]))
else:
    res = x.split("/")
    print(int(res[0]) // int(res[1]))
    

