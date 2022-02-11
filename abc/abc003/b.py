s = input()
t = input()
allow = ["a", "t", "c", "o", "d", "e", "r"]
judge = True
for i in range(len(s)):
    if s[i] != t[i]:
        if (s[i]=="@" and t[i] in allow) or (t[i]=="@" and s[i] in allow):
            pass
        else:
            judge = False
if judge:
    print("You can win")
else:
    print("You will lose")