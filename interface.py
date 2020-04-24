import pygame

import math
from time import sleep


class UI:
    def __init__(self, screen, player, debug=False):
        self.screen = screen
        self.player = player
        self.details = self.player.get_details()
        self.debug = debug
        self.black = (0, 0, 0, 100)
        self.surface = pygame.Surface((100, 1200), pygame.SRCALPHA)
        self.rect = pygame.Rect((0, 0), (100, 1200))
        self.font = pygame.font.Font('assets/fonts/Cheap_Pine_Sans.otf', 30)
        self.talkfont =  pygame.font.Font('assets/fonts/Cheap_Pine_Sans.otf', 28)
        self.date_font = pygame.font.Font(
            'assets/fonts/Cheap_Pine_Sans.otf', 20)
        self.date_changing = False

        self.w, self.h = pygame.display.get_surface().get_size()
        self.folder_image = pygame.image.load(
            'assets/ui/folder.png').convert_alpha()
        self.gear_image = pygame.image.load(
            'assets/ui/gear.png').convert_alpha()
        self.key_image = pygame.image.load('assets/ui/key.png').convert_alpha()
        self.note_image = pygame.image.load(
            'assets/ui/note.png').convert_alpha()

        self.folder_image = pygame.transform.smoothscale(
            self.folder_image, (60, 60))
        self.gear_image = pygame.transform.smoothscale(
            self.gear_image, (60, 60))
        self.key_image = pygame.transform.smoothscale(self.key_image, (60, 60))
        self.note_image = pygame.transform.smoothscale(
            self.note_image, (60, 60))

        self.folder_rect = self.folder_image.get_rect()
        self.gear_rect = self.gear_image.get_rect()
        self.key_rect = self.key_image.get_rect()
        self.note_rect = self.note_image.get_rect()

        self.folder_rect.centerx = 50
        self.gear_rect.centerx = 50
        self.key_rect.centerx = 50
        # self.note_rect.centerx = 50

        self.gear_rect.centery = self.h * (1/6)
        self.folder_rect.centery = self.h * (2/6)
        self.key_rect.centery = self.h * (1/2)
        self.watch_image = pygame.image.load(
            'assets/ui/watch.png').convert_alpha()
        x, y = self.watch_image.get_rect().size
        self.watch_image = pygame.transform.smoothscale(
            self.watch_image, (int(x*.3), int(y*.3)))
        self.small_hand = pygame.image.load(
            'assets/ui/short_hand.png').convert_alpha()
        x, y = self.small_hand.get_rect().size
        self.small_hand = pygame.transform.smoothscale(
            self.small_hand, (int(x*.25), int(y*.25)))
        self.big_hand = pygame.image.load(
            'assets/ui/big_hand.png').convert_alpha()
        x, y = self.big_hand.get_rect().size
        self.big_hand = pygame.transform.smoothscale(
            self.big_hand, (int(x*.25), int(y*.25)))

        self.watch_rect = self.watch_image.get_rect()
        self.small_hand_rect = self.small_hand.get_rect()
        self.big_hand_rect = self.big_hand.get_rect()

        self.watch_rect.center = (100, self.h*0.9)
        self.face_center = (self.watch_rect.centerx - 14,
                            self.watch_rect.centery + 7)
        self.big_hand_rect.center = self.face_center
        self.small_hand_rect.center = self.face_center
        self.player_char = pygame.image.load('assets/characters/boy.png').convert_alpha()
        self.player_rect = self.player_char.get_rect(center=(300, self.h))
        self.frame_count = 0
        self.target_date = self.details['Time']
        self.curTime = self.target_date
        self.text_box_image = pygame.transform.smoothscale(pygame.image.load('assets/ui/dialogue_info.png').convert_alpha(), (850, 125))
        self.text_box_rect = self.text_box_image.get_rect(bottomleft=(0, self.h))
        
        # self.tiptimer = 100000
        # self.tiptimercounter = 0
        self.displaytip = True
        self.tipCount = 0
        self.tips = ['Maybe I should look around. Move with a and d.',
                     'I can use my watch with t, maybe that will help me.', 'I should have a look around.',
                     "Oh no a crate is in my way"]

        self.roomtips =["Look there's another gear for the watch!", "Hey look a classified file! I should read it",
                        "I should try to find the old man again.."]
        self.roomtipcount = -1
        self.displayroomtip = False

    def update(self):
        self.details = self.player.get_details()
        self.frame_count += 1
        pygame.display.update()

    def render(self):
        pygame.draw.rect(self.surface, self.black, self.surface.get_rect())
        self.render_player_details()

        self.render_text_box()
        self.render_character_head()
        if self.displaytip:
            self.render_dialogue_view()
        if self.displayroomtip:
            self.render_room_dialogue()
        self.render_watch()

    def render_character_head(self):
        self.screen.blit(self.player_char, self.player_rect)

    def render_watch(self):
        # Need to render watch first, then render the hand rotating
        if self.curTime == self.target_date:
            self.player.change_date(self.target_date)
            self.date_changing = False
        big = pygame.transform.rotate(
            self.big_hand, self.frame_count*12).convert_alpha()
        small = pygame.transform.rotate(
            self.small_hand, -self.frame_count*3).convert_alpha()
        rect = big.get_rect(center=self.face_center)
        rect2 = small.get_rect(center=self.face_center)
        #curTime = self.details['Time']
        if self.curTime != self.target_date and self.date_changing:
            if self.target_date < self.curTime:
                self.curTime -= 2
            if self.target_date > self.curTime:
                self.curTime += 2
        self.date_surface = self.date_font.render(
            f"{self.curTime}", True, (0, 0, 0))
        self.date_rect = self.date_surface.get_rect()
        self.date_rect.centerx = self.face_center[0]
        self.date_rect.centery = self.face_center[1] + 15
        if self.frame_count >= 360:
            # print("360")
            self.frame_count = 0
        self.screen.blit(self.watch_image, self.watch_rect)
        self.screen.blit(self.date_surface, self.date_rect)
        pygame.draw.circle(self.screen, (0, 0, 0), self.face_center, 5)

        self.screen.blit(big, rect)
        self.screen.blit(small, rect2)
        pygame.display.flip()

    def render_dialogue_view(self):
        white = (255, 255, 255)

        dialogue_surface = self.talkfont.render(
            f"{self.tips[self.tipCount]}", True, white)
        #self.screen.blit(self.surface, (0, 0))
        dialoguerect = dialogue_surface.get_rect()
        dialoguerect.topleft = (self.player_rect.centerx + self.player_rect.width/2, 0.93*self.h)
        self.screen.blit(dialogue_surface, dialoguerect)

    def render_room_dialogue(self):
        white = (255, 255, 255)
        dialogue_surface = self.talkfont.render(
            f"{self.roomtips[self.roomtipcount]}", True, white)
        # self.screen.blit(self.surface, (0, 0))
        dialoguerect = dialogue_surface.get_rect()
        dialoguerect.topleft = (self.player_rect.centerx + self.player_rect.width / 2, 0.93 * self.h)
        self.screen.blit(dialogue_surface, dialoguerect)

    def showroomtip(self,x = -1):
        if x == -1:
            self.diaplyroomtip = False
        if x == 1:
            self.roomtipcount = 0
            self.displayroomtip = True

        if x == 2:
            self.roomtipcount = 1
            self.displayroomtip = True
        if x == 3:
            self.roomtipcount = 2
            self.displayroomtip = True


    def showTip(self):
        # self.displaytip = True
        self.tipCount += 1
        if self.tipCount >= len(self.tips):
            self.displaytip = False

        # self.tiptimercounter = self.tiptimer

    def render_text_box(self):
        self.screen.blit(self.text_box_image, self.text_box_rect)

    def render_player_details(self):
        self.screen.blit(self.surface, (0, 0))
        self.screen.blit(self.gear_image, self.gear_rect)
        self.screen.blit(self.folder_image, self.folder_rect)
        self.screen.blit(self.key_image, self.key_rect)
        white = (255, 255, 255)
        parts_surface = self.font.render(
            f"{self.details['Parts']}/4", True, white)
        folders_surface = self.font.render(
            f"{self.details['Folders']}/3", True, white)
        keys_surface = self.font.render(str(self.details['Keys']), True, white)

        parts_rect = parts_surface.get_rect()
        folders_rect = folders_surface.get_rect()
        keys_rect = keys_surface.get_rect()
        parts_rect.center = (50, self.h * (1/6) + 50)
        folders_rect.center = (50, self.h * (2/6) + 50)
        keys_rect.center = (50, self.h * (3/6) + 50)

        self.screen.blit(parts_surface, parts_rect)
        self.screen.blit(folders_surface, folders_rect)
        self.screen.blit(keys_surface, keys_rect)

        floor_surface = self.font.render(
            f"Floor {self.details['Floor']}", True, white)
        floor_rect = floor_surface.get_rect()
        floor_rect.center = (50, 35)
        self.screen.blit(floor_surface, floor_rect)

    def change_date(self):
        print(self.curTime)
        print(self.target_date)
        self.date_changing = True
        curTime = self.details['Time']

        if curTime == 1861:
            self.target_date = 1961
        if curTime == 1961:
            self.target_date = 1861
