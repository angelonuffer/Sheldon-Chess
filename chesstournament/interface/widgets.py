import pygame
from constants import (
    MAILRAYS,
    BUTTON_NORMAL,
    BUTTON_MOUSE_OVER,
    TEXTBOX_NORMAL,
    TEXTBOX_MOUSE_OVER,
    )


class Button(object):

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


class TextBox(object):

    FONT = pygame.font.Font(MAILRAYS, 20)

    def __init__(self, text):
        self.text = text
        self.size = self.width, self.height = 200, 40
        self.update_text()

    def action(self):
        pass

    def update_text(self):
        self.normal = pygame.image.load(TEXTBOX_NORMAL)
        self.mouse_over = pygame.image.load(TEXTBOX_MOUSE_OVER)
        text_surface = Button.FONT.render(self.text, True, (0, 0, 0))
        text_width, text_height = text_surface.get_size()
        position = self.width / 2 - text_width / 2, self.height / 2 - text_height / 2 + 5
        self.normal.blit(text_surface, position)
        self.mouse_over.blit(text_surface, position)
