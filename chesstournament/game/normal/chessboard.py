from chesstournament.piece import Pawn, Horse, King, Bishop, Queen, Rook


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

    def get_field(self, x, y):
        return self.board[x][y]

    def create_board(self):
        board = []
        color ="black"
        for y in range(self.height):
            linha = []
            board.append(linha)
            color = "black" if color == "white" else "white"
            for x in range(self.width):
                color = "black" if color == "white" else "white"
                linha.append(Field(color, x, y))
        return board

    def start_black_pieces(self):
        self.board[0][0].piece = Rook("black", 0, 0)
        self.board[0][1].piece = Horse("black", 0, 1)
        self.board[0][2].piece = Bishop("black", 0, 2)
        self.board[0][3].piece = King("black", 0, 3)
        self.board[0][4].piece = Queen("black", 0, 4)
        self.board[0][5].piece = Bishop("black", 0, 5)
        self.board[0][6].piece = Horse("black", 0, 6)
        self.board[0][7].piece = Rook("black", 0, 7)
        for x in range(self.width):
            self.board[1][x].piece = Pawn("black", 1, x)

    def start_white_pieces(self):
        self.board[7][0].piece = Rook("white", 7, 0)
        self.board[7][1].piece = Horse("white", 7, 1)
        self.board[7][2].piece = Bishop("white", 7, 2)
        self.board[7][3].piece = Queen("white", 7, 3)
        self.board[7][4].piece = King("white", 7, 4)
        self.board[7][5].piece = Bishop("white", 7, 5)
        self.board[7][6].piece = Horse("white", 7, 6)
        self.board[7][7].piece = Rook("white", 7, 7)
        for x in range(self.width):
            self.board[6][x].piece = Pawn("white", 6, x)
