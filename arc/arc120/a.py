from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))

cumsum = list(accumulate(A))
ans = 0
maximum = 0
for i in range(N):
    maximum = max(maximum, A[i])
    ans += cumsum[i]
    print(ans + maximum * (i + 1))
