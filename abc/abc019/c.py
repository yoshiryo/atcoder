n = int(input())
a = list(map(int, input().split()))
ans = set()
for i in range(n):
    while a[i]%2 == 0:
        a[i] //= 2
    ans.add(a[i])
print(len(ans))