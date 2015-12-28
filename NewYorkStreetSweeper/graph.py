
class Graph(object):

	def __init__(self, filename):
		with open(filename) as f:
			lines = f.read().split("\n")
			self.height = int(lines[0].split(" ")[0])
			self.width = int(lines[0].split(" ")[1])
			self.start = lines[1]
			graphAscii = "\n".join(lines[2:]).rstrip()

		self.adjList = {}
		self.parseGraph(graphAscii)

	def parseGraph(self, graphText):
		tmp = {}

		for y, line in enumerate(graphText.split("\n")):
			for x, char in enumerate(line.split()):
				tmp[(x, y)] = char
		print(tmp)

		print(tmp[(0,0)])
		print(tmp[(0,1)])
		print(tmp[(1,0)])

		# for point in tmp:
		# 	currX, currY = point
		# 	up, down, left, right = tmp.get((currX*2, currY+1), None), tmp.get((currX*2, currY-1), None), tmp.get((currX-1, currY), None), tmp.get((currX+1, currY), None)
		# 	if tmp[point].isupper():
		# 		adlist = []
		# 		if up == "|" or up == "^":
		# 			print("inside up" + str(up))
		# 			adlist.append(tmp[currX, currY+2])
		# 		if down == "|" or down == "v":
		# 			print("inside down" + str(down))
		# 			adlist.append(tmp[currX, currY-2])
		# 		if left == "<" or left == "-":
		# 			print("inside left" + str(left))
		# 			adlist.append(tmp[currX-2, currY])
		# 		if right == ">" or right == "-":
		# 			print("inside right" + str(right))
		# 			adlist.append(tmp[currX+2, currY])
		# 		self.adjList[tmp[point]] = adlist

		for y, line in enumerate(graph.split("\n")):
		    for x, c in enumerate(line.rstrip().split()):
		        left, right, up, down = points.get((x - 1, y)), points.get((x + 1, y)), points.get((x * 2, y - 1)), points.get((x * 2, y + 1))
		        
		        if c in "->":
		            self.adjList[left].append(right)
		        if c in "-<":
		            self.adjList[right].append(left)
		        if c in "|^":
		            self.adjList[down].append(up)
		        if c in  "|v":
		            self.adjList[up].append(down)






