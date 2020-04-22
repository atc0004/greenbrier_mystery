import pygame

class UI:
    def __init__(self, screen, debug=False):
        self.screen = screen
        self.debug = debug
        self.black = (0, 0, 0, 100)
        self.surface = pygame.Surface((100, 1200), pygame.SRCALPHA)
        self.rect = pygame.Rect((0,0),(100,1200))
    def update(self):
        pygame.display.update()

    def render(self):
        # Put transparent rectangle at side of screen,
        # pygame.draw.rect(Surface, color, Rect, width=0)
        pygame.draw.rect(self.surface, self.black, self.surface.get_rect())
        self.screen.blit(self.surface, (0,0))