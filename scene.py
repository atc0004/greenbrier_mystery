import pygame

from text_blurb import TextBlurb


class Scene:
    """Basic Scene Class"""

    """Scene Initializer
    Initializes a font for scene, this will be moved to a global font in the game class likely
    Gets the screen from the main Game loop, might be better to pass the game object to things like this so we can get other details as well?
    Each scene is currently given a color to use as the background, but we should make a Background class possibly to load images and assets
    """

    def __init__(self, color, screen, message_text=''):
        self.font = pygame.font.Font(None, 25)
        self.background = color
        self.screen = screen
        if message_text != '':
            self.message = TextBlurb(self.font, message_text,
                                 (200, 200), self.screen, autoreset=False)
        # self.image = pygame.image.load('./quicktopdown.PNG')

    """Scene Renderer
    Renders the background to the screen
    """

    def render_scene(self):
        # self.screen.fill(self.background)

        self.screen.blit(self.background, (0,0))
        if hasattr(self, 'message'):
            self.message.draw()
            pygame.display.flip()

    """Scene Updater
    This will be used to update things within the scene (animations, TextBlurbs, etc)
    """

    def update_scene(self):
        if hasattr(self, 'message'):
            self.message.update()
            if not self.message.finished:
                self.message.draw()
            pygame.display.flip()


    """Reset Scene

    Only want to do this with things such as text.. maybe? could be removed at a later date
    Objects in the scene do not need readded when reset if they were already acquired by the player
    """

    def reset_scene(self):
        if hasattr(self, 'message'):
            self.message.reset()
