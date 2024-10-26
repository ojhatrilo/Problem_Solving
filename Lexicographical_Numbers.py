
def lexNumbers(n):
	sol = []
	dfs(1, n, sol)
	print("[", sol[0], end= "", sep ="")
	for i in range(1,n):
		print(", ", sol[i], end= "", sep ="")
	print("]")


def dfs(temp, n, sol):
	if (temp > n):
		return
	sol.append(temp)
	dfs(temp * 10, n, sol)
	if (temp % 10 != 9):
		dfs(temp + 1, n, sol)

n = 15
lexNumbers(n)






