from math import gcd, log, floor, ceil, floor
from sys import stdin,stdout

stdstr = lambda: stdin.readline()
stdint = lambda: int(stdin.readline())
stdpr  = lambda x: stdout.write(str(x))

# ........................................ 
def palindrome(s):
    if s == s[::-1]:
        return "YES"
    else:
        return "NO"
    
def janina(rs):
    for i in range(len(rs)):
        if rs[i] != "0":
            return i

def solve():
    # n = int(input())
    # nums = [int(i) for i in input().split()][:n]
    # e, m, b = map(int, input().split())
    s = input()
    rs = s[::-1]
    
    print(rs[janina(rs):])
    print(palindrome(s))
    
    
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
  


