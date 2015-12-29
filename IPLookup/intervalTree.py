import collections 

class Interval:

	def __init__(self, start, end, name):
		self.start = start
		self.end = end
		self.name = name
		self.size = abs(self.start - self.end)

		self.count = 0

	def within(self, point):
		return point >= self.start and point <= self.end

	def greaterThan(self, point):
		return point > self.end

	def lessThan(self, point):
		return point < self.start

	def increment(self):
		self.count += 1

	def __repr__(self):
		return self.name + ": [" + str(self.start) + ", " + str(self.end) + "]"  

class TreeNode:

	def __init__(self, x_center, leftNode, rightNode, centerVals):
		self.x_center = x_center
		self.leftNode = leftNode
		self.rightNode = rightNode
		self.centerBegin = sorted(centerVals, key=lambda x: x.start)
		self.centerEnd = sorted(centerVals, key=lambda x: x.end)

class IntervalTree:

	def __init__(self, intervals):
		#intervals is a dictionary of {name: [range1, range2, ...], ...}. Each range object is a two item tuple of two 32 bit ints representing IPs.
		self.intervalObjDict = collections.defaultdict(list)
		self.intervalList = []
		
		for interval in intervals:
			if isinstance(intervals[interval][0], list):
				for inter in intervals[interval]:
					tmp = Interval(inter[0], inter[1], interval)
					self.intervalObjDict[interval].append(tmp)
					self.intervalList.append(tmp)
			else:
				tmp = Interval(intervals[interval][0], intervals[interval][1], interval)
				self.intervalObjDict[interval].append(tmp)
				self.intervalList.append(tmp)

		self.head = self.divideIntervals(self.intervalList)

	def findCenter(self, intervals): #intervals = list of interval objects
		sortedIntervals = sorted(intervals, key=lambda x: x.start)
		return sortedIntervals[int(len(sortedIntervals)/2)].start		

	def divideIntervals(self, intervals):

		def divide(intervals):
			if len(intervals) == 0:
				return 

			left = []
			right = []
			center = []

			centerPoint = self.findCenter(intervals)

			for interval in intervals:
				if interval.lessThan(centerPoint):
					right.append(interval)
				elif interval.greaterThan(centerPoint):
					left.append(interval)
				elif interval.within(centerPoint):
					center.append(interval)
			return left, right, center, centerPoint

		left, right, center, centerPoint = divide(intervals)
		head = TreeNode(centerPoint, None, None, center)
		stack = [(left, right, head)]

		while len(stack) > 0:
			left, right, prevNode = stack.pop()

			if len(left) > 0:
				left1, right1, center1, centerPoint1 = divide(left)
				prevNode.leftNode = TreeNode(centerPoint1, None, None, center1)
				stack.append((left1, right1, prevNode.leftNode))

			if len(right) > 0:
				left2, right2, center2, centerPoint2 = divide(right)
				prevNode.rightNode = TreeNode(centerPoint2, None, None, center2)
				stack.append((left2, right2, prevNode.rightNode))
		return head

			

	def findSmallestRange(self, point):

		def searchHelper(node, resList):
			if node.x_center > point:
				for interval in node.centerBegin:
					if interval.start <= point:
						resList.append(interval)
				if node.leftNode:
					return searchHelper(node.leftNode, resList)
				else:
					return resList

			elif node.x_center < point:
				for interval in node.centerEnd:
					if interval.end >= point:
						resList.append(interval)
				if node.rightNode:
					return searchHelper(node.rightNode, resList)
				else:
					return resList

			elif node.x_center == point:
				resList.extend(node.centerBegin)
				return resList

		overlaps = searchHelper(self.head, [])
		print(overlaps)
		found = min(overlaps, key=lambda x: x.size) if len(overlaps) > 0 else None
		found.increment()
		return found

if __name__ == "__main__":
	intervals = {
		"Horatio Gates": [[1, 5],[22, 27]],
		"Charles Lee": [4, 12],
		"Israel Putnam": [6, 19],
		"Benedict Arnold": [2, 13],
		"Marquis de Lafayette": [17, 26],
		"Nathaniel Greene": [21, 30],
		"Rochambeau": [12, 15],
	}

	itree = IntervalTree(intervals)
	print(itree.findSmallestRange(14))







