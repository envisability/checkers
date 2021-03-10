import board


class Move:
    moveNumber = 0

    def __init__(self, source=None, destination=None):
        # Setup the serial number for the move
        self.index = Move.moveNumber + 1
        Move.moveNumber = self.index

        self.source = source
        self.piece = source.piece

        self.destination = destination
        self.isLegalMove = False
        self.isAttackMove = False
        self.isWalkMove = False
        self.isDoubleAttackMove = False
        self.rank = None  # How good is this move

    def playMove(self, board):
        self.piece.toggleSelected(board)
        self.piece.movePiece(self.destination.row, self.destination.col)

    def getMoveType(self, board):
        pass

