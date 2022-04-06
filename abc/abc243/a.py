v, a, b, c = map(int, input().split())
all = a + b + c
if all <= v:
    cnt = v//all
    v -= all*cnt
if v < a:
    print("F")
elif v - a < b:
    print("M")
else:
    print("T")