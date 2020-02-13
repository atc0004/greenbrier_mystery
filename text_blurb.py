import pygame


class TextBlurb:
    def __init__(self, font, text, pos, screen, autoreset=False):
        self.finished = False
        self.font = font
        self.text = text
        self.autoreset=autoreset
        self.screen = screen
        self._generated = self.text_generator()
        self.pos = pos
        self.update()
        

    def text_generator(self):
        tmp = ''
        for letter in self.text:
            tmp += letter
            if letter != ' ':
                yield tmp

    def reset(self):
        self._generated = self.text_generator()
        self.finished = False
        self.update()

    def update(self):
        if not self.finished:
            try:
                self.rendered = self.font.render(
                    next(self._generated), True, (0, 128, 0))
            except StopIteration:
                self.finished = True
                if self.autoreset:
                    self.reset()
    def draw(self):
        self.screen.blit(self.rendered, self.pos)
    