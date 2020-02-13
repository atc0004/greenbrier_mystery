import pygame

from text_blurb import TextBlurb


class Scene:
    def __init__(self, color, screen):
        self.font = pygame.font.Font(None, 25)
        self.background = color
        self.screen = screen
        if self.background == (255, 0, 0):
            self.message = TextBlurb(self.font, "Hello world...",
                                     (200, 200), self.screen, autoreset=False)

    def render_scene(self):
        self.screen.fill(self.background)
        if self.background == (255, 0, 0):
            self.message.draw()
            pygame.display.flip()

    def update_scene(self, eventType):
        if self.background == (255, 0, 0):
            self.message.update()
