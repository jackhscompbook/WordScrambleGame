
import random
import os

class game():

	def __init__(self):
		self.wordBank= []
		with open('adjList.txt', 'r') as f:
			for i in f:
				self.wordBank.append(i[:-1])

	def getWord(self):
		self.word = random.choice(self.wordBank)


	def scrambleWord(self):

		self.wordSep = []
		for i in self.word:
			self.wordSep.append(i)

		random.shuffle(self.wordSep)
		self.scrambled = ''.join(self.wordSep)

	def clear(self):
		os.system('cls')


	def play(self):
		self.clear()
		print('\nWelcome to a_personlol\'s word scramble game')
		input('Press enter to begin...')
		self.clear()
		self.score = 0
		print(self.score)
		while True:

			self.getWord()
			self.scrambleWord()

			while True:
				choice = input(f'What is this word: {self.scrambled}\n>>> ').lower()

				if choice == self.word:
					self.clear()
					self.score += 1
					print(self.score)
					print('Good Job!')
					break
				elif choice == 'word':
					self.clear()
					print(self.score)
					print(self.word)
				else:
					self.clear()
					print(self.score)
					print('Wrong, sorry...')



game = game()
game.play()





