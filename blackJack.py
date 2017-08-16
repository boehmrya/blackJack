# a simple black jack game to work on object oriented design


class Card:
	suits = ['spades', 'clubs', 'diamonds', 'hearts']
	ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'jack', 'queen', 'king', 'ace']

	def __init__(self, isuit, irank):
		self.suit = isuit
		self.rank = irank

	# to string method
	def __str__(self):
		name = suit + " " + rank
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
		if (( thisRankIndex == otherRankIndex ) && ( thisSuitIndex == otherSuitIndex )) :
			return True
		else:
			return False

	# not equal to
	def __ne__(self, other):
		thisRankIndex = ranks.index(self.rank)
		otherRankIndex = ranks.index(other.rank)
		thisSuitIndex = suits.index(self.suit)
		otherSuitIndex = suits.index(other.suit)
		if (( thisRankIndex != otherRankIndex ) || ( thisSuitIndex != otherSuitIndex )) :
			return True
		else:
			return False


class Deck:
	







