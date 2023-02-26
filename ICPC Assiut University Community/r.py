# Follow me: www.facebook.com/codewithredoy
import math
# for _ in range(int(input())):
#     ...
# a, b = map(str, input().split())
# s = input()

num = int(input())
years = num // 365
num = num % 365
month = num // 30
num = num % 30

print(years, "years")
print(month, "months")
print(num, "days")
