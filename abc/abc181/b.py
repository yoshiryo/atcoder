n = int(input())
ans = 0
for _ in range(n):
    a, b = map(int, input().split())
    num = b - a + 1
    ans += num*(a+b)//2
print(ans)