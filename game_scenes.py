import pygame
from scenebase import SceneBase
from objects import Box, Painting


class Hall_Scene(SceneBase):
    def __init__(self, game):
        SceneBase.__init__(self)
        self.game = game
        self.player = self.game.player
        self.screen = self.game.screen

        self.moving = False
        self.bgX = 0
        self.bg_image = pygame.image.load('assets/scene_1.png')
        self.bg_sepia = pygame.image.load('assets/hall_sepia.png')
        self.edge_X = self.bgX + 1920
        self.box_relative_position = 0
        self.collides = False
<<<<<<< HEAD
        self.box = Box((2100, 775), 'assets/classifiedcrate.png',
                       self.screen, True)
=======
        self.box = Box((1921, 775), 'assets/classifiedcrate.png',
                           self.screen, True)
>>>>>>> f3a75097771f9c6bb4c344e3b8f84cf7accf1edd
        self.box_group = pygame.sprite.Group(self.box)
        self.box_onscreen = False

    def ProcessInput(self, events, pressed_keys):

        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.moving = True
            if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                self.moving = False
            self.Update()

    def Update(self):
        if self.moving and not self.collides and self.player.x >= 900:
            self.bgX -= 6
            # if self.box_onscreen:
            self.box.rect.x -= 6
        self.edge_X = self.bgX + 1920
        if self.edge_X <= 1450 and self.player.get_details()['Time'] != 1861:
            # Render the box

            self.box_onscreen = True
<<<<<<< HEAD
            collisions = pygame.sprite.spritecollide(
                self.player, self.box_group, False, collided=None)
=======
            # collisions = pygame.sprite.spritecollide(
                # self.player, self.box_group, False, collided=None)
>>>>>>> f3a75097771f9c6bb4c344e3b8f84cf7accf1edd
            self.collides = False
            if len(collisions) != 0:
                self.player.walking = False
                self.moving = False
                self.collides = True
                if isinstance(collisions[0], Box):
                    pass
<<<<<<< HEAD
        if self.player.get_details()['Time'] == 1861:
            self.box_onscreen = False
=======


>>>>>>> f3a75097771f9c6bb4c344e3b8f84cf7accf1edd

        pygame.display.update()

    def Render(self, screen, sepia):
        if sepia:
            screen.blit(self.bg_sepia, (self.bgX, 0))
        else:
            screen.blit(self.bg_image, (self.bgX, 0))
<<<<<<< HEAD
            # Show message to player to go back in time, box fades away, player can move forward

        if self.box_onscreen:
            self.box_group.update()
            self.box_group.draw(screen)
=======

        # if self.edge_X <= 1450 and self.player.get_details()['Time'] != 1861:
        #     # Render the box
            
        #     self.box_onscreen = True
        #     # collisions = pygame.sprite.spritecollide(
        #         # self.player, self.box_group, False, collided=None)
        #     self.collides = False
        #     if len(collisions) != 0:
        #         self.player.walking = False
        #         self.moving = False
        #         self.collides = True
        #         if isinstance(collisions[0], Box):
        #             pass
                    # Show message to player to go back in time, box fades away, player can move forward
        if self.box_onscreen:
            obj_group.update()
            obj_group.draw(screen)
>>>>>>> f3a75097771f9c6bb4c344e3b8f84cf7accf1edd
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
        self.counter = 0
        self.doorOpenS = 'sounds/effects/door-open.wav'
<<<<<<< HEAD
=======

>>>>>>> f3a75097771f9c6bb4c344e3b8f84cf7accf1edd

        self.frameClicked = False
        self.chairClicked = False

        # Need to initialize the objects
        # Painting, Chair, folder, etc
        self.objects_list = [
            Painting((1000, 775), 'assets/classifiedcrate.png', self.screen, False, True)]
        self.objects_group = pygame.sprite.Group(self.objects_list[0])

    def ProcessInput(self, events, pressed_keys):

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for item in self.objects_list:
                    if item.rect.collidepoint(event.pos):
                        item.onclick()

    def Update(self):
<<<<<<< HEAD

        if(self.counter == 0):
            pygame.mixer.music.load(self.doorOpenS)
            pygame.mixer
        print("uh-oh, you didn't override this in the child class")
=======
      
        if(self.counter == 0):
          pygame.mixer.music.load(self.doorOpenS)
          pygame.mixer.music.play(0)
          self.counter = 1
        #print("uh-oh, you didn't override this in the child class")
>>>>>>> f3a75097771f9c6bb4c344e3b8f84cf7accf1edd

    def Render(self, screen, sepia):
        screen.blit(self.bg_image, (self.bgX, 0))
        self.objects_group.update()
        self.objects_group.draw(self.screen)

    def SwitchToScene(self, next_scene):
        self.counter = 0
        self.next = next_scene
