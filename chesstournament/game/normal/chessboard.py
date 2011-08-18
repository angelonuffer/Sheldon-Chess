from chesstournament.piece import Pawn, Horse, King, Bishop, Queen, Rook


class Field(object):
   
    def __init__(self, color, x, y):
        self.color = None
        self.piece = None
        self.x = None
        self.y = None
    

class ChessBoard(object):
   
    def __init__(self):
        self.board = self.create_board()
        self.start_black_pieces()
        self.start_white_pieces()
        
    def create_board(self):
        board = []
        color ="black"
        for y in range(8):
            linha = []
            board.append(linha)
            for x in range(8):
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
        for x in range(8):
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
        for x in range(8):
            self.board[6][x].piece = Pawn("white", 6, x)                    
        
    
