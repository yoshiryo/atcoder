n = int(input())
num = set()
for a in range(2, 10**5+1):
    b = 2
    while a**b <= n:
        num.add(a**b)
        b += 1
print(n - len(num))