n, m = map(int, input().split())
a = n - m
time = 1900*m + a*100
print(int(time * 2**m))