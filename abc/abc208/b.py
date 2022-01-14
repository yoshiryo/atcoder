p = int(input())
coin = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
coin.sort(reverse=True)
ans = 0
for i in range(len(coin)):
    if p >= coin[i]:
        cnt = p//coin[i]
        ans += cnt
        p -= cnt*coin[i]
print(ans)