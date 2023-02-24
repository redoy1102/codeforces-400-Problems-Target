for _ in range(int(input())):
    n = int(input())
    a = input()
    
    for i in range(1, n):
        if i %2 == 1 and a[i] == "1":
            print("-",end="")
        elif i %2 == 0 and a[i] == "1":
            print("+",end="")
    print()