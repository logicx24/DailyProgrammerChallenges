#https://www.reddit.com/r/dailyprogrammer/comments/2tfs0b/20150123_challenge_198_hard_words_with_enemies/
import random

class WordsAI:

	def __init__(self, dictFile, letters, diff):
		self.dictionary = self.getDictionary(dictFile)
		self.letters = letters
		self.letterLen = len(letters)
		self.tree = self.buildPrefixTree()
		self.diff = diff
		self.condDict = self.generateCondDict(self.letterLen)
		self.soln = self.wordSearch()	
		#add scrabble scoring to weight the random choice to improve the function

	def generateCondDict(self, letterLen):
		return {
			1 : lambda length : True,
			2 : lambda length : length >= letterLen/3,
			3 : lambda length : length >= letterLen/2,
			4 : lambda length : length >= int(letterLen/1.5),
			5 : lambda length : length == letterLen
		}	

	def setLetters(self, letters):
		self.letters = letters
		self.letterLen = len(letters)
		self.condDict = self.generateCondDict(self.letterLen)
		self.soln = self.wordSearch()

	getDictionary = lambda self, filename: open(filename, 'r').read().split("\n")

	def buildPrefixTree(self):
		prefixTree = {}
		dictionary = self.dictionary
		for word in dictionary:
			currDict = prefixTree
			for letter in word:
				if letter in currDict:
					currDict = currDict[letter]
				else:
					currDict[letter] = {}
					currDict = currDict[letter]
			currDict["_end"] = "_end"
		return prefixTree

	def checkWord(self, word):
		tree = self.tree
		curr = tree
		for letter in word:
			if letter in curr:
				curr = curr[letter]
			else:
				return False
		return '_end' in curr

	def permutations(self, letters):
		if len(letters) <= 1:
			yield letters
		else:
			perms = self.permutations(letters[1:])
			curr = letters[0]

			for perm in perms:
				for i in range(len(perm) + 1):
					yield perm[:i] + curr + perm[i:]

	def wordSearch(self):
		tree = self.tree
		letters = self.letters
		
		def wordSearchHelper(tree, letters, successfulWords):
			for perm in self.permutations(letters):
				if self.checkWord(perm) and perm not in successfulWords:
					successfulWords.append(perm)
			if len(letters) > 1:
				for i in range(0, len(letters)):
					wordSearchHelper(tree, letters[:i] + letters[i+1:], successfulWords)
			return successfulWords
			""""WKIXQKSU"""
		return wordSearchHelper(tree, letters, [])

	def chooseDiff(self, condition):
		words = self.soln
		choiceList = [word for word in words if condition(len(word))]
		return random.choice(choiceList) if len(choiceList) > 0 else ''

	def choose(self, difficulty):
		return self.chooseDiff(self.condition(difficulty))

	def condition(self, level):
		return self.condDict[level]

	def execute(self):
		res = self.choose(self.diff)
		diff = self.diff
		letterLen = self.letterLen
		while len(res) == 0 and letterLen > 0:
			letterLen = letterLen - 1
			self.condDict = self.generateCondDict(letterLen)
			res = self.choose(diff)
		return res

if __name__ == "__main__":
	ai = WordsAI('dictionary.txt', 'lebgna', 5)
	ai.execute()
	ai.setLetters("wistful")
	print(ai.execute())
	ai.setLetters("agronst")
	print(ai.execute())
	ai.setLetters("prosacidlf")
	print(ai.execute())



