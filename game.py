import pygame
import os
from button import PlayButton, SettingsButton, ExitButton
from game_scenes import Hall_Scene, Room_Scene
from player import Player
from objects import Box
from interface import UI


class Game:
    """ Game Class that is the master to all other game content
    """

    """Game initializer

    Initializes pygame, the Screen, clock, room(s), and gets the scene list as of 2/13/2020
    """

    def __init__(self):
        os.environ['SDL_VIDEO_WINDOW_POS'] = "0,1"
        # os.environ['SDL_VIDEODRIVER'] = 'directx'
        self.WINDOW_SIZE = [1920, 1080]
        pygame.init()
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        # self.screen = pygame.display.set_mode(
        # self.WINDOW_SIZE, flags=pygame.FULLSCREEN | pygame.DOUBLEBUF)
        self.done = False
        self.clock = pygame.time.Clock()
        self.menu = True
        self.player = Player(self.screen)
        self.all_scenes = [
            ("Hallway", Hall_Scene(self.player, self.screen)),
            ("Room_Scene", Room_Scene(self.player, self.screen))
        ]
        self.scene_names = ["Hallway", "Room_Scene"]
        self.scene_num = 0
        self.current_scene = self.all_scenes[self.scene_num][1]
        self.collision_counter = 0

    """Main Game Loop

    Runs the game, initializes objects and logic.
    """

    def main_loop(self):

        my_group = pygame.sprite.Group(self.player)
        # hall = Hall_Scene(player, self.screen)
        user_interface = UI(self.screen, self.player, True)
        timechange = False
        # print(type(self.screen))
        while not self.done:
            sepia = False
            events = []
            quit_opt = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_opt = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        quit_opt = True
                    if event.key == pygame.K_RIGHT:
                        self.player.walking = True
                    if event.key == pygame.K_RETURN:
                        self.scene_num += 1
                        if self.scene_num == len(self.all_scenes):
                            self.scene_num = 0
                        self.current_scene.SwitchToScene(
                            self.all_scenes[self.scene_num][1])
                        self.current_scene = self.all_scenes[self.scene_num][1]
                        print(
                            f"Curr Scene {self.scene_num} : {self.current_scene}")
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.player.walking = False
                    if event.key == pygame.K_t:
                        # player.change_date()
                        user_interface.change_date()
                        timechange = True
                if quit_opt:
                    self.done = True
                else:
                    events.append(event)

            # if self.current_scene.box_onscreen and self.current_scene.collides and self.collision_counter < 1:
            #     # Hit the box, trigger the line
            #     self.collision_counter += 1
            #     # Should only print once
            #     print("Hit box")

            self.current_scene.ProcessInput(events, [])
            self.current_scene.Update()
            if self.player.details['Time'] == 1861:
                # Apply overlay
                sepia = True
            self.current_scene.Render(self.screen, sepia)
            my_group.update()
            my_group.draw(self.screen)
            user_interface.render()
            user_interface.update()

            pygame.display.flip()
            self.clock.tick(120)
        pygame.quit()
        exit()

    def main_menu(self):
        print('Main Menu Starting')  # Debug Print

        gb_img = pygame.image.load('assets/menu_bg.png')
        title_img = pygame.image.load('assets/title.png')
        title_rotate_image = title_img
        rect = title_img.get_rect()
        button1_img = pygame.image.load('assets/button.png')
        button2_img = button1_img.copy()
        button3_img = button1_img.copy()
        button1_hover = pygame.image.load('assets/button_hover.png')
        button2_hover = pygame.image.load('assets/button_hover.png')
        button3_hover = pygame.image.load('assets/button_hover.png')
        button_font = pygame.font.Font(
            './assets/fonts/Cheap_Pine_Sans.otf', 100)

        button1_rect = pygame.Rect(720, 420, 520, 170)
        button2_rect = pygame.Rect(720, 630, 520, 170)
        button3_rect = pygame.Rect(720, 840, 520, 170)
        play_button = PlayButton(button1_rect, "PLAY",
                                 button_font, button1_img, button1_hover)
        settings_button = SettingsButton(
            button2_rect, "SETTINGS", button_font, button2_img, button2_hover)
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
        # get and process events

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("Right, next scene")
                # self.room.get_next_scene()
                self.room.scroll_right = True
                # self.room.update_current_scene()

            elif event.key == pygame.K_LEFT:

                print("Left, previous scene")
                self.room.get_prev_scene()
            elif event.key == pygame.K_ESCAPE:
                self.done = True
        elif event.type == pygame.KEYUP:
            self.room.scroll_right = False

        else:
            # pass
            self.room.update_current_scene()


"""Main Runner
Creates game object and runs the Game loop
"""
if __name__ == '__main__':
    game = Game()
    game.main_menu()
    game.main_loop()
