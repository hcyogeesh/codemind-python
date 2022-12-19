
def findWinner(M, N):
	if (M % 2 == 0 or N % 2 == 0):
		print("Player 1");
	else:
		print("Player 2");

M, N = map(int, input().split());
findWinner(M, N);

