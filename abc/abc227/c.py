n = int(input())
ans = 0
for a in range(1, n+1):
    if a*a*a > n:
        break
    for b in range(a, n+1):
        if a*b*b > n:
            break
        ab = a*b
        cmi = b
        cma = n//ab
        ans += cma - cmi + 1
print(ans)