# Follow Me On FaceBook: www.facebook.com/codewithredoy

import sys
import math
import collections

input = sys.stdin.readline
    
def solve():
    # s = input()
    # num = int(input())
    n, k, a = map(int, input().split())

    quotient, remainder = divmod(n*k, a)
    # result = (n * k) / a

    # if result.is_integer():
    if remainder == 0:
        if -2**31 <= quotient <= 2**31-1:
            print("int")
        else:
            print("long long")
    else:
        print("double")
        
        
        
def main():
    # t = int(input())
    t = 1
    for _ in range(t):
        solve()
        
if __name__ == "__main__":
    main()
