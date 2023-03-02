from math import gcd, log, floor, ceil, floor
from sys import stdin,stdout

stdstr = lambda: stdin.readline()
stdint = lambda: int(stdin.readline())
stdpr  = lambda x: stdout.write(str(x))

# ........................................ 

def solve():
    n = int(input())
    # nums = [int(i) for i in input().split()][:n]
    # e, m, b = map(int, input().split())
    # s = input()
    
    for j in range(2, n+1):
        c = 0
        for i in range(2, j):
            if j %i == 0:
                c += 1
                
        if c == 0:
            print(j, end=" ")

# ........................................

def check():
    pass
        
  
def main():
    # t = int(input())
    t = 1
    for _ in range(t):
        solve()
        
    # check()

if __name__ == "__main__":
  main()
  


