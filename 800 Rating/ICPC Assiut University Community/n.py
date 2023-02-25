# Follow me: www.facebook.com/codewithredoy
import math
# for _ in range(int(input())):
#     ...
# a, b = map(str, input().split())

x = ord(input())    #ascii code of x
if ord('a') <= x <= ord('z'):
    print(chr(x-32))
    
else:
    print(chr(x+32))

