import pygame
from scenebase import SceneBase
from objects import Box, Chair, Document, DocumentItem, Gear, GearItem, Item, Painting


class Hall_Scene(SceneBase):
    def __init__(self, game):
        SceneBase.__init__(self)
        self.game = game
        self.player = self.game.player
        self.screen = self.game.screen
        self.BG_SPEED = 4
        self.moving = False
        self.moving_left = False
        self.w, self.h = pygame.display.get_surface().get_size()
        self.bgX = 0
        self.bg_image = pygame.image.load('assets/scene_1.png').convert_alpha()
        self.bg_sepia = pygame.image.load(
            'assets/hall_sepia.png').convert_alpha()
        self.edge_X = self.bgX + 1920
        self.box_relative_position = 0
        self.collides = False
        self.box = Box((2400, 775), 'assets/classifiedcrate.png',
                       self.screen, True)
        self.box_group = pygame.sprite.Group(self.box)
        self.box_onscreen = False
        self.canAdvance = False

    def ProcessInput(self, events, pressed_keys):

        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                self.moving = True
            if event.type == pygame.KEYUP and event.key == pygame.K_d:
                self.moving = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                self.moving_left = True
            if event.type == pygame.KEYUP and event.key == pygame.K_a:
                self.moving_left = False
            self.Update()

    def Update(self):
        # (self.bgX)
        if self.moving and not self.collides and self.player.x > self.w/2-1 and self.bgX > -2500:
            self.bgX -= self.BG_SPEED
            # if self.box_onscreen:
            self.box.rect.x -= self.BG_SPEED
        if self.moving_left and not self.collides and self.bgX < 0:
            self.bgX += self.BG_SPEED
            # if self.box_onscreen:
            self.box.rect.x += self.BG_SPEED
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
        if(self.bgX <= -1600):
            self.canAdvance = True
        else:
            self.canAdavance = False
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
        self.is_new_item = None
        self.new_item_group = pygame.sprite.Group()
        self.items_found = 0
        self.items_available = 2
        self.canAdvance = False
        self.detail_image = pygame.image.load(
            'assets/bunker_details.PNG').convert()
        self.detail_rect = self.detail_image.get_rect(center=(w/2, h/2))
        self.display_file_contents = False

    def ProcessInput(self, events, pressed_keys):

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.display_file_contents:
                    self.display_file_contents = False
                print(event.pos)
                for item in self.objects_list:
                    if item.rect.collidepoint(event.pos):
                        self.is_new_item = item.onclick()
                        if issubclass(self.is_new_item.__class__, Item):
                            if isinstance(self.is_new_item, DocumentItem):
                                print("Instance of document, show content")
                            # self.screen.blit(self.detail_image, self.detail_rect)
                                self.display_file_contents = True
                            self.player.add_item(self.is_new_item.name)
                            self.is_new_item = None
                            self.items_found += 1

    def Update(self):

        if(self.counter == 0):
            creak = pygame.mixer.Sound(self.doorOpenS)
            creak.set_volume(0.3)
            creak.play()
            self.counter = 1
            pygame.mixer
        if self.items_found == self.items_available:
            self.canAdvance = True

    def Render(self, screen, sepia):
        if pygame.mixer.get_busy():
            return
        screen.blit(self.bg_image, (self.bgX, 0))

        # for obj in self.objects_list:
        # obj.update()
        # obj.draw(self.screen)
        if self.is_new_item is not None and self.items_found < self.items_available:
            # print(self.is_new_item)
            self.new_item_group.add(self.is_new_item)
            self.objects_list.append(self.is_new_item)
            self.new_item_group.update()
            self.new_item_group.draw(self.screen)

        self.objects_group.update()
        self.objects_group.draw(self.screen)
        if self.display_file_contents:
            self.screen.blit(self.detail_image, self.detail_rect)

    def SwitchToScene(self, next_scene):
        self.counter = 0
        self.next = next_scene
