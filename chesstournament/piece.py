class Piece(object):
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y


class Pawn(Piece):
    def define_possibilities(self, board):
        possibilities = []
        if self.color == "black":
            if board[self.x][self.y + 1].piece == None:
                possibilities = [(self.x, self.y + 1)]
                if self.y == 1:
                    possibilities.extend([(self.x, self.y + 2)] if board[self.x][self.y + 2].piece == None else [])
                possibilities.extend([(self.x + i, self.y + 1) for i in [-1, 1] if getattr(board[self.x + i][self.y + 1].piece, "color", self.color) != self.color])
        else:
            if board[self.x][self.y - 1].piece == None:
                possibilities = [(self.x, self.y - 1)]
                if self.y == 6:
                    possibilities.extend([(self.x, self.y - 2)] if board[self.x][self.y - 2].piece == None else [])
                possibilities.extend([(self.x + i, self.y - 1) for i in [-1, 1] if getattr(board[self.x + i][self.y - 1].piece, "color", self.color) != self.color])
        return possibilities    


class Rook(Piece):
    def define_possibilities(self, board):
        possibilities = possibilities or []
        _x, _y = self.x, self.y + 1
        while _y < 8 and board[_x][_y].piece == None:
            possibilities.append((_x, _y))
            _y += 1
        if _y < 8 and board[_x][_y].self.color != self.color:
            possibilities.append((_x, _y))
        _x, _y = self.x, self.y - 1
        while _y >= 0 and board[_x][_y].piece == None:
            possibilities.append((_x, _y))
            _y -= 1
        if _y >= 0 and board[_x][_y].self.color != self.color:
            possibilities.append((_x, _y))
        _x, _y = self.x + 1, self.y
        while _x < 8 and board[_x][_y].piece == None:
            possibilities.append((_x, _y))
            _x += 1
        if _x < 8 and board[_x][_y].self.color != self.color:
            possibilities.append((_x, _y))
        _x, _y = self.x - 1, self.y
        while _x >= 0 and board[_x][_y].piece == None:
            possibilities.append((_x, _y))
            _x -= 1
        if _x >= 0 and board[_x][_y].self.color != self.color:
            possibilities.append((_x, _y))
        return possibilities


class Bishop(Piece):
    def define_possibilities(self, board):
        possibilities = []
        _x, _y = self.x + 1, self.y + 1
        while (_y < 8 and _x < 8) and board[_x][_y].piece == None:
            possibilities.append((_x, _y))
            _x += 1; _y += 1
        if (_y < 8 and _x < 8) and board[_x][_y].self.color != self.color:
            possibilities.append((_x, _y))
        _x, _y = self.x - 1, self.y - 1
        while (_y >= 0 and _x >= 0) and board[_x][_y].piece == None:
            possibilities.append((_x, _y))
            _y -= 1; _x -= 1
        if (_y >= 0 and _x >= 0) and board[_x][_y].self.color != self.color:
            possibilities.append((_x, _y))
        _x, _y = self.x + 1, self.y - 1
        while (_x < 8 and _y >=0) and board[_x][_y].piece == None:
            possibilities.append((_x, _y))
            _x += 1; _y -= 1
        if (_x < 8 and _y >=0) and board[_x][_y].self.color != self.color:
            possibilities.append((_x, _y))
        _x, _y = self.x - 1, self.y + 1
        while (_x >= 0 and _y < 8) and board[_x][_y].piece == None:
            possibilities.append((_x, _y))
            _x -= 1; _y += 1
        if (_x >= 0 and _y < 8) and board[_x][_y].self.color != self.color:
            possibilities.append((_x, _y))
        return possibilities


class Horse(Piece):
    def define_possibilities(self, board):
        possibilities = [(self.x + x, self.y + 3 - abs(x)) for x in range(-2, 3) if x != 0]
        possibilities.extend([(self.x + x, self.y - 3 + abs(x)) for x in range(-2, 3) if x != 0])
        possibilities = filter(lambda (x, y): x >= 0 and x <= 7 and y >= 0 and y <= 7, possibilities)
        return filter(lambda (x, y): getattr(board[x][y].piece, "color", None) != self.color, possibilities)

class Queen(Piece):
    def define_possibilities(self, board):
        return self._rook_movimentation(piece, self._bishop_movimentation(piece))


class King(Piece):
    def define_possibilities(self, board):
        possibilities = [(self.x - 1 + (n / 3), self.y - 1 + (n % 3)) for n in range(9) if n != 4]
        possibilities = filter(lambda (x, y): x >= 0 and x <= 7 and y >= 0 and y <= 7, possibilities)
        return filter(lambda (x, y): getattr(board[x][y].piece, "color", None) != self.color, possibilities)
