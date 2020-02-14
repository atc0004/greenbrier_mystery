import pygame


class TextBlurb:
    """TextBlurb Class
    Creates a text blurb on the screen where the text will slowly come in, like Pokemon games
    """

    """TextBlurb Initializer
    Need some details for the blurb
    """
    def __init__(self, font, text, pos, screen, autoreset=False):
        self.finished = False
        self.font = font
        self.text = text
        self.autoreset=autoreset
        self.screen = screen
        self.firstPlay = True
        # pygame.mixer.init()
        self.sound = pygame.mixer.Sound("type.wav")
        self._generated = self.text_generator()
        self.pos = pos
        self.update()
        
    """Text Generator
    Yields at each letter so that the printing happens before the next one comes up
    """
    def text_generator(self):
        tmp = ''
        for letter in self.text:
            tmp += letter
            if letter != ' ':
                yield tmp
    """Reset Blurb
    Resets the text so that it goes away after it is finished
    """
    def reset(self):
        self._generated = self.text_generator()
        self.finished = False
        self.firstPlay = True
        self.update()
    """Text Updater
    Updates the text on the screen, either getting the next letter, printing first letter, or resetting text
    """
    def update(self):
        if not self.finished:
            try:
                self.rendered = self.font.render(
                    next(self._generated), True, (0, 128, 0))
            except StopIteration:
                self.sound.stop()
                self.sound.set_volume(0)
                pygame.mixer.stop()
                self.finished = True
                if self.autoreset:
                    self.reset()
    """Draw Text
    Renders text to the screen
    """
    def draw(self):
        self.screen.blit(self.rendered, self.pos)
        if self.firstPlay:
            self.sound.set_volume(1)
            self.sound.play()
            self.firstPlay = False
        
    