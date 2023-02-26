# Follow me: www.facebook.com/codewithredoy

import math
# for _ in range(int(input())):
#     ...
a, b, c = map(int, input().split())
# s = input()
# num = float(input())

numbers = list((a, b, c))
cp = numbers.copy()

cp.sort()
for i in cp:
    print(i)
print()

for i in numbers:
    print(i)