n = int(input())
st = []
for _ in range(n):
    s, t = input().split()
    t = int(t)
    st.append([s, t])
st = sorted(st, key=lambda x:x[1])
print(st[n-2][0])