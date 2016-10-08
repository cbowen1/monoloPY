import util
from square import Square
import os
class GameBoard:
	board = []
	def __init__(self):
		self.generateBoard()
	def generateBoard(self):
		file = open("monoloPY/board.config","r") #opensFile
		for line in file:
			square = Square(line)
			self.board.append(square)