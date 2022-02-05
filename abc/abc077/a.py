s1 = input()
s2 = input()
t1 = s1[::-1]
t2 = s2[::-1]

if s1 == t2 and s2 == t1:
    print("YES")
else:
    print("NO")