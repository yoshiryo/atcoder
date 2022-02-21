n = int(input())
s = list(map(int, input().split()))
t = int(input())
ans = set()
for i in range(n):
    ans.add(s[i]//t)
print(len(ans))