### A checkers board
from graphics import *
from piece import *
from move import *


class Board:
    width = 600
    height = 600
    exit = False
    # Count the number of clicks the player clicked. On the second click the player
    # shall select a target tile to move to.
    clickCount = 0

    blackPiecesCount = 12
    whitePiecesCount = 12

    def __init__(self, boardDim):
        # Paint the window and set the background
        self.win = GraphWin('Checkers', Board.width, Board.height)  # draws screen
        self.win.setBackground('White')
        self.win.setCoords(-1, -3, 11, 9)

        #
        self.BoardDimension = 8

        # Paint the tiles of the board
        self.tiles = [[Tile(self.win, col, row) for row in range(self.BoardDimension)]
                      for col in range(self.BoardDimension)]

        # Save the initial starting tiles for the light and the dark pieces
        self.startLightPiecesTiles = \
            [tile for col in self.tiles for tile in col if (tile.color == 'Red' and tile.row < 3)]
        self.startDarkPiecesTiles = \
            [tile for col in self.tiles for tile in col if (tile.color == 'Red' and tile.row > 4)]

        self.clickPoint = None
        #  Setup the pieces

        self.setupStandardBoard()

        self.sourceTile = None  # the tile that is marked by the player as the source t
        self.destinationTile = None  # the tile that is mark by the player as the destination
        self.selectedPiece = None  # the piece that is currently marked for move
        self.isBlackTurn = False  # The white always starts the game

    def selectSourceTile(self):
        mouseClick = self.win.getMouse()
        tile = self.selectTile(mouseClick)  # type: object
        if tile.piece is not None:
            self.selectedPiece = tile.piece
            tile.piece.toggleSelected(self.win)
            self.sourceTile = tile
        return tile

    def selectTargetTile(self):
        mouseClick = self.win.getMouse()
        tile = self.selectTile(mouseClick)
        return tile

    def selectTile(self, mouseClick):
        px, py = mouseClick.getX(), mouseClick.getY()
        col, row = int(px), int(py)
        # Select the tile
        return self.getTileByRowCol(row, col)

    def toggleTurn(self):
        if self.isBlackTurn:
            self.isBlackTurn = False
        else:
            self.isBlackTurn = True

    def selectPieceToPlay(self, mouseClick):
        if Board.sourceTile is not None:
            Board.sourceTile.piece.toggleSelected(self.win)

        px, py = mouseClick.getX(), mouseClick.getY()
        col, row = int(px), int(py)
        # Select the tile
        selected = [tile for columns in self.tiles
                    for tile in columns if (tile.row == row and tile.col == col)][0]  # type: Tile
        if selected.piece is not None:
            Board.sourceTile = selected
        return Move(selected.piece, selected, None)

    def setupStandardBoard(self):
        # Setup white pieces
        for lt in self.startLightPiecesTiles:
            lt.piece = Pawn(lt.col, lt.row, 'White', self)
            lt.piece.drawPiece(self.win)
            lt.piece.parentTile = self
        for dt in self.startDarkPiecesTiles:
            dt.piece = Pawn(dt.col, dt.row, 'Black', self)
            dt.piece.drawPiece(self.win)
            dt.piece.paren0t0Tile = self

    # Returns the tiles that are adjacent to this tile.
    def getAdjacentPlayableTiles(self, row, col, rowDirection):
        row += rowDirection
        tiles = [self.getTileByRowCol(row, col - 1),
                 self.getTileByRowCol(row, col + 1)]
        return tiles

    def getTileByRowCol(self, row, col):
        return [tile for columns in self.tiles
                for tile in columns if (tile.row == row and tile.col == col)][0]  # type: Tile

    @staticmethod
    def inRect(rectangleOrigin, point, width, height):
        ox, oy = rectangleOrigin.getX(), rectangleOrigin.getY()
        px, py = point.getY(), point.getY()
        return (ox < px < ox + width) and (oy < py < oy + height)


class Tile:
    width = 1
    height = 1

    # X and Y are the indices of the tile
    def __init__(self, win, X, Y):
        self.win = win
        # The location of the tile
        self.col = X
        self.row = Y
        self.color = self.SetTileColor(X, Y)
        self.PaintTile(X, Y)
        self.isLightInit = True
        self.piece = None
        # Selection properties
        self.isSelected = False
        self.selectedHighlight = None

    def PaintTile(self, X, Y):
        rect = Rectangle(Point(X, Y), Point(X + Tile.width, Y + Tile.height))
        rect.setFill(self.color)
        rect.draw(self.win)

    @staticmethod
    def SetTileColor(x, y):
        if (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1):
            # sets every other square to red
            return 'Red'
        else:
            # every non red square to white
            return 'White'

    # Check if the given point is included in the tile
    # based on the row and column of the tile
    def isPointInTile(self, point):
        px = point.getX()
        py = point.getY()
        return ((self.row < px < self.row + Tile.width)
                and (self.col < py < self.col + Tile.height))

    def toggleSelected(self, board):
        if not self.isSelected:
            # Draw a circle to mark a target
            cx, cy = self.col + 0.5 * Tile.width, self.row + 0.5 * Tile.height
            center = Point(cx, cy)
            radius = Tile.width * 0.05
            self.selectedHighlight = Circle(center, radius)
            self.selectedHighlight.setFill('white')
            self.selectedHighlight.draw(board)
