import os
import pygame

MAILRAYS = os.path.join(os.path.dirname(__file__), "fonts", "mailrays.ttf")
WATER_ON_THE_OIL = os.path.join(os.path.dirname(__file__), "fonts", "WaterontheOil.ttf")
BUTTON_NORMAL = os.path.join(os.path.dirname(__file__), "images", "button_normal.png")
BUTTON_MOUSE_OVER = os.path.join(os.path.dirname(__file__), "images", "button_mouse_over.png")


class Menu(object):

    FONT = pygame.font.Font(WATER_ON_THE_OIL, 50)

    def __init__(self, window, title, buttons):
        self.window = window
        self.title = title
        self.buttons = buttons
        self.title_surface = Menu.FONT.render(title, True, (255, 255, 255))
        self.surface = pygame.Surface(window.size)

    @property
    def frame(self):
        self.surface.fill((0, 0, 0))
        title_width, title_height = self.title_surface.get_size()
        position = self.window.width / 2 - title_width / 2, 100
        self.surface.blit(self.title_surface, position)
        for i, button in enumerate(self.buttons):
            x, y = self.window.center
            x = x - button.width / 2
            y = y - button.height / 2 + 50 * i
            rect = (x, y, button.width, button.height)
            if self.window.mouse_over(rect):
                if pygame.mouse.get_pressed()[0]:
                    button.action()
                self.surface.blit(button.mouse_over, rect)
            else:
                self.surface.blit(button.normal, rect)
        return self.surface


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


class MainMenu(Menu):

    def __init__(self, window):
        buttons = [
            Button("New Game", self.new_game),
            Button("Options", self.options),
            Button("Credits", self.credits),
            Button("Exit", self.exit),
        ]
        super(MainMenu, self).__init__(window, "Chess Tournament", buttons)

    def new_game(self):
        pass

    def options(self):
        pass

    def credits(self):
        pass

    def exit(self):
        self.window.running = False
