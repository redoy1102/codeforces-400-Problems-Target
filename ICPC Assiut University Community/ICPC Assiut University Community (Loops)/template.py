from math import gcd, log, floor, ceil, floor
from sys import stdin,stdout

stdstr =lambda: stdin.readline()
stdint =lambda: int(stdin.readline())
stdpr  =lambda x: stdout.write(str(x))

# ........................................ 
def one(e, b):
  if e < 2 or b < 1:
    return 0
  else:
    if e >= b:
      res = e / 2
      return floor(res)
    elif b > e:
      return floor(e/2)
    
    

def two(e, m, b):
  if e < 2 or m < 1 or b < 1:
    return 0
  else:
    min(floor(e/2), m, b)

def three(e, m, b):
  if e < 1 or m < 1 or b < 1:
    return 0
  else:
    return min(e, m, b)


def solve():
  # num = int(input())
  e, m, b = map(int, input().split())
  # s = input()
  rOne = one(e, b)
  rTwo = two(e, m, b)
  rThree = three(e, m, b)
  # print(rTwo, rThree)
  
  print(max(rOne, rTwo, rThree))
  












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
  


