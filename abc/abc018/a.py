score = []
for i in range(3):
    a = int(input())
    score.append([a, i])
score = sorted(score, key=lambda x:x[0], reverse=True)
for i in range(3):
    score[i].append(i+1)
score = sorted(score, key=lambda x:x[1])
for i in range(3):
    print(score[i][2])
