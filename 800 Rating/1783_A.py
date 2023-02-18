for _ in range(int(input())):
    n = int(input())
    
    a = [int(i) for i in input().split()][:n]
    
    if len(set(a)) == 1:
        print("NO")
    else:
        print("YES")
        print(a[0],end=' ')
        
        aa = a[1:]
        aa.sort(reverse=True)
        for i in aa:
            print(i,end=' ')
            
        print()