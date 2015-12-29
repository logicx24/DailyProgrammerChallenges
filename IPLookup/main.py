#https://www.reddit.com/r/dailyprogrammer/comments/3xdmtw/20151218_challenge_245_hard_guess_whois/

import intervalTree
import collections

def parseRanges(filename): #returns the {name: [[range1, range2], [...], ...], ...} IntervalTree expects
	nameToRanges = collections.defaultdict(list)
	with open(filename) as f:
		for line in f.read().strip().split("\n"): #making sure zeros are added correctly
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
	return nameToRanges

def runQueries(nameToRanges, queryFilename):
	itree = intervalTree.IntervalTree(nameToRanges)
	unknown = 0
	with open(queryFilename) as f:
		for line in f.read().strip().split("\n"): #making sure zeros are added correctly
			for i in range(len(line)):
				tmp = line.split(".")
				for ind, num in enumerate(tmp):
					while len(num) < 3:
						num = "0" + num
					tmp[ind] = num
				line = ".".join(tmp)
			ip = int(line.replace(".", ""))
			if not itree.findSmallestRange(ip):
				unknown += 1
	orgToCount = {}
	for key in itree.intervalObjDict:
		orgToCount[key] = sum(i.count for i in itree.intervalObjDict[key])

	return orgToCount

def toString(orgToCount):
	return "\n".join(str(orgToCount[key]) + " - " + key for key in orgToCount)

if __name__ == "__main__":
	print(toString(runQueries(parseRanges("smallinputranges.txt"), "smallQueryFile.txt")))


