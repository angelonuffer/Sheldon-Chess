import os
import pygame

MAILRAYS = os.path.join(os.path.dirname(__file__), "fonts", "mailrays.ttf")
BUTTON_NORMAL = os.path.join(os.path.dirname(__file__), "images", "button_normal.png")
BUTTON_MOUSE_OVER = os.path.join(os.path.dirname(__file__), "images", "button_mouse_over.png")


class Menu(object):

    def __init__(self, window, buttons):
        self.window = window
        self.buttons = buttons
        self.surface = pygame.Surface(window.size)

    @property
    def frame(self):
        self.surface.fill((0, 0, 0))
        for i, button in enumerate(self.buttons):
            x, y = self.window.center
            x = x - button.width / 2
            y = y - button.height / 2 + 50 * i
            rect = (x, y, button.width, button.height)
            if self.window.mouse_over(rect):
                self.surface.blit(button.mouse_over, rect)
            else:
                self.surface.blit(button.normal, rect)
        return self.surface


class Button(object):

    FONT = pygame.font.Font(MAILRAYS, 20)

    def __init__(self, text):
        self.text = text
        self.size = self.width, self.height = 200, 40
        self.text_surface = Button.FONT.render(text, True, (255, 255, 255))
        text_width, text_height = self.text_surface.get_size()
        position = self.width / 2 - text_width / 2, self.height / 2 - text_height / 2 + 5
        self.normal = pygame.image.load(BUTTON_NORMAL)
        self.normal.blit(self.text_surface, position)
        self.mouse_over = pygame.image.load(BUTTON_MOUSE_OVER)
        self.mouse_over.blit(self.text_surface, position)


class MainMenu(Menu):

    def __init__(self, window):
        buttons = map(Button, ["New Game", "Options", "Credits", "Exit"])
        super(MainMenu, self).__init__(window, buttons)
