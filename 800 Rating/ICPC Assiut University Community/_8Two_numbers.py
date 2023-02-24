import math
from decimal import Decimal, ROUND_HALF_UP

a, b = map(int, input().split())
fl = a // b
cl = math.ceil(a/b)

rn = Decimal(a / b)
res = rn.quantize(Decimal(1), rounding = ROUND_HALF_UP)

print("floor {} / {} = {}".format(a, b, fl))
print("ceil {} / {} = {}".format(a, b, cl))
print("round {} / {} = {}".format(a, b, res))