n = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
a1_cnt = 0
a2_cnt = sum(a2)
ans = 0
for i in range(n):
    a1_cnt += a1[i]
    ans = max(ans, a1_cnt + a2_cnt)
    a2_cnt -= a2[i]
print(ans)