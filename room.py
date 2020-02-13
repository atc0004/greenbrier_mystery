import pygame
from scene import Scene
from itertools import cycle
class Room:
    """ Class for a Room in the game

    Each room will have a list of scenes
    Each scene needs to be loaded or have the option of being loaded when the next scene button is clicked (right +1, left -1)
        
    """
    def __init__(self, screen):
        self.screen = screen
        self.room_name = 'test'
        self.color_list = [(0,0,0),(255,255,255),(255,0,0),(0,255,0),(0,0,255)]
        self.scene_list =self.generate_scenes()
        self.start_scene = self.scene_list[0]
        self.current_scene_pos = 0
        self.current_scene = self.start_scene
        self.scene_count = len(self.scene_list)

    def __str__(self):
        return f"{self.room_name}: {self.scene_list}"
    def get_scenes(self):
        return self.scene_list
    
    def generate_scenes(self):
        scene_list = []
        for x in range(5):
            scene_list.append(Scene(self.color_list[x], self.screen))
        return scene_list
    
    def get_next_scene(self):
        self.current_scene_pos +=1
        if self.current_scene_pos == self.scene_count:
            self.current_scene_pos = 0
        self.current_scene = self.scene_list[self.current_scene_pos]
        
    
    def get_prev_scene(self):
        self.current_scene_pos -= 1
        if self.current_scene_pos == -1:
            self.current_scene_pos = self.scene_count-1
        self.current_scene = self.scene_list[self.current_scene_pos]
        
    def render_current_scene(self):
        self.current_scene.render_scene()
    def update_current_scene(self, event):
        self.current_scene.update_scene(event)