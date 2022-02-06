t = int(input())
for _ in range(t):
    a, s = map(int, input().split())
    a_bit = format(a, 'b')
    s_bit = format(s, 'b')
    a_bit = a_bit[::-1]
    s_bit = s_bit[::-1]
    print(a_bit, s_bit)
    ans = "Yes"
    for i in range(len(a_bit)):
        if a_bit[i] == "1":
            if len(s_bit) < i+2 or s_bit[i+1] != "1":
                ans = "No"
                break
    print(ans)