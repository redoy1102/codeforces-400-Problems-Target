# Follow Me On FaceBook: www.facebook.com/codewithredoy

import math
import sys
input = sys.stdin.readline


def solve():
    # a, b, k = map(int, input().split())
    # s = input()
    # num = int(input())
    
    s = input()
    if s == "z":
        print("a")
    else:
        aCode = ord(s)
        print(chr(aCode+1))

    # if a % k == 0 and b % k == 0:
    #     print("Both")
    # elif a % k == 0 and b % k != 0:
    #     print("Memo")
    # elif a % k != 0 and b % k == 0:
    #     print("Momo")
    # elif a % k != 0 and b % k != 0:
    #     print("No One")


def main():
    # t = int(input())
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
