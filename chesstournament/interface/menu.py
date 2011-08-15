import pygame
from widgets import Button, TextBox
from constants import WATER_ON_THE_OIL


class Screen(object):

    def __init__(self, window):
        self.window = window
        self.running = True

    def put_widget(self, widget, center):
        x, y = center
        x = x - widget.width / 2
        y = y - widget.height / 2
        rect = (x, y, widget.width, widget.height)
        if self.window.mouse_over(rect):
            if pygame.mouse.get_pressed()[0]:
                widget.action()
            self.surface.blit(widget.mouse_over, rect)
        else:
            self.surface.blit(widget.normal, rect)


class Menu(Screen):

    FONT = pygame.font.Font(WATER_ON_THE_OIL, 50)

    def __init__(self, window, title, buttons):
        super(Menu, self).__init__(window)
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
            y = y + 50 * i
            self.put_widget(button, (x, y))
        return self.surface


class MainMenu(Menu):

    def __init__(self, window):
        buttons = [
            Button(_("new game"), self.new_game),
            Button(_("options"), self.options),
            Button(_("credits"), self.credits),
            Button(_("exit"), self.exit),
        ]
        super(MainMenu, self).__init__(window, "Chess Tournament", buttons)

    def new_game(self):
        lobby = NormalGameLobby(self.window)
        self.window.display(lobby)

    def options(self):
        pass

    def credits(self):
        pass

    def exit(self):
        self.window.running = False


class NormalGameLobby(Screen):

    def __init__(self, window):
        super(NormalGameLobby, self).__init__(window)
        self.surface = pygame.Surface(window.size)
        self.back_button = Button(_("back"), self.back)
        self.player_black = TextBox("Player 1")
        self.player_white = TextBox("Player 2")
        self.start_button = Button(_("start"), self.start)

    @property
    def frame(self):
        self.surface.fill((100, 100, 255))
        self.put_widget(self.back_button, (120, self.window.center[1]))
        self.put_widget(self.player_black, (self.window.center[0], 50))
        self.put_widget(self.player_white, (self.window.center[0], 100))
        self.put_widget(self.start_button, (self.window.width - 120, self.window.center[1]))
        return self.surface

    def back(self):
        self.running = False

    def start(self):
        pass
