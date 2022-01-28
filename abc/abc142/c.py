n = int(input())
a = list(map(int, input().split()))
students = []
for i in range(n):
    students.append([a[i], i+1])
students = sorted(students, key=lambda x:x[0])
ans = []
for s in students:
    ans.append(s[1])
print(*ans)