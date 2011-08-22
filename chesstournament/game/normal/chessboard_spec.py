import unittest
from should_dsl import should
from chessboard import ChessBoard
from chesstournament.piece import Rook, Pawn


class TestBoard(unittest.TestCase):

    def it_has_a_size(self):
        board = ChessBoard()
        board.width |should| equal_to(8)
        board.height |should| equal_to(8)

    def its_fields_have_colors(self):
        board = ChessBoard()
        corner0 = board.get_field(0, 0)
        corner0.color |should| equal_to("white")
        corner1 = board.get_field(0, 7)
        corner1.color |should| equal_to("black")
        corner2 = board.get_field(7, 0)
        corner2.color |should| equal_to("black")
        corner3 = board.get_field(7, 7)
        corner3.color |should| equal_to("white")

    def it_has_pieces(self):
        board = ChessBoard()
        corner0 = board.get_field(0, 0)
        type(corner0.piece) |should| be(Rook)
        corner0.piece.color |should| equal_to("black")
        field = board.get_field(4, 1)
        type(field.piece) |should| be(Pawn)
        field.piece.color |should| equal_to("black")
        field = board.get_field(3, 6)
        type(field.piece) |should| be(Pawn)
        field.piece.color |should| equal_to("white")

    def it_can_remove_a_piece(self):
        board = ChessBoard()
        field = board.get_field(4, 6)
        type(field.piece) |should| be(Pawn)
        white_pawn = board.get_piece(4, 6)
        field.piece |should| be(None)
        type(white_pawn) |should| be(Pawn)

    def it_only_remove_pieces_of_turn_player(self):
        board = ChessBoard()
        field1 = board.get_field(4, 1)
        type(field1.piece) |should| be(Pawn)
        board.get_piece(4, 1) |should| be(None)
        type(field1.piece) |should| be(Pawn)
        field2 = board.get_field(4, 6)
        type(field2.piece) |should| be(Pawn)
        white_pawn = board.get_piece(4, 6)
        field2.piece |should| be(None)
        type(white_pawn) |should| be(Pawn)

    def it_can_put_a_piece(self):
        board = ChessBoard()
        origin_field = board.get_field(2, 6)
        target_field = board.get_field(2, 4)
        board.turn |should| equal_to("white")
        type(origin_field.piece) |should| be(Pawn)
        target_field.piece |should| be(None)
        white_pawn = board.get_piece(2, 6)
        board.put_piece(white_pawn, 2, 4)
        board.turn |should| equal_to("black")
        origin_field.piece |should| be(None)
        type(target_field.piece) |should| be(Pawn)
    
    def it_can_get_panw_movimentation(self):
        board = ChessBoard()
        pawn = board.board[1][1].piece
        type(pawn) |should| be(Pawn)
        board.movimentation_possibilities(pawn) |should| equal_to([(2, 1), (3, 1)])
        board.board[2][0].piece = board.board[6][0].piece
        board.movimentation_possibilities(pawn) |should| equal_to([(2, 1), (3, 1), (2, 0)])
        

        
         
