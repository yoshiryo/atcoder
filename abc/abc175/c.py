x, k, d = map(int, input().split())

if k*d <= abs(x):
    print(abs(x) - k*d)
else:
    cnt = abs(x) // d
    p = abs(x) - d*cnt
    k -= cnt
    if k%2 == 1:
        p -= d
    print(abs(p)) 