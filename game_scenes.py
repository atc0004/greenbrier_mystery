import pygame
from scenebase import SceneBase
from objects import Box, Painting


class Hall_Scene(SceneBase):
    def __init__(self, player, screen):
        SceneBase.__init__(self)
        self.moving = False
        self.bgX = 0
        self.bg_image = pygame.image.load('assets/scene_1.png')
        self.bg_sepia = pygame.image.load('assets/hall_sepia.png')
        self.edge_X = self.bgX + 1920
        self.box_relative_position = 0
        self.player = player
        self.collides = False
        self.screen = screen
        self.box = Box((1921, 775), 'assets/classifiedcrate.png',
                           self.screen, True)
        self.box_onscreen = False
        

    def ProcessInput(self, events, pressed_keys):

        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.moving = True
            if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                self.moving = False
            self.Update()

    def Update(self):
        if self.moving and not self.collides and not self.player.x < 900:
            self.bgX -= 6
            if self.box_onscreen:
                self.box.rect.x -= 6
        self.edge_X = self.bgX + 1920
        pygame.display.update()

    def Render(self, screen, sepia):
        if sepia:
            screen.blit(self.bg_sepia, (self.bgX, 0))
        else:
            screen.blit(self.bg_image, (self.bgX, 0))

        if self.edge_X <= 1450 and self.player.get_details()['Time'] != 1861:
            # Render the box
            
            self.box_onscreen = True
            obj_group = pygame.sprite.Group(self.box)
            collisions = pygame.sprite.spritecollide(
                self.player, obj_group, False, collided=None)
            self.collides = False
            if len(collisions) != 0:
                self.player.walking = False
                self.moving = False
                self.collides = True
                if isinstance(collisions[0], Box):
                    pass
                    # Show message to player to go back in time, box fades away, player can move forward
            obj_group.update()
            obj_group.draw(screen)
        else:
            self.collides = False

    def SwitchToScene(self, next_scene):
        self.next = next_scene


class Room_Scene(SceneBase):
    def __init__(self, player, screen):
        SceneBase.__init__(self)
        self.player = player
        self.screen = screen
        self.bgX = 0
        self.bg_image = pygame.image.load('assets/bedroom.png')


        self.frameClicked = False
        self.chairClicked = False

        # Need to initialize the objects
        # Painting, Chair, folder, etc
        self.objects_list = [Painting((1000, 775), 'assets/classifiedcrate.png', self.screen, False, True)]
        self.objects_group = pygame.sprite.Group(self.objects_list[0])

    def ProcessInput(self, events, pressed_keys):

        for event in events:
          if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for item in self.objects_list:
              if item.rect.collidepoint(event.pos):
                item.onclick()

    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen, sepia):
        screen.blit(self.bg_image, (self.bgX, 0))
        self.objects_group.update()
        self.objects_group.draw(self.screen)

    def SwitchToScene(self, next_scene):
        self.next = next_scene
