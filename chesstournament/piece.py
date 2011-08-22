class Piece(object):
    def __init__(self,color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.first_motion = True


class Pawn(Piece):
    pass


class Rook(Piece):
    pass


class Bishop(Piece):
    pass


class Horse(Piece):
    pass


class Queen(Piece):
    pass


class King(Piece):
    pass
