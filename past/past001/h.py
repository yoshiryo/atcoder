n = int(input())
c = list(map(int, input().split()))
q = int(input())
all_mi = min(c)
odd_mi = min(c[::2])
all_sale = 0
odd_sale = 0
index_sale = 0
for _ in range(q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        x, a = s[1:]
        re = c[x-1] - all_sale - a
        if x%2 == 1:
            re -= odd_sale
        if re >= 0:
            index_sale += a
            c[x-1] -= a
            all_mi = min(all_mi, re)
            if x%2 == 1:
                odd_mi = min(odd_mi, re)
    elif s[0] == 2:
        a = s[1]
        if odd_mi >= a:
            odd_sale += a
            odd_mi -= a
            all_mi = min(all_mi, odd_mi)
    else:
        a = s[1]
        if all_mi >= a:
            all_sale += a
            all_mi -= a
            odd_mi -= a
print(all_sale*n + odd_sale*((n+1)//2) + index_sale)
