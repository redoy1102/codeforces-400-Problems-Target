from math import gcd, log, floor, ceil, floor
from sys import stdin,stdout

stdstr =lambda: stdin.readline()
stdint =lambda: int(stdin.readline())
stdpr  =lambda x: stdout.write(str(x))

# ........................................ 

def solve():
    n = int(input())
    # e, m, b = map(int, input().split())
    # s = input()
    if n == 1:
        print(-1)
    else:
        for i in range(2, n+1, 2):
            print(i)
  




# ........................................

def check():
  print(floor(2.0))
  
def main():
  # t = int(input())
  t = 1
  for _ in range(t):
    solve()
    # check()

if __name__ == "__main__":
  main()
  


