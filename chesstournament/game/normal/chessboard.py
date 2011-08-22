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
        self.turn = "white"
        

    def get_field(self, x, y):
        return self.board[y][x]

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
        self.board[0][1].piece = Horse("black", 1, 0)
        self.board[0][2].piece = Bishop("black", 2, 0)
        self.board[0][3].piece = Queen("black", 3, 0)
        self.board[0][4].piece = King("black", 4, 0)
        self.board[0][5].piece = Bishop("black", 5, 0)
        self.board[0][6].piece = Horse("black", 6, 0)
        self.board[0][7].piece = Rook("black", 7, 0)
        for x in range(self.width):
            self.board[1][x].piece = Pawn("black", x, 1)

    def start_white_pieces(self):
        self.board[7][0].piece = Rook("white", 0, 7)
        self.board[7][1].piece = Horse("white", 1, 7)
        self.board[7][2].piece = Bishop("white", 2, 7)
        self.board[7][3].piece = Queen("white", 3, 7)
        self.board[7][4].piece = King("white", 4, 7)
        self.board[7][5].piece = Bishop("white", 5, 7)
        self.board[7][6].piece = Horse("white", 6, 7)
        self.board[7][7].piece = Rook("white", 7, 7)
        for x in range(self.width):
            self.board[6][x].piece = Pawn("white", x, 6)

    def get_piece(self, x, y):
        field = self.get_field(x, y)
        if field.piece.color == self.turn:
            piece = field.piece
            field.piece = None
            return piece

    def put_piece(self, piece, x, y):
        field = self.get_field(x, y)
        field.piece = piece
        piece.x = x
        piece.y = y
        self.turn = "white" if self.turn == "black" else "black"
    
    def validation_field(self, y, x):
        if (x >= 0 and x <= self.width) and (y >= 0 and y <= self.height):
            return True
        return False 
   
    def movimentation_validation(self, piece, y, x):
        if self.validation_field(y, x) is True and self.board[y][x].piece == None:
            return True        
        elif self.validation_field(x ,y) is True and self.board[y][x].piece != None:
            if self.board[y][x].piece.color != piece.color:
                return True
        return False
                
    
    def movimentation_possibilities(self, piece):
        if type(piece) is Pawn:
            return self.pawn_movimentation(piece)
        elif type(piece) is Horse:
            return self.horse_movimentation(piece)    
            
    def pawn_movimentation(self, piece):
        possibilities = []
        x = piece.x
        y = piece.y
        if piece.color == "black":
            position = (y + 1, x)
            if self.movimentation_validation(piece ,position[0], position[1]) is True and self.board[position[0]][position[1]].piece == None:
                possibilities.append(position)
            position = (y + 2, x)
            if self.movimentation_validation(piece, position[0], position[1]) is True and piece.first_motion == True and self.board[position[0]][position[1]].piece == None and self.board[position[0] - 1][position[1]].piece == None :
                possibilities.append(position)
            position = (y + 1, x + 1)
            if self.movimentation_validation(piece, position[0], position[1]) is True and self.board[position[0]][position[1]].piece != None:
                if self.board[position[0]][position[1]].piece.color == "white":
                    possibilities.append(position)
            position = (y + 1, x - 1)
            if self.movimentation_validation(piece ,position[0] ,position[1]) is True and self.board[position[0]][position[1]].piece != None:
                if self.board[position[0]][position[1]].piece.color == "white":
                    possibilities.append(position)    
            return possibilities
        else:
            position = (y - 1, x)
            if self.movimentation_validation(piece ,position[0], position[1]) is True and self.board[position[0]][position[1]].piece == None:
                possibilities.append(position)
            position = (y - 2, x)
            if self.movimentation_validation(piece, position[0], position[1]) is True and piece.first_motion == True and self.board[position[0]][position[1]].piece == None and self.board[position[0] - 1][position[1]].piece == None :
                possibilities.append(position)
            position = (y - 1, x - 1)
            if self.movimentation_validation(piece, position[0], position[1]) is True and self.board[position[0]][position[1]].piece != None:
                if self.board[position[0]][position[1]].piece.color == "black":
                    possibilities.append(position)
            position = (y - 1, x + 1)
            if self.movimentation_validation(piece ,position[0] ,position[1]) is True and self.board[position[0]][position[1]].piece != None:
                if self.board[position[0]][position[1]].piece.color == "black":
                    possibilities.append(position)    
            return possibilities        
    
    def horse_movimentation(self, piece):
        possibilities = []
        x = piece.x
        y = piece.y
        position = (y + 2, x + 1)
        if self.movimentation_validation(piece ,position[0], position[1]) is True:
            possibilities.append(position)
        position = (y + 2, x - 1)
        if self.movimentation_validation(piece ,position[0], position[1]) is True:
            possibilities.append(position)
        position = (y - 2, x + 1)
        if self.movimentation_validation(piece ,position[0], position[1]) is True:
            possibilities.append(position)
        position = (y - 2, x - 1)
        if self.movimentation_validation(piece ,position[0], position[1]) is True:
            possibilities.append(position)
        position = (y + 1, x + 2)
        if self.movimentation_validation(piece ,position[0], position[1]) is True:
            possibilities.append(position)
        position = (y + 1, x - 2)
        if self.movimentation_validation(piece ,position[0], position[1]) is True:
            possibilities.append(position)
        position = (y - 1, x + 2)
        if self.movimentation_validation(piece ,position[0], position[1]) is True:
            possibilities.append(position)
        position = (y - 1, x - 2)
        if self.movimentation_validation(piece ,position[0], position[1]) is True:
            possibilities.append(position)
        return possibilities                 
        
        
        
        
        
