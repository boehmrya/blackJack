# a simple black jack game

import random

# global variables
suits = ['spades', 'clubs', 'diamonds', 'hearts']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'jack', 'queen', 'king', 'ace']
scores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10']


class Card:
	def __init__(self, isuit, irank):
		self.suit = isuit
		self.rank = irank

	# to string method
	def __str__(self):
		name = self.suit + " " + self.rank
		return name

	# greater than or equal to
	def __ge__(self, other):
		thisRankIndex = ranks.index(self.rank)
		otherRankIndex = ranks.index(other.rank)
		if ( thisRankIndex > otherRankIndex ) :
			return True
		elif ( thisRankIndex < otherRankIndex ):
			return False
		else:
			thisSuitIndex = suits.index(self.suit)
			otherSuitIndex = suits.index(other.suit)
			if ( thisSuitIndex > otherSuitIndex ) :
				return True
			elif ( thisSuitIndex < otherSuitIndex ):
				return False
			else:
				return True

	# greater than
	def __gt__(self, other):
		thisRankIndex = ranks.index(self.rank)
		otherRankIndex = ranks.index(other.rank)
		if ( thisRankIndex > otherRankIndex ) :
			return True
		elif ( thisRankIndex < otherRankIndex ):
			return False
		else:
			thisSuitIndex = suits.index(self.suit)
			otherSuitIndex = suits.index(other.suit)
			if ( thisSuitIndex > otherSuitIndex ) :
				return True
			elif ( thisSuitIndex < otherSuitIndex ):
				return False
			else:
				return False

	# less than or equal to
	def __le__(self, other):
		thisRankIndex = ranks.index(self.rank)
		otherRankIndex = ranks.index(other.rank)
		if ( thisRankIndex < otherRankIndex ) :
			return True
		elif ( thisRankIndex > otherRankIndex ):
			return False
		else:
			thisSuitIndex = suits.index(self.suit)
			otherSuitIndex = suits.index(other.suit)
			if ( thisSuitIndex < otherSuitIndex ) :
				return True
			elif ( thisSuitIndex > otherSuitIndex ):
				return False
			else:
				return True

	# less than
	def __lt__(self, other):
		thisRankIndex = ranks.index(self.rank)
		otherRankIndex = ranks.index(other.rank)
		if ( thisRankIndex < otherRankIndex ) :
			return True
		elif ( thisRankIndex > otherRankIndex ):
			return False
		else:
			thisSuitIndex = suits.index(self.suit)
			otherSuitIndex = suits.index(other.suit)
			if ( thisSuitIndex < otherSuitIndex ) :
				return True
			elif ( thisSuitIndex > otherSuitIndex ):
				return False
			else:
				return False

	# equal to
	def __eq__(self, other):
		thisRankIndex = ranks.index(self.rank)
		otherRankIndex = ranks.index(other.rank)
		thisSuitIndex = suits.index(self.suit)
		otherSuitIndex = suits.index(other.suit)
		if (( thisRankIndex == otherRankIndex ) and ( thisSuitIndex == otherSuitIndex )):
			return True
		else:
			return False

	# not equal to
	def __ne__(self, other):
		thisRankIndex = ranks.index(self.rank)
		otherRankIndex = ranks.index(other.rank)
		thisSuitIndex = suits.index(self.suit)
		otherSuitIndex = suits.index(other.suit)
		if (( thisRankIndex != otherRankIndex ) or ( thisSuitIndex != otherSuitIndex )):
			return True
		else:
			return False


class Deck:
	def __init__(self):
		self.cards = []
		# add all cards in array in order
		for suit in suits:
			for rank in ranks:
				card = Card(suit, rank)
				self.cards.append(card)

	# randomly re-order the cards in the deck
	def shuffle(self):
		random.shuffle(self.cards)

	# randomly draw one card
	def draw(self):
		index = random.randint(0, 51)
		card = self.cards[index]
		return card


def blackJack():
	# initialize the deck of cards
	gameDeck = Deck()
	gameDeck.shuffle()

	# draw first card
	card1 = gameDeck.draw()
	print("first card is: " + str(card1))
	move = input("Stand or Hit? Enter h or s: ")

	# player move
	if move == 's':
		print("game over")
	elif move == 'h':
		card2 = gameDeck.draw()
		print("second card is: " + str(card2))
		index1 = ranks.index(card1.rank)
		index2 = ranks.index(card2.rank)
		score1 = int(scores[index1])
		score2 = int(scores[index2])
		totalScore = score1 + score2
		print("total score equals: " + str(totalScore))
	else:
		print("sorry.  you didn't enter h or s")

# play game
blackJack()














