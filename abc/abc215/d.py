def make_divisors(n):
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            l.add(i)
            if i != n // i:
                l.add(n//i)
    return 

n, m = map(int, input().split())
a = list(map(int, input().split()))
l = set()
for i in range(n):
    make_divisors(a[i])
l = list(l)
judge = [True]*m
for i in range(len(l)):
    if l[i] == 1:
        continue
    k = 1
    while True:
        if l[i]*k > m:
            break
        else:
            index = l[i]*k - 1
            judge[index] = False
            k += 1
ans = []
for i in range(m):
    if judge[i]:
        ans.append(i+1)
print(len(ans))
for i in ans:
    print(i)