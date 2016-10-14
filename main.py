#####################
#
#
#
#####################
from util import Util
from gameBoard import GameBoard
def playGame(board,gameOver):
	print ("You are currently on " + board.printCurrentSquareName())
	while(gameOver == False):
		diceRoll = util.rollDice()
		board.updateCurrentSquare(diceRoll)
		print ("You are currently on " + board.printCurrentSquareName())
		input("Press enter to continue...")

util = Util()
print("Welcome to monoloPY")
board = GameBoard()
gameOver = False
playGame(board,gameOver)