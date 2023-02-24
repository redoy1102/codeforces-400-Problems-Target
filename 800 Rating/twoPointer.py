def pairSum(arr, s):
    for i in arr:
        for j in arr:
            if i == j:
                continue
            elif i + j == s:
                return True
            elif i + j > s:
                break
    return False

num = [1,2,3,4]
search = 8

res = pairSum(num, search)
print(res)