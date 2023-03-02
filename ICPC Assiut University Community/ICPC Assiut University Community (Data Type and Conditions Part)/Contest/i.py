# Follow Me On FaceBook: www.facebook.com/codewithredoy

import math
import collections
# for i in range(int(input())):
# ...
# x, p = map(int, input().split())
s = input()
# num = int(input())
if s[1] == "0":
    print("YES")
    
elif int(s[0]) % int(s[1]) == 0 or int(s[1]) % int(s[0]) == 0:
    print("YES")
    
else:
    print("NO")