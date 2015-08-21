#https://www.reddit.com/r/dailyprogrammer/comments/3h0uki/20150814_challenge_227_hard_adjacency_matrix/

dirMap = {
	'|': [0, -1],
	'-': [1, 0],
	'\\': [1, 1],
	'/': [-1, -1]
}


def parseInput(filename):
	with open(filename, 'r') as graph:
		graphTxt = graph.read()
		graphArr = [0]*len(graphTxt.splitlines()[1:])
		for ind, line in enumerate(graphTxt.splitlines()[1:]):
			graphArr[ind] = list(line)
	return graphArr

def getNodes(graphArr):
	nodeList = []
	for x, lin in enumerate(graphArr):
		for y, char in enumerate(lin):
			if char not in ['\\', '-', '+', '/', '#', ' ', '|']:
				nodeList.append((char, x, y))
	return nodeList

def getNeighbors(graphArr, node):
	neighbors = []
	for node in nodeList:
		for x in range(node[0], node[0]+1):
			for y in range(node[0], node[0]+1):
				if x < len(graphArr) - 1 and x >= 0 and y < len(graphArr[x]) - 1 and y <= 0:
					if 

