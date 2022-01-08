import heapq
n, k = map(int, input().split())
a = list(map(int, input().split()))
q = a[:k]
print(min(q))
heapq.heapify(q)
for i in range(k, n):
    mi = heapq.heappop(q)
    if mi > a[i]:
        print(mi)
        heapq.heappush(q, mi)
    else:
        heapq.heappush(q, a[i])
        ans = heapq.heappop(q)
        print(ans)
        heapq.heappush(q, ans)