a, b, w = map(int, input().split())
w *= 1000
if a == b:
    if w % a == 0:
        print(w//a, w//b)
    else:
        print("UNSATISFIABLE")
else:
    MAX = w//a
    if w%b == 0:
        MIN = w//b
    else:
        MIN = w//b + 1

    if MAX >= MIN:
        print(MIN, MAX)
    else:
        print("UNSATISFIABLE")