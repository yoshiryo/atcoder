n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ma = max(a)
mi = min(b)
if ma > mi:
    print(0)
else:
    print(mi - ma + 1)