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
			if(line[0] != '#'):
				line = line.rstrip()
				line = line.split("|")
				square = Square(line[0],line[1])
				self.board.append(square)
		file.close()	
	def printBoard(self):
		for x in self.board:
			print(x.getName())
	def printCurrentSquareName(self):
		return str(self.board[self.currentSquare].getName())
	def getCurrentSquareType(self):
		return str(self.board[self.currentSquare].getType())
	def printCurrentSquareInfo(self):
		print("== Current Square ==")
		print("Name: " + str(self.printCurrentSquareName()))
		print("Type: " + str(self.getCurrentSquareType()))
	def updateCurrentSquare(self,roll):
		self.currentSquare = self.currentSquare + roll
		if (self.currentSquare >= len(self.board)):
			self.currentSquare = self.currentSquare - len(self.board)