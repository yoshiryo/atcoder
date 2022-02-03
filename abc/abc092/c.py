n = int(input())
a = list(map(int, input().split()))
b =[0]
for i in a:
    b.append(i)
b.append(0)

cnt = 0
for i in range(n+1):
    cnt += abs(b[i+1] - b[i])

for i in range(1, n+1):
    print(cnt - abs(b[i]-b[i-1]) - abs(b[i+1]-b[i]) + abs(b[i+1]-b[i-1]))


