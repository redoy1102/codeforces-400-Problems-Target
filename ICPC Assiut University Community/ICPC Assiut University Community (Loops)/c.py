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
    numbers = [int(i) for i in input().split()][:n]
    even = odd = pos = neg = 0
    
    for i in numbers:
        if i %2 == 0:
            even += 1
        if i < 0:
            neg += 1
        if i > 0:
            pos += 1
        if i %2 != 0:
            odd += 1
            
    print("Even:", even)
    print("Odd:", odd)
    print("Positive:", pos)
    print("Negative:", neg)
    
    
  

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
  


