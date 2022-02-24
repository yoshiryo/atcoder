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
ab = []
for _ in range(n):
    a, b = map(int, input().split())
    ab.append([a, b])

all1 = make_divisors(ab[0][0])
all1.sort(reverse=True)
ans1 = 1
for x in all1:
    judge = True
    for i in range(n):
        if ab[i][0]%x != 0 and ab[i][1]%x != 0:
            judge = False
            break
    if judge:
        ans1 = x
        break

all2 = make_divisors(ab[0][1])
all2.sort(reverse=True)
ans2 = 1
for x in all2:
    judge = True
    for i in range(n):
        if ab[i][0]%x != 0 and ab[i][1]%x != 0:
            judge = False
            break
    if judge:
        ans2 = x
        break
print(max(ans1, ans2))