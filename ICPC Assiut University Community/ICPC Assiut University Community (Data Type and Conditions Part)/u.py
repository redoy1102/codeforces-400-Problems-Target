# Follow me: www.facebook.com/codewithredoy

import math
# for _ in range(int(input())):
#     ...
# a, b, c = map(int, input().split())
s = input()
# num = float(input())

if "." in s:
    main = s.split(".")
    # print(main)
    if len(set(main[1])) == 1:
        zero = list(set(main[1]))
        if zero[0] == "0":
            print("int", int(main[0]))
        else:
            print("float", main[0], "0."+main[1])
    elif len(set(main[1])) > 1:
        print("float", main[0], "0."+main[1])
else:
    print("int", int(s))

