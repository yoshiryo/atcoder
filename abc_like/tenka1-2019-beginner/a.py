a, b, c = map(int, input().split())
ma = max(a, b)
mi = min(a, b)
if mi <= c <= ma:
    print("Yes")
else:
    print("No")