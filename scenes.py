import pygame

from text_blurb import TextBlurb


class Scene:
    """Basic Scene Class"""

    """Scene Initializer
    Initializes a font for scene, this will be moved to a global font in the game class likely
    Gets the screen from the main Game loop, might be better to pass the game object to things like this so we can get other details as well?
    Each scene is currently given a color to use as the background, but we should make a Background class possibly to load images and assets
    """

    def __init__(self, color, screen, message_text='', image=''):
        self.bgX = 0
        self.font = pygame.font.Font(None, 25)
        self.background = color
        self.screen = screen
        if message_text != '':
            self.message = TextBlurb(self.font, message_text,
                                     (200, 200), self.screen, autoreset=False)
        if image != '':
            self.image = pygame.image.load(image)

    def render_scene(self):
        self.screen.fill(self.background)
        if self.image is not None:
            self.screen.blit(self.image, (self.bgX,0))
        if hasattr(self, 'message'):
            self.message.draw()
            pygame.display.flip()

    """Scene Updater
    This will be used to update things within the scene (animations, TextBlurbs, etc)
    """

    def update_scene(self, scroll):
        if hasattr(self, 'message'):
            self.message.update()
            if not self.message.finished:
                self.message.draw()
            pygame.display.flip()
        if scroll:
            self.screen.blit(self.image, (self.bgX,0))
            self.bgX -= 1
        pygame.display.update()

    """Reset Scene

    Only want to do this with things such as text.. maybe? could be removed at a later date
    Objects in the scene do not need readded when reset if they were already acquired by the player
    """

    def reset_scene(self):
        if hasattr(self, 'message'):
            self.message.reset()
