import pygame


class Button:
    def __init__(self, button_rect, text='', font=None, default_surface=None, hover_surface=None):
        self.button_rect = pygame.Rect(button_rect)
        self.text = text
        if font is None:
            self.font = pygame.font.Font('freesanbold.ttf', 20)
        else:
            self.font = font
        self.default_surface = default_surface
        self.hover_surface = hover_surface
        self.button_pressed = False
        self.button_highlighted = False
        self.last_down_over_button = False
        self.visible = True
        

    def draw(self, screen):
        if self.button_highlighted:
            screen.blit(self.hover_surface, self.button_rect)
        else:
            screen.blit(self.default_surface, self.button_rect)

    def update(self):
        if self.button_highlighted:
            text_color = (255,255,255)
        else:
            text_color = (235, 222, 100)
        text_surface = self.font.render(self.text, True, text_color)
        text_rect = text_surface.get_rect()
        text_rect.center = int(self.button_rect.width /
                               2), int(self.button_rect.height/2)
        self.default_surface.blit(text_surface, text_rect)
        self.hover_surface.blit(text_surface, text_rect)
        # self.hover_surface = self.default_surface

    def handle_event(self, event):
        actions = []
        exit_button = False
        if not self.button_highlighted and self.button_rect.collidepoint(event.pos):
            # Mouse enters button, change to hover surface
            self.button_highlighted = True
            actions.append('enter')
            # self.mouseEnter() # Might be a function that plays a sound or somehting
        elif self.button_highlighted and not self.button_rect.collidepoint(event.pos):
            # Left button
            self.button_highlighted = False
            exit_button = True

        if self.button_rect.collidepoint(event.pos):
            # Mouse event happened over button
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.button_pressed = True
                self.last_down_over_button = True
                actions.append('click')
        
        clicked = False
        if event.type == pygame.MOUSEBUTTONUP:
            if self.last_down_over_button:
                clicked = True
            if self.button_pressed:
                self.button_pressed = False
            if clicked:
                self.button_pressed = False
                # self.mouseClick(event)
        if exit_button:
            actions.append('exit')
        return actions
