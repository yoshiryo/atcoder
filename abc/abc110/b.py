n, m, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
ma = max(x)
mi = min(y)
for i in range(X+1, Y+1):
    if ma < i <= mi:
        print("No War")
        exit()
print("War")