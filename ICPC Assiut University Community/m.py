# Follow me: www.facebook.com/codewithredoy
import math
# for _ in range(int(input())):
#     ...
# a, b = map(str, input().split())

x = ord(input())    #ascii code of x
if 48 <= x <= 57:
    print("IS DIGIT")
    
elif ord('a') <= x <= ord('z') or ord('A') <= x <= ord('Z'):
    if ord('a') <= x <= ord('z'):
        print("ALPHA")
        print("IS SMALL")
    else:
        print("ALPHA")
        print("IS CAPITAL")
