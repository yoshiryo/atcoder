import itertools

n = int(input())
all = itertools.product('abc', repeat=n)
for s in all:
    print("".join(s))