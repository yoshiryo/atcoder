n, l, r = map(int, input().split())
bit = bin(n)[2:]
ans = 0
for k in range(len(bit)):
    if bit[len(bit) - k - 1] == "1":
        ma = max(l, 2**k)
        mi = min(r, 2**(k+1) - 1)
        if ma > mi:
            continue
        ans += mi - ma + 1
print(ans)