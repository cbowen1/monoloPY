import random
class Util:
	def rollDice(self):
		diceRoll = random.randint(1,6)
		print ("You rolled a " + str(diceRoll))
		return diceRoll

