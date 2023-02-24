for i in range(int(input())):
    n = int(input())
    s = input()
    
    if len(s) == n:
        start = 0
        end = n-1
        res = n
        
        while True:
            if s[start] == s[end]:
                print(res)
                break
            else:
                res = res - 2
                start += 1
                end -= 1
        print(res)