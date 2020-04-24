import pygame
from scenebase import SceneBase
from objects import Box, Painting, Chair


class Hall_Scene(SceneBase):
    def __init__(self, game):
        SceneBase.__init__(self)
        self.game = game
        self.player = self.game.player
        self.screen = self.game.screen

        self.moving = False
        self.bgX = 0
        self.bg_image = pygame.image.load('assets/scene_1.png').convert_alpha()
        self.bg_sepia = pygame.image.load('assets/hall_sepia.png').convert_alpha()
        self.edge_X = self.bgX + 1920
        self.box_relative_position = 0
        self.collides = False
        self.box = Box((2400, 775), 'assets/classifiedcrate.png',
                       self.screen, True)
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
            collisions = pygame.sprite.spritecollide(
                self.player, self.box_group, False, collided=None)
            self.collides = False
            if len(collisions) != 0:
                self.player.walking = False
                self.moving = False
                self.collides = True
                if isinstance(collisions[0], Box):
                    pass
        if self.player.get_details()['Time'] == 1861:
            self.box_onscreen = False

        pygame.display.update()

    def Render(self, screen, sepia):
        if sepia:
            screen.blit(self.bg_sepia, (self.bgX, 0))
        else:
            screen.blit(self.bg_image, (self.bgX, 0))
            # Show message to player to go back in time, box fades away, player can move forward

        if self.box_onscreen:
            self.box_group.update()
            self.box_group.draw(screen)
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
        self.bg_image = pygame.image.load('assets/bedroom.png').convert_alpha()
        self.counter = 0
        self.doorOpenS = 'sounds/effects/door-open.wav'
        w, h = pygame.display.get_surface().get_size()
        self.frameClicked = False
        self.chairClicked = False
        self.frameCoords = (0.58 * w, 0.35*h)
        self.chairCoords = (0.7 * w, 0.6*h)
        # Need to initialize the objects
        # Painting, Chair, folder, etc
        self.objects_list = [
            Painting(self.frameCoords, 'assets/frame.png', self.screen, False, True), Chair(self.chairCoords, 'assets/chair.png', self.screen, False, True)]
        self.objects_group = pygame.sprite.Group()
        for i in self.objects_list:
            self.objects_group.add(i)

    def ProcessInput(self, events, pressed_keys):

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print(event.pos)
                for item in self.objects_list:
                    if item.rect.collidepoint(event.pos):
                        item.onclick()

    def Update(self):

        if(self.counter == 0):
            # pygame.mixer.music.load(self.doorOpenS)
            creak = pygame.mixer.Sound(self.doorOpenS)
            creak.set_volume(0.3)
            # pygame.mixer.music.play(0)
            creak.play()
            self.counter = 1
            pygame.mixer

            # while pygame.mixer.get_busy():
                # pass

        #print("uh-oh, you didn't override this in the child class")

    def Render(self, screen, sepia):
        screen.blit(self.bg_image, (self.bgX, 0))
        # for obj in self.objects_list:
        # obj.update()
        # obj.draw(self.screen)
        self.objects_group.update()
        self.objects_group.draw(self.screen)

    def SwitchToScene(self, next_scene):
        self.counter = 0
        self.next = next_scene
