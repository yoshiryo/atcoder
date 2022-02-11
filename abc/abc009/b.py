n = int(input())
s = [int(input()) for _ in range(n)]
s = list(set(s))
s.sort()
print(s[-2])