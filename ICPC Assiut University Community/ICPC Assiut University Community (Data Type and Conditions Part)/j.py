# Follow me: www.facebook.com/codewithredoy
import math
# for _ in range(int(input())):
#     ...

a, b = map(int, input().split())
if (a % b  == 0) or (b % a == 0):
    print("Multiples")
else:
    print("No Multiples")