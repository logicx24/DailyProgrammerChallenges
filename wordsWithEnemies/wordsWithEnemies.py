from wordsAI import WordsAI
import random

dictionary = (lambda filename: open(filename, 'r').read().split("\n"))('dictionary.txt')

def setup():
	wordsEnem = 0
	if str(input("Would you like to play against an AI? [Y/N]")) == 'Y':
		wordsEnem = WordsWithEnemies(AIPlayer(diff=int(input("What difficulty setting? [1 through 5]"))), HumanPlayer())
	elif str(input("Would you like to play against an AI? [Y/N]")) == 'A':
		wordsEnem = WordsWithEnemies(AIPlayer(diff=int(input("What difficulty setting? [1 through 5]"))), AIPlayer())
	else:
		wordsEnem = WordsWithEnemies(HumanPlayer(), HumanPlayer())		
	wordsEnem.eventLoop()

class WordsWithEnemies:
	
	def __init__(self, player1, player2, letterLen=8, winScore=5):
		self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
		self.letterLen = 8

		self.player2Score = 0
		self.player1Score = 0

		self.player1 = player1
		self.player2 = player2
		self.winScore = winScore

	def generateLetters(self):
		final = ''
		for i in range(self.letterLen):
			final += random.choice(self.alphabet)
		return final

	def wordTest(self, player1Word, player2Word):
		collisions = [letter for letter in set(player1Word + player2Word) if letter in player1Word and letter in player2Word]
		leftOverP1 = player1Word
		leftOverP2 = player2Word
		for collision in collisions:
			leftOverP1 = leftOverP1.replace(collision, "")
			leftOverP2 = leftOverP2.replace(collision, "")
		print("This was player1's word: " + player1Word)
		print("This was player2's word: " + player2Word)
		if len(leftOverP2) > len(leftOverP1):
			self.player2Score += 1
			return "Player2 won this round. Player2 score is " + str(self.player2Score) + ". Player1 is at " + str(self.player1Score) + "."
		if len(leftOverP2) < len(leftOverP1):
			self.player1Score += 1
			return "Player1 won this round. Player2 score is " + str(self.player2Score) + ". Player1 is at " + str(self.player1Score) + "."
		if len(leftOverP2) == len(leftOverP1):
			return "Tie. Player2 score is " + str(self.player2Score) + ". Player1 is at " + str(self.player1Score) + "."

	def eventLoop(self):
		while self.player1Score < self.winScore and self.player2Score < self.winScore:
			letters = self.generateLetters()
			self.player1.setLetters(letters)
			self.player2.setLetters(letters)
			print(self.wordTest(self.player1.chooseWord(), self.player2.chooseWord()))

		if self.player1Score >= self.winScore:
			print("Player1 won.")
		else:
			print("Player2 won.")



class Player:

	def __init__(self, diff=5):
		self.diff = diff
		pass

	def setLetters(self):
		pass

	def chooseWord(self):
		pass

	def validateWord(self):
		pass

class AIPlayer(Player):

	def setLetters(self, letters):
		self.ai = WordsAI('dictionary.txt', letters, self.diff)
		
	def chooseWord(self):
		return self.ai.execute()

class HumanPlayer(Player):

	def setLetters(self, letters):
		self.letters = letters

	def letterString(self):
		return " ".join(self.letters.upper().split())

	def validateWord(self, word):
		return all([letter in self.letters  for letter in word]) and word in dictionary

	def chooseWord(self):
		print("Here are your letters: " + self.letterString())
		while True:
			word = input("Enter your word: ")
			if self.validateWord(word):
				return word
			else:
				print("Use the fucking letters you dimwit. Try again.")









