#https://www.reddit.com/r/dailyprogrammer/comments/31aja8/20150403_challenge_208_hard_the_universal_machine/

class Tape(object):
	def __init__(self, string):
		self.string = string
		self.indexToTape = {}

		for index, char in enumerate(self.string):
			self.indexToTape[index] = char

	def accessTape(self, index):
		return self.indexToTape.get(index, "_")

	def setTape(self, index, value):
		self.indexToTape[index] = value

	def printAll(self, readhead):
		final = ""
		lineBelow = ""
		for key in self.indexToTape:
			if key == 0:
				lineBelow += "|"
			elif key == readhead and key != 0:
				lineBelow += "^"
			else:
				lineBelow += " "
			final += self.indexToTape[key]
		if self.indexToTape[readhead] == "_" or self.indexToTape[0] == "_":
			return final + "\n" + lineBelow
		else:
			return final.replace("_", "") + "\n" + lineBelow

class TuringMachine(object):

	def __init__(self, input):
		text = open(input).read()
		self.parseInput(text)
		self.readhead = 0

	def parseInput(self, input):
		lines = input.strip().split('\n')
		self.alphabet = lines[0]
		self.states = lines[1].split()
		self.state = lines[2]
		self.accepting = lines[3]
		self.tape = Tape(lines[4])
		self.transitionHash = {}
		for string in lines[5:]:
			rule = string.split("=")
			h1 = rule[0].split()
			h2 = rule[1].split()
			self.transitionHash[(h1[0], h1[1])] = (h2[0], h2[1], h2[2])

	def printAll(self):
		print(self.alphabet)
		print(self.states)
		print(self.state)
		print(self.accepting)
		print(self.tape)
		print(self.transitionHash)

	def execute(self):
		readDict = {
			">" : lambda: self.readhead + 1,
			"<" : lambda: self.readhead - 1
		}
		while self.state != self.accepting:
			transition = self.transitionHash[(self.state, self.tape.accessTape(self.readhead))]
			self.state = transition[0]
			self.tape.setTape(self.readhead, transition[1])
			self.readhead = readDict[transition[2]]()
		return self.tape.printAll(self.readhead)

if __name__ == "__main__":
	turing = TuringMachine('inputTuring.txt')
	print(turing.execute())
