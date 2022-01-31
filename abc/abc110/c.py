from typing import DefaultDict
s = input()
t = input()

s_dic = DefaultDict(int)
t_dic = DefaultDict(int)

for i in range(len(t)):
    a = s[i]
    b = t[i]
    if s_dic[a] == 0:
        s_dic[a] = b
    else:
        if s_dic[a] != b:
            print("No")
            exit()
    if t_dic[b] == 0:
        t_dic[b] = a
    else:
        if t_dic[b] != a:
            print("No")
            exit()
print("Yes")