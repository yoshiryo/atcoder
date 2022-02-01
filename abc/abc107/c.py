import bisect

n, k = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
if 0 in x:
    k -= 1
idx = bisect.bisect_left(x, 0)
pos = [0]
neg = [0]
# 先頭に追加 0　のやり方簡単なのがない気がするので空リストに追加していく

pos_l = 1
neg_l = 1
for i in range(n):
    if x[i] < 0:
        neg.append(-x[i])
        neg_l += 1
    elif x[i] > 0:
        pos.append(x[i])
        pos_l += 1
neg.sort()  # ここを忘れていた。
ans = 10 ** 9  # INF
idx = -1
for i in range(k + 1):
    if i < neg_l and k - i < pos_l:
        ans = min(ans, pos[k - i] + neg[i] + min(neg[i], pos[k - i]))

print(ans)