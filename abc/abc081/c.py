from collections import Counter
n, k = map(int, input().split())
a = list(map(int, input().split()))
c = Counter(a)
key = list(c.values())
key.sort()
print(sum(key[:-k]))