from collections import Counter
n = int(input())
s = [input() for _ in range(n)]
c = Counter(s)
ans, _ = c.most_common()[0]
print(ans)