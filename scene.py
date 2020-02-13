import pygame

from text_blurb import TextBlurb


class Scene:
    """Basic Scene Class"""

    """Scene Initializer
    Initializes a font for scene, this will be moved to a global font in the game class likely
    Gets the screen from the main Game loop, might be better to pass the game object to things like this so we can get other details as well?
    Each scene is currently given a color to use as the background, but we should make a Background class possibly to load images and assets
    """
    def __init__(self, color, screen):
        self.font = pygame.font.Font(None, 25)
        self.background = color
        self.screen = screen
        if self.background == (255, 0, 0):
            self.message = TextBlurb(self.font, "Hello world...",
                                     (200, 200), self.screen, autoreset=False)

    """Scene Renderer
    Renders the background to the screen
    """
    def render_scene(self):
        self.screen.fill(self.background)
        if self.background == (255, 0, 0):
            self.message.draw()
            pygame.display.flip()

    """Scene Updater
    This will be used to update things within the scene (animations, TextBlurbs, etc)
    """
    def update_scene(self, eventType):
        if self.background == (255, 0, 0):
            self.message.update()
