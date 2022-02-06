a, b = map(int, input().split())
score = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1]
a_score = score.index(a)
b_score = score.index(b)
if a_score > b_score:
    print("Alice")
elif a_score == b_score:
    print("Draw")
else:
    print("Bob")