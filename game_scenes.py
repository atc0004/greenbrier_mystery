import pygame
from scenebase import SceneBase


class Hall_Scene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.moving = False
        self.bgX = 0
        self.bg_image = pygame.image.load('assets/scene_1.png')

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                # Move to the next scene when the user pressed Enter
                self.moving = True
            if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                self.moving = False
            self.Update()

    def Update(self):
        if self.moving:
            self.bgX -= 3
        # pygame.display.update()

    def Render(self, screen):
        screen.blit(self.bg_image, (self.bgX,0))
        pygame.display.update()

    def SwitchToScene(self, next_scene):
        self.next = next_scene

class Room_Scene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
    
    def ProcessInput(self, events, pressed_keys):
        pass

    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene
