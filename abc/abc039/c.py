s = input()
all = "WBWBWWBWBWBWWBWBWWBWBWBWWBWBWWBWBWBWWBWBWWBWBWBW"
A = ["Do","Re","Mi","Fa","So","La","Si"]
B = [0,2,4,5,7,9,11]

for i in range(7):
	if s == all[B[i]:B[i]+20]:
		print(A[i])