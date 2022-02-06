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
all = make_divisors(n)
ans = 10**10
for i in range(len(all)):
    a = str(all[i])
    b = str(n//all[i])
    f = max(len(a), len(b))
    ans = min(ans, f)
print(ans)