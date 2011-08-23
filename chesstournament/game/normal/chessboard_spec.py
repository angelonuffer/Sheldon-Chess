import unittest
from should_dsl import should
from chessboard import ChessBoard
from chesstournament.piece import Rook, Pawn, Horse, Bishop


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

    def it_knows_the_panw_movimentation(self):
        board = ChessBoard()
        pawn = board.board[0][1].piece
        type(pawn) |should| be(Pawn)
        board.movimentation_possibilities(pawn) |should| equal_to([(0, 2), (0, 3)])
        board.board[1][2].piece = board.board[0][6].piece
        board.movimentation_possibilities(pawn) |should| equal_to([(0, 2), (0, 3), (1, 2)])
        
    def it_knows_the_horse_movimentation_for_initial_position(self):
        board = ChessBoard()
        horse = board.board[1][0].piece
        type(horse) |should| be(Horse)
        board.movimentation_possibilities(horse) |should| equal_to([(0, 2), (2, 2)])
        horse = board.board[6][0].piece
        type(horse) |should| be(Horse)
        board.movimentation_possibilities(horse) |should| equal_to([(5,2),(7,2)])

    def it_knows_the_horse_movimentation_out_initial_position(self):
        board = ChessBoard()
        board.board[4][4].piece = Horse('black  ', 4, 4)
        horse = board.board[4][4].piece
        type(horse) |should| be(Horse)
        possibilities = board.movimentation_possibilities(horse)
        possibilities.sort()
        possibilities |should| equal_to([(2, 3), (2, 5), (3, 2),(3, 6), (5, 2), (5, 6), (6, 3), (6, 5)])
        
    def it_knows_the_bishop_movimentation(self):
        board = ChessBoard()
        bishop = board.board[2][0].piece
        type(bishop) |should| be(Bishop)  
        board.movimentation_possibilities(bishop) |should| equal_to([])
        board.board[3][1].piece = None
        board.movimentation_possibilities(bishop) |should| equal_to([(3, 1), (4, 2), (5, 3), (6, 4), (7, 5)])

        
