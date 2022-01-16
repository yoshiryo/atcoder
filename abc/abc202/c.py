n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a_cnt = [0]*n
b_cnt = [0]*n

for i in range(n):
    a_cnt[a[i] - 1] += 1
    b_cnt[b[c[i] - 1] - 1] += 1
ans = 0
for i in range(n):
    ans += a_cnt[i] * b_cnt[i]
print(ans)