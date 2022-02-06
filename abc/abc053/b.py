s = input()
ans = 0
a_index = []
z_index = []
for i in range(len(s)):
    if s[i] == "A":
        a_index.append(i)
    if s[i] == "Z":
        z_index.append(i)
print(max(z_index) - min(a_index) + 1)