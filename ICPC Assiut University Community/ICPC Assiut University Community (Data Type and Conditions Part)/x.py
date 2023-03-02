# Follow me: www.facebook.com/codewithredoy

import math
# for _ in range(int(input())):
#     ...
l1, r1, l2, r2 = map(int, input().split())
# s = input()
# num = int(input())

if r1 < l2 or r2 < l1:
    print(-1)
else:
    l = max(l1, l2)
    r = min(r1, r2)
    print(l, r)
