# エラトステネスの篩を使い、上限limitまでの素数列を取得する
def get_prime_list(limit):
    # nが素数なら、primep[n]==Trueとする配列を準備
    primep = [True] * (limit + 1)
 
    # 0, 1は素数から除外
    primep[0], primep[1] = False, False
 
    # 2～limitの平方根まで順番に見ていく
    for n in range(2, int(limit ** 0.5) + 1):
        # nが素数と確定したら、その倍数を全て素数から除外
        if primep[n] == True:
            for p in range(n * 2, limit + 1, n):
                primep[p] = False
 
    # 最後に素数だけを取り出す
    return [p for p in range(limit + 1) if primep[p]==True]
n = int(input())
mod = 10**9 + 7
l = get_prime_list(n)
all = []
for i in range(len(l)):
    num = n
    cnt = 0
    while num//l[i] > 0:
        cnt += num//l[i]
        num //= l[i]
    all.append(cnt)
ans = 1
for i in range(len(all)):
    ans = (ans%mod) * ((all[i] + 1)%mod)
print(ans%mod)