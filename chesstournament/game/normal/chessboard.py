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
        if (x, y) in self.movimentation_possibilities(piece):
            field.piece = piece
            piece.x = x
            piece.y = y
            self.turn = "white" if self.turn == "black" else "black"
            return True

    def can_move(self, piece):
        return self.movimentation_possibilities(piece) != []

    def validation_field(self, x, y):
        if (x >= 0 and x < self.width) and (y >= 0 and y < self.height):
            return True
        return False

    def movimentation_validation(self, piece, x, y):
        if self.validation_field(x, y) is True and self.board[x][y].piece == None:
            return True
        elif self.validation_field(x ,y) is True and self.board[x][y].piece != None:
            if self.board[x][y].piece.color != piece.color:
                return True
        return False

    def movimentation_possibilities(self, piece):
        if type(piece) is Pawn:
            return self._pawn_movimentation(piece)
        elif type(piece) is Horse:
            return self._horse_movimentation(piece)
        elif type(piece) is Rook:
            return self._rook_movimentation(piece)
        elif type(piece) is Bishop:
            return self._bishop_movimentation(piece)
        elif type(piece) is Queen:
            return self._queen_movimentation(piece)

    def _pawn_movimentation(self, piece):
        possibilities = []
        x = piece.x
        y = piece.y
        if piece.color == "black":
            position = (x, y + 1)
            if self.movimentation_validation(piece ,position[0], position[1]) is True and self.board[position[0]][position[1]].piece == None:
                possibilities.append(position)
            position = (x, y + 2)
            if self.movimentation_validation(piece, position[0], position[1]) is True and piece.first_motion == True and self.board[position[0]][position[1]].piece == None and self.board[position[0] - 1][position[1]].piece == None :
                possibilities.append(position)
            position = (x + 1, y + 1)
            if self.movimentation_validation(piece, position[0], position[1]) is True and self.board[position[0]][position[1]].piece != None:
                if self.board[position[0]][position[1]].piece.color == "white":
                    possibilities.append(position)
            position = (x - 1, y + 1)
            if self.movimentation_validation(piece ,position[0] ,position[1]) is True and self.board[position[0]][position[1]].piece != None:
                if self.board[position[0]][position[1]].piece.color == "white":
                    possibilities.append(position)
            return possibilities
        else:
            position = (x, y - 1)
            if self.movimentation_validation(piece ,position[0], position[1]) is True and self.board[position[0]][position[1]].piece == None:
                possibilities.append(position)
            position = (x, y - 2)
            if self.movimentation_validation(piece, position[0], position[1]) is True and piece.first_motion == True and self.board[position[0]][position[1]].piece == None and self.board[position[0] - 1][position[1]].piece == None :
                possibilities.append(position)
            position = (x - 1, y - 1)
            if self.movimentation_validation(piece, position[0], position[1]) is True and self.board[position[0]][position[1]].piece != None:
                if self.board[position[0]][position[1]].piece.color == "black":
                    possibilities.append(position)
            position = (x + 1, y - 1)
            if self.movimentation_validation(piece ,position[0] ,position[1]) is True and self.board[position[0]][position[1]].piece != None:
                if self.board[position[0]][position[1]].piece.color == "black":
                    possibilities.append(position)
            return possibilities

    def _horse_movimentation(self, piece):
        possibilities = [(piece.x + x, piece.y + 3 - abs(x)) for x in range(-2, 3) if x != 0]
        possibilities.extend([(piece.x + x, piece.y - 3 + abs(x)) for x in range(-2, 3) if x != 0])
        possibilities = filter(lambda (x, y): x >= 0 and x <= 7 and y >= 0 and y <= 7, possibilities)
        return filter(lambda (x, y): getattr(self.get_field(x, y).piece, "color", None) != piece.color, possibilities)

    def _rook_movimentation(self,  piece, possibilities = []):
        _x, _y = piece.x, piece.y + 1
        while _y < self.height and self.board[_x][_y].piece == None:
            possibilities.append((_x, _y))
            _y += 1
        if _y < self.height and self.board[_x][_y].piece.color != piece.color:
            possibilities.append((_x, _y))
        _x, _y = piece.x, piece.y - 1
        while _y >= 0 and self.board[_x][_y].piece == None:
            possibilities.append((_x, _y))
            _y -= 1
        if _y >= 0 and self.board[_x][_y].piece.color != piece.color:
            possibilities.append((_x, _y))
        _x, _y = piece.x + 1, piece.y
        while _x < self.width and self.board[_x][_y].piece == None:
            possibilities.append((_x, _y))
            _x += 1
        if _x < self.width and self.board[_x][_y].piece.color != piece.color:
            possibilities.append((_x, _y))        
        _x, _y = piece.x - 1, piece.y
        while _x >= 0 and self.board[_x][_y].piece == None:
            possibilities.append((_x, _y))
            _x -= 1
        if _x >= 0 and self.board[_x][_y].piece.color != piece.color:
            possibilities.append((_x, _y))
        return possibilities

    def _bishop_movimentation(self, piece):
        possibilities = []
        _x, _y = piece.x + 1, piece.y + 1
        while (_y < self.height and _x < self.width) and self.board[_x][_y].piece == None:
            possibilities.append((_x, _y))
            _x += 1; _y += 1
        if (_y < self.height and _x < self.width) and self.board[_x][_y].piece.color != piece.color:
            possibilities.append((_x, _y))
        _x, _y = piece.x - 1, piece.y - 1
        while (_y >= 0 and _x >= 0) and self.board[_x][_y].piece == None:
            possibilities.append((_x, _y))
            _y -= 1; _x -= 1
        if (_y >= 0 and _x >= 0) and self.board[_x][_y].piece.color != piece.color:
            possibilities.append((_x, _y))
        _x, _y = piece.x + 1, piece.y - 1
        while (_x < self.width and _y >=0) and self.board[_x][_y].piece == None:
            possibilities.append((_x, _y))
            _x += 1; _y -= 1
        if (_x < self.width and _y >=0) and self.board[_x][_y].piece.color != piece.color:
            possibilities.append((_x, _y))        
        _x, _y = piece.x - 1, piece.y + 1
        while (_x >= 0 and _y < self.height) and self.board[_x][_y].piece == None:
            possibilities.append((_x, _y))
            _x -= 1; _y += 1
        if (_x >= 0 and _y < self.height) and self.board[_x][_y].piece.color != piece.color:
            possibilities.append((_x, _y))
        return possibilities

    def _queen_movimentation(self, piece):
        return self._rook_movimentation(piece, self._bishop_movimentation(piece))
