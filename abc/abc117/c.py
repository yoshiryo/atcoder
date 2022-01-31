n, m = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
y = []
for i in range(m-1):
    y.append(x[i+1] - x[i])
y.sort()
if n >= m:
    print(0)
else:
    print((sum(y[:m-n])))