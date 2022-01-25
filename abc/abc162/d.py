n = int(input())
s = input()
all = s.count("R")*s.count("G")*s.count("B")

for i in range(n-2):
    for j in range(i+1, n-1):
        k = 2*j - i
        if k > n-1:
            continue
        if s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
            all -= 1
print(all)
