import bisect

n = int(input())
a = list(map(int, input().split()))
cake = sum(a)
if cake % 10 != 0:
    print("No")
    exit()
for i in range(n):
    a.append(a[i])
b = [a[0]]
for i in range(len(a) - 1):
    b.append(b[i] + a[i+1])
num = cake // 10

for i in range(n):
    j = bisect.bisect_left(b, num + b[i])
    if b[j] - b[i] == num:
        print("Yes")
        exit()
print("No")