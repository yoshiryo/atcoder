n = int(input())
a = list(map(int, input().split()))
na = []
for i in range(n):
    na.append([a[i], i+1])
na = sorted(na, key=lambda x:x[0])

print(na[n-2][1])