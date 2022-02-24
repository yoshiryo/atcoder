n = int(input())
ans = set()
for _ in range(n):
    a = list(input().split())
    a.sort()
    b = "".join(a)
    ans.add(b)
print(len(ans))