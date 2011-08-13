import os
import pygame


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

    def __init__(self, text):
        self.text = text
        self.size = self.width, self.height = 200, 40
        normal_path = os.path.join(os.path.dirname(__file__), "images", "button_normal.png")
        self.normal = pygame.image.load(normal_path)
        mouse_over_path = os.path.join(os.path.dirname(__file__), "images", "button_mouse_over.png")
        self.mouse_over = pygame.image.load(mouse_over_path)


class MainMenu(Menu):

    def __init__(self, window):
        buttons = map(Button, ["New Game", "Options", "Credits", "Exit"])
        super(MainMenu, self).__init__(window, buttons)
