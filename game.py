import pygame
import os
from button import PlayButton, SettingsButton, ExitButton, BackButton
from game_scenes import Hall_Scene, Room_Scene, Character_Scene
from player import Player
from objects import Box
from interface import UI


class Game:
    """ Game Class that is the master to all other game content
    """

    """Game initializer

    Initializes pygame, the Screen, clock, room(s), and gets the scene list as of 2/13/2020
    """
    # sounds
    achievementS = 'sounds/effects/achievement.wav'
    doorOpenS = 'sounds/effects/door-open.wav'
    slidings = 'sounds/effects/sliding.wav'

    def __init__(self):
        os.environ['SDL_VIDEO_WINDOW_POS'] = "0,1"
        # os.environ['SDL_VIDEODRIVER'] = 'directx'
        self.WINDOW_SIZE = [1920, 1080]

        pygame.init()
        # sound
        self.gameM = 'sounds/music/Greenbrier.wav'
        self.timeTravel = pygame.mixer.Sound(
            'sounds/effects/timetravel_short.wav')
        self.timeTravel.set_volume(0.1)
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        pygame.display.set_caption('The Greenbrier - A Mystery In Time')
        pygame.mixer.music.set_volume(0.01)
        pygame.mixer.fadeout(500)
        # self.screen = pygame.display.set_mode(
        # self.WINDOW_SIZE, flags=pygame.FULLSCREEN | pygame.DOUBLEBUF)
        self.done = False
        self.clock = pygame.time.Clock()
        self.menu = True
        # self.player = Player(self.screen)
        self.all_scenes = []
        # self.all_scenes = [
        #     ("Hallway", Hall_Scene(self)),
        #     ("Room_Scene", Room_Scene(self.player, self.screen))
        # ]
        self.scene_names = ["Hallway", "Room_Scene"]
        self.scene_num = 0
        # self.current_scene = self.all_scenes[self.scene_num][1]
        self.collision_counter = 0
        self.bleedout_timer = 0
        self.bleeding = False
        self.model_chosen = 'girl'

    """Main Game Loop

    Runs the game, initializes objects and logic.
    """

    def main_loop(self):
        self.player = Player(self.screen, self.model_chosen)
        self.all_scenes = [
            ("Hallway", Hall_Scene(self)),
            ("Room_Scene", Room_Scene(self.player, self.screen))
        ]
        self.current_scene = self.all_scenes[self.scene_num][1]
        pygame.mixer.music.load(self.gameM)
        pygame.mixer.music.play(-1)
        my_group = pygame.sprite.Group(self.player)
        # hall = Hall_Scene(player, self.screen)
        user_interface = UI(self.screen, self.player, True)
        timechange = False
        # print(type(self.screen))
        tip = False
        pygame.time.set_timer(pygame.USEREVENT, 4000)
        while not self.done:

            sepia = False
            events = []
            quit_opt = False

            if self.bleeding:
                self.bleedout_timer += 1
                if (self.bleedout_timer % 10 == 0):
                    # moving backwards
                    if self.player.details['Time'] != 1861:
                        self.screen.fill((240, 208, 2))
                        user_interface.render()
                        user_interface.update()
                    else:  # moving forward in time
                        self.screen.fill((106, 194, 252))
                        user_interface.render()
                        user_interface.update()
            if self.bleedout_timer > 60:
                self.bleeding = False
                self.bleedout_timer = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_opt = True
                elif event.type == pygame.USEREVENT:
                    # tip = False
                    user_interface.showTip()
                    pygame.time.set_timer(pygame.USEREVENT, 4000)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        quit_opt = True
                    if event.key == pygame.K_d:
                        self.player.walking = True
                    if event.key == pygame.K_a:
                        self.player.walking_left = True
                    if event.key == pygame.K_t:
                        # player.change_date()
                        self.timeTravel.play()
                        user_interface.change_date()
                        timechange = True
                        self.bleeding = True
                        self.bleedout_timer = 0
                    if event.key == pygame.K_RETURN:
                        # if(self.scene_num == 0):
                        if(self.current_scene.canAdvance):
                            self.scene_num += 1
                            if self.scene_num == len(self.all_scenes):
                                self.scene_num = 0
                            self.current_scene.SwitchToScene(
                                self.all_scenes[self.scene_num][1])
                            self.current_scene = self.all_scenes[self.scene_num][1]
                            print(
                                f"Curr Scene {self.scene_num} : {self.current_scene}")

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        self.player.walking = False

                    if event.key == pygame.K_a:
                        self.player.walking_left = False

                if quit_opt:
                    self.done = True
                else:
                    events.append(event)

            self.current_scene.ProcessInput(events, [])
            self.current_scene.Update()
            if self.player.details['Time'] == 1861:
                # Apply overlay
                sepia = True
            self.current_scene.Render(self.screen, sepia)
            if self.scene_num == 0:
                # Show player
                my_group.update()
                my_group.draw(self.screen)

            user_interface.render()
            user_interface.update()
            # user_interface.render_dialogue_view()
            # tip = False

            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
        exit()

    def settings_menu(self):
        print('settings menu starting')

        gb_img = pygame.image.load('assets/menu_bg.png').convert_alpha()
        button1_img = pygame.image.load('assets/button.png').convert_alpha()
        button1_hover = pygame.image.load(
            'assets/button_hover.png').convert_alpha()
        button_font = pygame.font.Font(
            './assets/fonts/Cheap_Pine_Sans.otf', 100)
        button1_rect = pygame.Rect(720, 840, 520, 170)
        back_button = BackButton(button1_rect, "BACK",
                                 button_font, button1_img, button1_hover)
        all_buttons = [back_button]
        t_img = pygame.image.load('assets/menus/key_t.png').convert_alpha()
        t_img_rect = t_img.get_rect(center=(300, 100))
        a_img = pygame.image.load('assets/menus/key_a.png').convert_alpha()
        a_img_rect = a_img.get_rect(center=(300, 300))
        d_img = pygame.image.load('assets/menus/key_d.png').convert_alpha()
        d_img_rect = d_img.get_rect(center=(300, 500))
        enter_img = pygame.image.load(
            'assets/menus/key_enter.png').convert_alpha()
        enter_img_rect = enter_img.get_rect(center=(1200, 100))
        mouseclick_img = pygame.image.load(
            'assets/menus/mouseclick.png').convert_alpha()
        mouseclick_rect = mouseclick_img.get_rect(center=(1200, 325))

        white = (255, 255, 255)
        controls_font = pygame.font.Font(
            './assets/fonts/Cheap_Pine_Sans.otf', 75)

        atxt = controls_font.render("Move Left", True, white)
        dtxt = controls_font.render("Move Right", True, white)
        ttxt = controls_font.render("Use Watch", True, white)
        textsr1 = [ttxt, atxt, dtxt, ]

        entertxt = controls_font.render("Enter Area", True, white)
        mousetxt = controls_font.render("Object Interaction", True, white)
        textsr2 = [entertxt, mousetxt]
        rects = [t_img_rect, a_img_rect, d_img_rect]

        x = 0
        while self.menu:
            # render menu
            self.screen.blit(gb_img, (0, 0))
            self.screen.blit(d_img, d_img_rect)
            self.screen.blit(a_img, a_img_rect)
            self.screen.blit(t_img, t_img_rect)
            self.screen.blit(enter_img, enter_img_rect)
            self.screen.blit(mouseclick_img, mouseclick_rect)

            x = 400
            y = 100
            for t in textsr1:
                self.screen.blit(t, (x, y))
                y = y + 200
            x = 1350
            y = 100
            for t in textsr2:
                self.screen.blit(t, (x, y))
                y = y + 225

            for b in all_buttons:
                b.draw(self.screen)
                b.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                    pygame.quit()
                    exit()
                elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEMOTION, pygame.MOUSEBUTTONUP):
                    for b in all_buttons:
                        button_events = b.handle_event(event)
                        if 'click' in button_events:
                            b.mouse_click(self)
                        elif 'enter' in button_events:
                            b.mouse_enter()
                        elif 'exit' in button_events:
                            b.mouse_exit()
                        else:
                            b.update()

            self.clock.tick(60)
            pygame.display.update()
            x = x+1
        pygame.quit()
        exit()

    def main_menu(self):
        print('Main Menu Starting')  # Debug Print

        menuM = 'sounds/music/menuAmbiance.wav'
        pygame.mixer.music.load(menuM)
        pygame.mixer.music.play(-1)
        gb_img = pygame.image.load('assets/menu_bg.png').convert_alpha()
        title_img = pygame.image.load('assets/title.png').convert_alpha()
        title_rotate_image = title_img
        rect = title_img.get_rect()
        button1_img = pygame.image.load('assets/button.png').convert_alpha()
        button2_img = button1_img.copy()
        button3_img = button1_img.copy()
        button1_hover = pygame.image.load(
            'assets/button_hover.png').convert_alpha()
        button2_hover = pygame.image.load(
            'assets/button_hover.png').convert_alpha()
        button3_hover = pygame.image.load(
            'assets/button_hover.png').convert_alpha()
        button_font = pygame.font.Font(
            './assets/fonts/Cheap_Pine_Sans.otf', 100)

        button1_rect = pygame.Rect(720, 420, 520, 170)
        button2_rect = pygame.Rect(720, 630, 520, 170)
        button3_rect = pygame.Rect(720, 840, 520, 170)
        play_button = PlayButton(button1_rect, "PLAY",
                                 button_font, button1_img, button1_hover)
        settings_button = SettingsButton(
            button2_rect, "CONTROLS", button_font, button2_img, button2_hover)
        exit_button = ExitButton(button3_rect, "EXIT",
                                 button_font, button3_img, button3_hover)
        all_buttons = [play_button, settings_button, exit_button]
        while self.menu:
            # render menu

            self.screen.blit(gb_img, (0, 0))
            self.screen.blit(title_img, (525, 60))
            for b in all_buttons:
                b.draw(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                    pygame.quit()
                    exit()
                elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEMOTION, pygame.MOUSEBUTTONUP):
                    for b in all_buttons:
                        button_events = b.handle_event(event)
                        if 'click' in button_events:
                            b.mouse_click(self)
                        elif 'enter' in button_events:
                            b.mouse_enter()
                        elif 'exit' in button_events:
                            b.mouse_exit()
                        else:
                            b.update()

            self.clock.tick(60)
            pygame.display.update()
        pygame.quit()
        exit()

    def character_select(self):
        print("Character Select")
        char_menu = True
        scene = Character_Scene(self)
        events_list = []
        while char_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    char_menu = False
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        char_menu = False
                        pygame.quit()
                        exit()
                else:
                    events_list.append(event)
            scene.ProcessInput(events_list, [])
            scene.Update()
            scene.Render(self.screen)
            if scene.canAdvance:
                char_menu = False
            self.clock.tick(60)
            pygame.display.update()
        self.main_loop()


"""Main Runner
Creates game object and runs the Game loop
"""
if __name__ == '__main__':
    game = Game()

    pygame.mixer.init(44100, -16, 2, 2048)

    game.main_menu()
    # game.main_loop()
