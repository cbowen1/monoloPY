import util
from square import Square
import os
class GameBoard:
	board = []
	currentSquare = 0
	def __init__(self):
		self.generateBoard()
	def generateBoard(self):
		file = open("monoloPY/board.config","r") #opensFile
		for line in file:
			line = line.rstrip()
			square = Square(line)
			self.board.append(square)
		file.close()	
	def printBoard(self):
		for x in self.board:
			print(x.getName())
	def printCurrentSquareName(self):
		return str(self.board[self.currentSquare].getName())
	def updateCurrentSquare(self,roll):
		self.currentSquare = self.currentSquare + roll
		if (self.currentSquare >= len(self.board)):
			self.currentSquare = self.currentSquare - len(self.board)