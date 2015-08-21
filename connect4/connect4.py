
grid = []

for _ in range(6):
	r = []
	for z in range(7):
		r.append(0)
	grid.append(r)


lettersToIndex = {
	'a': 0,
	'b': 1,
	'c': 2,
	'd': 3,
	'e': 4,
	'f': 5,
	'g': 6
}

indexToLetters = {
	0: 'a',
	1: 'b',
	2: 'c',
	3: 'd',
	4: 'e',
	5: 'f',
	6: 'g'
}

xPieces = []
oPieces = []

def gridStr(grid):
	string = ""
	for row in grid:
		for col in row:
			string += str(col)
			string += " "
		string += "\n"
	return string

def run(filename):
	with open(filename, 'r') as movesFile:
		movesFile = movesFile.read()
		for ind, line in enumerate(movesFile.splitlines()):
			spl = line.split()
			makeMove(grid, spl[0].lower(), spl[1].lower())
			print(line)
			print(gridStr(grid))
			res = checkWin(grid)
			if res[0] == 'X':
				print('X won at move ' + str(ind + 1) + " (with " + " ".join(indexToLetters[res[1][i][1]].upper() + str(6-res[1][i][0]) for i in range(len(res[1]))) + ")")
				return
			elif res[0] == 'O':
				print('O won at move ' + str(ind + 1) + " (with " + " ".join(indexToLetters[res[1][i][1]].upper() + str(6-res[1][i][0]) for i in range(len(res[1]))) + ")") 
				return

def makeMove(grid, XMove, OMove):
	XRow = findOpenRow(grid, lettersToIndex[XMove])
	grid[XRow][lettersToIndex[XMove]] = 'X'
	ORow = findOpenRow(grid, lettersToIndex[OMove])
	grid[ORow][lettersToIndex[OMove]] = 'O'
	xPieces.append((XRow, lettersToIndex[XMove]))
	oPieces.append((ORow, lettersToIndex[OMove]))

def findOpenRow(grid, column):
	for i in range(6)[::-1]:
		if grid[i][column] == 0:
			return i

def checkWin(grid):
	for piece in xPieces:
		xWin = hasWinningChain(piece, 'X')
		if xWin[0]:
			return 'X', xWin[1]
	for piece in oPieces:
		oWin = hasWinningChain(piece, 'O')
		if oWin[0]:
			return 'O', oWin[1]
	return 'N', []

def hasWinningChain(piece, player):
	directions = [[1,0], [0,1], [1,1], [-1,-1], [-1,0], [0,-1], [1,-1], [-1,1]]
	for direction in directions:
		res = hasDiag(piece, direction, player)
		if res[0]:
			return (True, res[1])
	return (False, [])

def hasDiag(piece, direction, player):
	y = piece[0]
	x = piece[1]
	count = 0
	chain = []
	while y >= 0 and y < len(grid) and x >= 0 and x < len(grid[y]):
		if grid[y][x] != player:
			return (False, [])
		if grid[y][x] == player:
			chain.append((y, x))
			count += 1
		x += direction[1]
		y += direction[0]
		if count >= 4:
			return (True, chain)
	return (False, [])

