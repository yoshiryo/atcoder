def score(S):
    res = 0
    for i in range(1,10):
        tmp = S.count(str(i))   
        res += i * 10 ** tmp    
    return res

k = int(input())
s = input()
s = s[:-1]
t = input()
t = t[:-1]
cnt = [k] * 10 
for i in s:
    cnt[int(i)] -= 1
for j in t:
    cnt[int(j)] -= 1

ans = 0
for i in range(1,10):
    if cnt[i] == 0: 
        continue
    for j in range(1,10):
        if i == j or cnt[j] == 0:   
            continue
        if score(s + str(i)) > score(t + str(j)):
            ans += cnt[i] * cnt[j] 

for i in range(1,10):
    if cnt[i] < 2:  
        continue
    if score(s + str(i)) > score(t + str(i)):   
        ans += cnt[i] * (cnt[i] - 1) 

all = 9 * k - 8  

print(ans / all / (all-1))