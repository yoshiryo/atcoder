n = int(input())
c1_sum = [0]
c2_sum = [0]
sum1 = 0
sum2 = 0
for i in range(n):
    c, p = map(int, input().split())
    if c == 1:
        sum1 += p
    else:
        sum2 += p
    c1_sum.append(sum1)
    c2_sum.append(sum2)

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    score1 = c1_sum[r] - c1_sum[l-1]
    score2 = c2_sum[r] - c2_sum[l-1]
    print(score1, score2)
