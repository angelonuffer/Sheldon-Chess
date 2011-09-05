import pygame
from sheldonchess.piece import Pawn, Rook, Bishop, Horse, Queen, King
from constants import PIECES

def get_piece_surface(x, y):
    image = pygame.image.load(PIECES)
    return image.subsurface((x * 63, y * 72, 63, 72))


class Piece(object):

    WHITE_PAWN = get_piece_surface(5, 2)
    WHITE_ROOK = get_piece_surface(2, 2)
    WHITE_BISHOP = get_piece_surface(3, 2)
    WHITE_HORSE = get_piece_surface(4, 2)
    WHITE_QUEEN = get_piece_surface(1, 2)
    WHITE_KING = get_piece_surface(0, 2)
    BLACK_PAWN = get_piece_surface(5, 3)
    BLACK_ROOK = get_piece_surface(2, 3)
    BLACK_BISHOP = get_piece_surface(3, 3)
    BLACK_HORSE = get_piece_surface(4, 3)
    BLACK_QUEEN = get_piece_surface(1, 3)
    BLACK_KING = get_piece_surface(0, 3)

    def __init__(self, core):
        self.core = core
        if type(self.core) is Pawn:
            if self.core.color == "white":
                self.image = Piece.WHITE_PAWN.copy()
            if self.core.color == "black":
                self.image = Piece.BLACK_PAWN.copy()
        if type(self.core) is Rook:
            if self.core.color == "white":
                self.image = Piece.WHITE_ROOK.copy()
            if self.core.color == "black":
                self.image = Piece.BLACK_ROOK.copy()
        if type(self.core) is Bishop:
            if self.core.color == "white":
                self.image = Piece.WHITE_BISHOP.copy()
            if self.core.color == "black":
                self.image = Piece.BLACK_BISHOP.copy()
        if type(self.core) is Horse:
            if self.core.color == "white":
                self.image = Piece.WHITE_HORSE.copy()
            if self.core.color == "black":
                self.image = Piece.BLACK_HORSE.copy()
        if type(self.core) is Queen:
            if self.core.color == "white":
                self.image = Piece.WHITE_QUEEN.copy()
            if self.core.color == "black":
                self.image = Piece.BLACK_QUEEN.copy()
        if type(self.core) is King:
            if self.core.color == "white":
                self.image = Piece.WHITE_KING.copy()
            if self.core.color == "black":
                self.image = Piece.BLACK_KING.copy()

    def get_image(self, width, height):
        return pygame.transform.scale(self.image, (width, height))
