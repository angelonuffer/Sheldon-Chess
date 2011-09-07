from sheldonchess.piece import Pawn, Horse, King, Bishop, Queen, Rook


class Field(object):

    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.piece = None


class ChessBoard(object):

    def __init__(self):
        self.width = 8
        self.height = 8
        self.board = self.create_board()
        self.start_black_pieces()
        self.start_white_pieces()
        self.turn = "white"

    def get_field(self, x, y):
        return self.board[x][y]

    def create_board(self):
        board = []
        for y in range(self.height):
            line = []
            board.append(line)
            for x in range(self.width):
                color = "black" if ((x - y) % 2) else "white"
                line.append(Field(color, x, y))
        return board

    def start_black_pieces(self):
        self.board[0][0].piece = Rook("black", 0, 0)
        self.board[1][0].piece = Horse("black", 1, 0)
        self.board[2][0].piece = Bishop("black", 2, 0)
        self.board[3][0].piece = Queen("black", 3, 0)
        self.board[4][0].piece = King("black", 4, 0)
        self.board[5][0].piece = Bishop("black", 5, 0)
        self.board[6][0].piece = Horse("black", 6, 0)
        self.board[7][0].piece = Rook("black", 7, 0)
        for x in range(self.width):
            self.board[x][1].piece = Pawn("black", x, 1)

    def start_white_pieces(self):
        self.board[0][7].piece = Rook("white", 0, 7)
        self.board[1][7].piece = Horse("white", 1, 7)
        self.board[2][7].piece = Bishop("white", 2, 7)
        self.board[3][7].piece = Queen("white", 3, 7)
        self.board[4][7].piece = King("white", 4, 7)
        self.board[5][7].piece = Bishop("white", 5, 7)
        self.board[6][7].piece = Horse("white", 6, 7)
        self.board[7][7].piece = Rook("white", 7, 7)
        for x in range(self.width):
            self.board[x][6].piece = Pawn("white", x, 6)

    def get_piece(self, x, y):
        field = self.get_field(x, y)        
        if field.piece:
            if field.piece.color == self.turn and self.can_move(field.piece):
                piece = field.piece
                field.piece = None
                return piece

    def put_piece(self, piece, x, y):
        field = self.get_field(x, y)
        if (x, y) in piece.define_possibilities(self.board):
            field.piece = piece
            piece.x = x
            piece.y = y
            self.turn = "white" if self.turn == "black" else "black"
            return True

    def can_move(self, piece):
        return piece.define_possibilities(self.board) != []
    
    def get_all_pieces(self):
        pieces = []        
        for x in range(8):
            for y in range(8):
                if self.board[x][y].piece != None:
                    pieces.append(self.board[x][y].piece)     
        return pieces
    
    def get_pieces_from_other_turn(self):
        return filter(lambda piece: piece.color != self.turn, self.get_all_pieces())

    def get_all_possibilities_from_other_turn(self):
        all_possibilities = []
        [all_possibilities.extend(piece.define_possibilities(self.board)) for piece in self.get_pieces_from_other_turn()]
        return set(all_possibilities)
    
    def check_is_in_check(self):
        king = filter(lambda piece: type(piece) == King and piece.color == self.turn, self.get_all_pieces()).pop()
        return (king.x, king.y) in self.get_all_possibilities_from_other_turn()
