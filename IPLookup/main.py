import intervalTree
import collections

def parseRanges(filename): #returns the {name: [[range1, range2], [...], ...], ...} IntervalTree expects
	nameToRanges = collections.defaultdict(list)
	with open(filename) as f:
		for line in f.read().strip().split("\n"):
			splitted = line.split(" ")
			for i in range(len(splitted[:2])):
				tmp = splitted[i].split(".")
				for ind, num in enumerate(tmp):
					while len(num) < 3:
						num = "0" + num
					tmp[ind] = num
				splitted[i] = ".".join(tmp)
			range1 = [int(splitted[0].replace(".", "")), int(splitted[1].replace(".", ""))]
			nameToRanges[" ".join(splitted[2:])].append(range1)
	print(nameToRanges)	
	return intervalTree.IntervalTree(nameToRanges)
