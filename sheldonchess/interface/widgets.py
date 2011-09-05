import pygame
from constants import (
    MAILRAYS,
    BUTTON_NORMAL,
    BUTTON_MOUSE_OVER,
    TEXTBOX_NORMAL,
    TEXTBOX_MOUSE_OVER,
    )
from sheldonchess.game.normal import ChessBoard
from pieces import Piece


class Widget(object):

    def handle_event(self, event):
        pass


class Button(Widget):

    FONT = pygame.font.Font(MAILRAYS, 20)

    def __init__(self, text, action):
        self.text = text
        self.action = action
        self.size = self.width, self.height = 200, 40
        self.text_surface = Button.FONT.render(text, True, (255, 255, 255))
        text_width, text_height = self.text_surface.get_size()
        position = self.width / 2 - text_width / 2, self.height / 2 - text_height / 2 + 5
        self.normal = pygame.image.load(BUTTON_NORMAL)
        self.normal.blit(self.text_surface, position)
        self.mouse_over = pygame.image.load(BUTTON_MOUSE_OVER)
        self.mouse_over.blit(self.text_surface, position)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.action()


class TextBox(Widget):

    FONT = pygame.font.Font(MAILRAYS, 20)

    def __init__(self, text):
        self.text = text
        self.size = self.width, self.height = 200, 40
        self.update_text()

    def update_text(self):
        self.normal = pygame.image.load(TEXTBOX_NORMAL)
        self.mouse_over = pygame.image.load(TEXTBOX_MOUSE_OVER)
        text_surface = Button.FONT.render(self.text, True, (0, 0, 0))
        text_width, text_height = text_surface.get_size()
        position = self.width / 2 - text_width / 2, self.height / 2 - text_height / 2 + 5
        self.normal.blit(text_surface, position)
        self.mouse_over.blit(text_surface, position)


class Board(Widget):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.screen = None
        self.core = ChessBoard()
        white_field = pygame.Surface((width / self.core.width, height / self.core.height))
        white_field.fill((255, 255, 255))
        self.possibilities_image = white_field.copy()
        self.possibilities_image.fill((0, 255, 0))
        self.possibilities_image.set_alpha(80)
        self.pieces = {}
        self.selected_piece = None
        self.image = pygame.Surface((width, height))
        for x in range(self.core.width):
            for y in range(self.core.height):
                field = self.core.get_field(x, y)
                if field.color == "white":
                    self.image.blit(white_field, (x * width / self.core.width, y * height / self.core.height))
                if field.piece:
                    name = "_".join([field.piece.__class__.__name__.lower(), field.piece.color])
                    self.pieces[name] = Piece(field.piece)
        self.normal = self.image.copy()
        self.update_pieces()

    def start(self, screen):
        self.screen = screen
        self.handle_event = self._handle_event

    def _handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                field_width = self.width / self.core.width
                field_height = self.height / self.core.height
                x, y = event.pos
                x = (x - self.x + self.width / 2) / field_width
                y = (y - self.y + self.height / 2) / field_height
                if self.selected_piece:
                    self.put_piece(x, y)
                else:
                    self.get_piece(x, y, field_width, field_height)

    def get_piece(self, x, y, width, height):
        core_piece = self.core.get_piece(x, y)
        if core_piece:
            name = "_".join([core_piece.__class__.__name__.lower(), core_piece.color])
            piece = self.pieces[name]
            piece.core.x = x
            piece.core.y = y
            self.selected_piece = piece
            self.screen.window.cursor_image = piece.get_image(width, height)
            self.update_pieces()

    def put_piece(self, x, y):
        if self.core.put_piece(self.selected_piece.core, x, y):
            self.selected_piece = None
            self.screen.window.cursor_image = None
            self.update_pieces()

    def update_pieces(self):
        field_width = self.width / self.core.width
        field_height = self.height / self.core.height
        self.normal = self.image.copy()
        self.put_possibles()
        for field_x in range(self.core.width):
            for field_y in range(self.core.height):
                field = self.core.get_field(field_x, field_y)
                x = field_x * field_width
                y = field_y * field_height
                if field.piece:
                    name = "_".join([field.piece.__class__.__name__.lower(), field.piece.color])
                    piece = self.pieces[name]
                    self.normal.blit(piece.get_image(field_width, field_height), (x, y))
        self.mouse_over = self.normal.copy()

    def put_possibles(self):
        if self.selected_piece:
            field_width = self.width / self.core.width
            field_height = self.height / self.core.height
            for x, y in self.selected_piece.core.define_possibilities(self.core.board):
                self.normal.blit(self.possibilities_image, (x * self.width / self.core.width, y * self.height / self.core.height))
