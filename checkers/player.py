# Players should have access to the board and to the pieces
import board
import piece
from move import *


class Player(object):
    def __init__(self, pieceCount, color, board):
        self.color = color
        self.kings = 0  # The number of kings the player has
        self.getCurrentValue()
        self.board = board

        self.currentMoves = []  # The move that the player is going to play

        self.activePieces = []
        self.getPlayerPieces()

    # Return the current value of the user based on the
    def getCurrentValue(self):
        return

    def play(self):
        pass

    def getPlayerPieces(self):
        if self.color == 'White':
            return self.board.startLightPiecesTiles
        if self.color == 'Black':
            return self.board.startDarkPiecesTiles


class AIPlayer(Player):
    def __init__(self, piecesCount, color, board):
        super(AIPlayer, self).__init__(piecesCount, color, board)
        self.moves = []

    def play(self, board):
        stam = ""

    def getMoves(self):
        # Get all the pieces that are able to move and that are still on the board
        playablePieces = [pc for pc in self.activePieces if(len(pc.moves) is not 0)]
        for piece in playablePieces:  # type: Piece
            self.currentMoves.append(piece.allowedMoves)


class HomanPlayer(Player):
    def __init__(self, piecesCount, color, board):
        super(HomanPlayer, self).__init__(piecesCount, color, board)

    def play(self, board):
        sourceTile = board.selectSourceTile()
        targetTile = board.selectTargetTile()
        move = Move(sourceTile, targetTile)
        move.playMove(board)
        board.toggleTurn()
