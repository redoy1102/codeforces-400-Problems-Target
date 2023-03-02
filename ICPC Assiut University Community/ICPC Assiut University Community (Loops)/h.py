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
    
    c = 0
    for i in range(2, n):
        if n %i == 0:
            c += 1
            
    if c > 0:
        print("NO")
    else:
        print("YES")
    

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
  


