from itertools import accumulate

n = int(input())
a = list(map(int, input().split()))

s = list(accumulate(a))  # S: Aの累積和
x = [0] + list(accumulate(s)) # X: iターン目のスタート位置
v = list(accumulate(s, func=max))  # V: iターン目での変位の最大値

ans = max(x[i] + v[i] for i in range(n))  # X[i] + V[i]: iターン目でのx座標の最大値
print(max(0, ans))