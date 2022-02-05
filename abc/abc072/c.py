n = int(input())
a = list(map(int, input().split()))
cnt = [0]*(10**5 + 1)
for i in range(n):
    if a[i] - 1 >= 0:
        cnt[a[i] - 1] += 1
    cnt[a[i]] += 1
    cnt[a[i] + 1] += 1
print(max(cnt))