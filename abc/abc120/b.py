a, b, k = map(int, input().split())
all = []
for i in range(1, 101):
    if a%i == 0 and b%i == 0:
        all.append(i)
all = all[::-1]
print(all[k-1])