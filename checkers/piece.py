# from checkers.board import Board
from graphics import *
import math


class Piece(object):
    radius = 0.4
    centerPadding = 0.5

    def __init__(self, col, row, color, board):
        self.col = col
        self.row = row
        self.color = color
        self.board = board

        # Calculate the location
        self.center = Point(col + Piece.centerPadding, row + Piece.centerPadding)
        self.shape = Circle(self.center, Piece.radius)

        self.allowedMoves = []

        # Selection properties
        self.isSelected = False
        self.selectedBorder = None

        # Possible moves for this piece in a given position
        self.possibleMoves = []
        self.value = None  # Set by the instance

        # Add reference to the tile parent
        self.parentTile = None

    def getAllowedMoves(self):
        return

    def drawPiece(self, board):
        self.shape.draw(board)
        self.shape.setFill(self.color)

    # Returns true if a given point is part of the shape
    def isPointInShape(self, point):
        px = point.getX()
        py = point.getY()
        cx = self.center.getX()
        cy = self.center.getY()
        # Calculate the parameters for the hypot function
        # and calculate the distance from the origin
        parendicular = abs(cy - py)
        base = abs(cx - px)
        distance = Piece.radius - math.hypot(parendicular, base)

        return distance > 0

    def movePiece(self, row, col):
        mRow = row - self.row
        mCol = col - self.col
        self.row = mRow + self.row
        self.col = mCol + self.col
        self.shape.move(mCol, mRow)

    def toggleSelected(self, board):
        if not self.isSelected:
            center = self.shape.getCenter()
            self.selectedBorder = Circle(center, Piece.radius)
            self.selectedBorder.setOutline('yellow')
            self.selectedBorder.setWidth(5)
            self.selectedBorder.draw(board)
            self.isSelected = True
        else:
            self.selectedBorder.undraw()
            self.isSelected = False

    # def capture(self):
    #     if self.color == 'White':
    #         Board.whitePiecesCount -= 1
    #     else:
    #         Board.blackPiecesCount -= 1



class Pawn(Piece):
    def __init__(self, col, row, color, board):
        super(Pawn, self).__init__(col, row, color, board)
        self.getMovingDirection()

    def movePiece(self, row, col):
        mRow = row - self.row
        mCol = col - self.col
        self.row = mRow + self.row
        self.col = mCol + self.col
        self.shape.move(mCol, mRow)

    def getPossibleMoveAllowed(self, board):
        adjacentTiles = board.getAdjacentPlayableTiles(self.row, self.col)

    def getMovingDirection(self):
        if self.color == 'White':
            return 1
        else:
            return -1
