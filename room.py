import pygame
from scene import Scene
from itertools import cycle


class Room:
    """ Class for a Room in the game

    Each room will have a list of scenes
    Each scene needs to be loaded or have the option of being loaded when the next scene button is clicked (right +1, left -1)

    """

    """Room Initializer
    
    Gets assigned the main screen for later use, 
    Each room gets a name for reference
    color_list is temporary, this would likely be a list of scenes or backgrounds for scenes
    Initializes scene counters
    """

    def __init__(self, screen):
        self.screen = screen
        self.room_name = 'test'
        self.color_list = [(0, 0, 0), (255, 255, 255),
                           (255, 0, 0), (0, 255, 0), (0, 0, 255)]
        self.scene_list = self.generate_scenes()
        self.start_scene = self.scene_list[0]
        self.current_scene_pos = 0
        self.current_scene = self.start_scene
        self.scene_count = len(self.scene_list)

    # Just to pretty print the Room details
    def __str__(self):
        return f"{self.room_name}: {self.scene_list}"

    """Getter for scene list"""

    def get_scenes(self):
        return self.scene_list

    """Scene Generator

    As of 2/13/2020 this is how scenes are generated, this will be static for each room in later versions
    """

    def generate_scenes(self):
        scene_list = []
        for x in range(5):
            scene_list.append(Scene(self.color_list[x], self.screen))
        return scene_list

    """Get Next Scene
    Sets the current scene to be the next scene
    """

    def get_next_scene(self):
        self.current_scene_pos += 1
        if self.current_scene_pos == self.scene_count:
            self.current_scene_pos = 0
        self.current_scene = self.scene_list[self.current_scene_pos]

    """Get Previous Scene
    Sets the current scene to be the previous scene
    """

    def get_prev_scene(self):
        self.current_scene_pos -= 1
        if self.current_scene_pos == -1:
            self.current_scene_pos = self.scene_count-1
        self.current_scene = self.scene_list[self.current_scene_pos]


    """Render the Current Scene"""

    def render_current_scene(self):
        self.current_scene.render_scene()

        
    """If scene was already rendered, just update the current scene"""

    def update_current_scene(self, event):
        self.current_scene.update_scene(event)
