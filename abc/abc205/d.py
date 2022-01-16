import bisect
n, q = map(int, input().split())
a = list(map(int, input().split()))
K = []
for _ in range(q):
    k = int(input())
    K.append(k)

C = [0] * n
for i in range(n):
    C[i] = a[i] - i - 1

for i in range(q):
    if C[n-1] < K[i]:
        print(a[n-1] + (K[i] - C[n-1]))
    else:
        tmp = bisect.bisect_left(C,K[i])
        print(a[tmp] - C[tmp] + K[i] - 1)