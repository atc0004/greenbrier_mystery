import pygame

class Scene:
    def __init__(self, color, screen):
        self.background = color
        self.screen = screen
    
    def render_scene(self):
        self.screen.fill(self.background)
