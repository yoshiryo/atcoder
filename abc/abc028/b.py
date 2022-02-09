s = input()
alp = ["A", "B", "C", "D", "E", "F"]
ans = []
for a in alp:
    ans.append(s.count(a))
print(*ans)