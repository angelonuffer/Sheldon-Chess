import pygame
from widgets import Button, TextBox, Board
from constants import WATER_ON_THE_OIL, MAILRAYS, CRUNCH, CREDITS, CHESSSOUND_TITLE


class Screen(object):

    def __init__(self, window):
        self.window = window
        self.running = True

    def put_widget(self, widget):
        x = widget.x - widget.width / 2
        y = widget.y - widget.height / 2
        rect = (x, y, widget.width, widget.height)
        if self.window.mouse_over(rect):
            self.surface.blit(widget.mouse_over, rect)
            self.window.focus = widget
        else:
            self.surface.blit(widget.normal, rect)
            if self.window.focus is widget:
                self.window.focus = None


class Menu(Screen):

    FONT = pygame.font.Font(WATER_ON_THE_OIL, 50)

    def __init__(self, window, background_path, buttons):
        super(Menu, self).__init__(window)
        self.window = window
        self.buttons = []
        x, y = self.window.center
        y += 30
        for button_name, action in buttons:
            self.buttons.append(Button(x, y, button_name, action))
            y += 50
        self.background = pygame.image.load(background_path)
        self.background = pygame.transform.scale(self.background, window.size)
        self.surface = self.background.copy()

    @property
    def frame(self):
        self.surface = self.background.copy()
        for button in self.buttons:
            self.put_widget(button)
        return self.surface


class MainMenu(Menu):

    def __init__(self, window):
        buttons = [
            (_("new game"), self.new_game),
            (_("options"), self.options),
            (_("credits"), self.credits),
            (_("exit"), self.exit),
        ]
        super(MainMenu, self).__init__(window, CHESSSOUND_TITLE, buttons)
        pygame.mixer.music.load(CRUNCH)
        pygame.mixer.music.play()

    def new_game(self):
        lobby = NormalGameLobby(self.window)
        self.window.display(lobby)

    def options(self):
        options = OptionsMenu(self.window)
        self.window.display(options)

    def credits(self):
        credits = Credits(self.window)
        self.window.display(credits)

    def exit(self):
        self.window.running = False


class NormalGameLobby(Screen):

    def __init__(self, window):
        super(NormalGameLobby, self).__init__(window)
        self.surface = pygame.Surface(window.size)
        self.back_button = Button(120, self.window.center[1], _("back"), self.back)
        self.player_black = TextBox(self.window.center[0], 25, "Player 1")
        self.player_white = TextBox(self.window.center[0], 285, "Player 2")
        self.board = Board(self.window.center[0], 155, 200, 200)
        self.start_button = Button(self.window.width - 120, self.window.center[1], _("start"), self.start)

    @property
    def frame(self):
        self.surface.fill((100, 100, 255))
        self.put_widget(self.back_button)
        self.put_widget(self.player_black)
        self.put_widget(self.player_white)
        self.put_widget(self.board)
        self.put_widget(self.start_button)
        return self.surface

    def back(self):
        self.running = False

    def start(self):
        pygame.mixer.music.stop()
        normal_game = NormalGame(self.window)
        self.window.display(normal_game)


class NormalGame(Screen):

    def __init__(self, window):
        super(NormalGame, self).__init__(window)
        self.surface = pygame.Surface(window.size)
        x = self.window.width - self.window.height / 2 - 10
        y = self.window.center[1]
        self.board = Board(x, y, window.height - 20, window.height - 20)
        self.board.start(self)

    @property
    def frame(self):
        self.surface.fill((200, 255, 255))
        self.put_widget(self.board)
        return self.surface


class OptionsMenu(Menu):

    def __init__(self, window):
        buttons = [
            (_("audio"), self.audio),
            (_("video"), self.video),
            (_("language"), self.language),
            (_("back"), self.back),
        ]
        super(OptionsMenu, self).__init__(window, CHESSSOUND_TITLE, buttons)

    def audio(self):
        pass

    def video(self):
        pass

    def language(self):
        pass

    def back(self):
        self.running = False


class Credits(Screen):

    FONT = pygame.font.Font(MAILRAYS, 20)

    def __init__(self, window):
        super(Credits, self).__init__(window)
        self.surface = pygame.Surface(window.size)
        self.text_surface = pygame.Surface(window.size)
        for i, line in enumerate(CREDITS.split("\n")):
            line_surface = Credits.FONT.render(line, True, (255, 255, 255))
            self.text_surface.blit(line_surface, (50, i * 20))
        self.back_button = Button(self.window.width / 2, self.window.height - 100, _("back"), self.back)

    @property
    def frame(self):
        self.surface.fill((0, 0, 0))
        self.surface.blit(self.text_surface, (0, 0))
        self.put_widget(self.back_button)
        return self.surface

    def back(self):
        self.running = False
