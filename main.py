from checkers.board import Board
from checkers.player import *

# Constant
BOARD_DIMENSIONS = 8
NUM_OF_PIECES = 12
TILE_WIDTH = 1
TILE_HEIGHT = 1

# Initiate game variables and objects
gameOver = False
isBlackTurn = False
board = Board(8)
aiPlayer = AIPlayer(NUM_OF_PIECES, 'Black', board)
human = HomanPlayer(NUM_OF_PIECES, 'White', board)

while not gameOver:
    # White (human) starts
    board.win.getMouse() # just to keep the window open
    human.play(board)
    aiPlayer.play(board)