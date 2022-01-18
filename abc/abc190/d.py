def f1(n):
    divs = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divs.append(i)
            j = n // i
            if i != j:
                divs.append(j)
    return divs

N = int(input())
divs = f1(2 * N)
cnt = 0
for n in divs:
    X = (2 * N) // n
    if (X - n + 1) % 2 == 0:
        cnt += 1
print(cnt)