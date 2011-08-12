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
            self.surface.blit(button.normal, (x, y, button.width, button.height))
        return self.surface


class Button(object):

    def __init__(self, text):
        self.text = text
        self.size = self.width, self.height = 200, 40
        self.surface = pygame.Surface(self.size)
        self.surface.fill((255, 255, 255))

    @property
    def normal(self):
        return self.surface



class MainMenu(Menu):

    def __init__(self, window):
        buttons = map(Button, ["New Game", "Options", "Credits", "Exit"])
        super(MainMenu, self).__init__(window, buttons)
