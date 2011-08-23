import os
import gettext
import pygame
pygame.font.init()
pygame.mixer.init()

from screens import MainMenu
from constants import LOCALE


class Window(object):

    def __init__(self, size=(800, 600)):
        self.size = self.width, self.height = size
        self.screen = None
        self.language = "en"
        self.focus = None
        self.cursor_image = None

    @property
    def center(self):
        return self.width / 2, self.height / 2

    def init(self):
        global _
        translation = gettext.translation("menu", LOCALE, languages=[self.language])
        translation.install()
        _ = translation.lgettext
        self.screen = pygame.display.set_mode(self.size)
        self.focus = None
        self.cursor_image = None
        main_menu = MainMenu(self)
        self.running = True
        self.display(main_menu)
        pygame.display.quit()

    def display(self, screen):
        while self.running and screen.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif self.focus:
                    self.focus.handle_event(event)
            self.screen.fill((0, 0, 0))
            self.screen.blit(screen.frame, (0, 0, self.width, self.height))
            if self.cursor_image:
                self.put_cursor()
            pygame.display.flip()

    def put_cursor(self):
        x, y = pygame.mouse.get_pos()
        width, height = self.cursor_image.get_size()
        x = x - width / 2
        y = y - height / 2
        self.screen.blit(self.cursor_image, (x, y))

    def mouse_over(self, rect):
        x, y, width, height = rect
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return mouse_x > x and mouse_x < x + width and mouse_y > y and mouse_y < y + height
