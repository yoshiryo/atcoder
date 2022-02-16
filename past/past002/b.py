s = input()
a_cnt = s.count("a")
b_cnt = s.count("b")
c_cnt = s.count("c")
ma = max(a_cnt, b_cnt, c_cnt)
if ma == a_cnt:
    print("a")
elif ma == b_cnt:
    print("b")
else:
    print("c")