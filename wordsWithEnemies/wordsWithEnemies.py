from wordsAI import WordsAI
import random

class WordsWithEnemies:
	#implement game. trivial, so I don't want to do it. fuck it. 
	
	def __init__(self, difficulty, letterLen=8):
		self.ai = WordsAI('dictionary.txt', 'lebgna', difficulty)
		self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
		self.letterLen = 8

		self.aiScore = 0
		self.humanScore = 0

	def generateLetters(self):
		final = ''
		for i in range(len(self.letterLen)):
			final += random.choice(self.alphabet)
		return final

	def wordTest(self, humanWord, aiWord):
		collisions = set(humanWord + aiWord)
		leftOverHuman = humanWord
		leftOverAI = aiWord
		for collision in collisions:
			leftOverHuman = leftOverHuman.replace(collision)
			leftOverAI = leftOverAI.replace(collision)
		if len(leftOverAI) > len(leftOverHuman):
			self.aiScore += 1
			return "The AI won this round. AI score is " + str(self.aiScore) + ". Humans are at " + str(self.humanScore) + "."
		if len(leftOverAI) < len(leftOverHuman):
			self.aiScore += 1
			return "The Humans won this round. AI score is " + str(self.aiScore) + ". Humans are at " + str(self.humanScore) + "."
		if len(leftOverAI) > len(leftOverHuman):
			self.aiScore += 1
			return "Tie. AI score is " + str(self.aiScore) + ". Humans are at " + str(self.humanScore) + "."	
