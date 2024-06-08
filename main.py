import copy
board = []

n = 8

for i in range(n):
	tmp = []
	for q in range(n):
		tmp.append(0)
	board.append(tmp)

answers = set()

def place(board_copy, y, x, to_place_counter):
	n = len(board_copy)

	for i in range(n):
		board_copy[y][i] = '-'
		board_copy[i][x] = '-'

	for i in range(1, n):
		if y-i >= 0 and x-i >= 0: #типа вверх влево
			board_copy[y-i][x-i] = '-'

		if y+i < n and x+i < n:  #вниз вправо
			board_copy[y+i][x+i] = '-'
		if y+i < n and x-i >= 0: #вниз влево 
			board_copy[y+i][x-i] = '-'
		if y-i >= 0 and x+i < n:  # вверх вправо
			board_copy[y-i][x+i] = '-'

	board_copy[y][x] = 'q'

	if to_place_counter == 0:
		global answers
		print("Found", len(answers), "answers", end='\r')
		answers.add(tuple(tuple(row) for row in board_copy))

	to_place_counter -= 1

	#debug
	if to_place_counter and False:
		print("I have to place", to_place_counter, "queens. Current board:")
		for line in board_copy:
			print(' '.join(map(str, line)))


	for i in range(n):
		for q in range(n):
			pass
			if board_copy[i][q] == 0:
				place(copy.deepcopy(board_copy), i, q, to_place_counter)


to_place_counter = 8
try:
	for i in tqdm(range(n)):
		for q in tqdm(range(n)):
			print("Found", len(answers), "answers",i, q, end = '\r')
			pass
			if board[i][q] == 0:
				place(copy.deepcopy(board), i, q, to_place_counter-1)
except KeyboardInterrupt:
	pass
print(i, q, "Found", len(answers), "answers")

print("Result")

counter = 1
for board in answers:
	print("Answer number", counter)
	counter += 1
	for line in board:
		print(' '.join(map(str, line)))
	print()