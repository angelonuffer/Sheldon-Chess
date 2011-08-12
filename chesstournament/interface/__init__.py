import pygame
from menu import MainMenu


class Window(object):

    def __init__(self):
        self.screen = None
        self.size = self.width, self.height = 0, 0

    @property
    def center(self):
        return self.width / 2, self.height / 2

    def init(self, size=(800, 600)):
        self.size = self.width, self.height = size
        self.screen = pygame.display.set_mode(size)
        main_menu = MainMenu(self)
        self.running = True
        self.display(main_menu)
        pygame.display.quit()

    def display(self, screen):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill((0, 0, 0))
            self.screen.blit(screen.frame, (0, 0, self.width, self.height))
            pygame.display.flip()
