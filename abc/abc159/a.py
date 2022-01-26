import itertools
n, m = map(int, input().split())
print(len(list(itertools.combinations(range(n), 2))) +  len(list(itertools.combinations(range(m), 2))))
