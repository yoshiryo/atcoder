def make_divisors(n): #約数列挙
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

n = int(input())
ans = 0
for i in range(1, n+1):
    cnt = len(make_divisors(i))
    if cnt == 8 and i%2 != 0:
        ans += 1
print(ans)
