n = int(input())
p = list(map(int, input().split()))
q = []
l = []
for i in range(n):
    l.append([p[i], i+1])
l = sorted(l, key=lambda x:x[0])
for i in range(n):
    q.append(l[i][1])
print(*q)