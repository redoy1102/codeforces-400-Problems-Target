n, k, a = map(int, input().split())

result = (n * k) / a

if result.is_integer():
    if -2**31 <= result <= 2**31-1:
        print("int")
    else:
        print("long long")
else:
    print("double")
