n, k = map(int, input().split())
p = list(map(int, input().split()))

num_li = [0]*n

for i in range(n):
    num_li[i] = (p[i]+1)/2

num = sum(num_li[:k])
ans = num

for j in range(n-k):
    num = num-num_li[j]+num_li[j+k]
    ans = max(num, ans)

print(ans)