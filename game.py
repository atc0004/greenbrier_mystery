import pygame
from room import Room
import os
from button import Button


class Game:
    """ Game Class that is the master to all other game content
    """

    """Game initializer

    Initializes pygame, the Screen, clock, room(s), and gets the scene list as of 2/13/2020
    """

    def __init__(self):
        os.environ['SDL_VIDEO_WINDOW_POS'] = "0,1"
        self.WINDOW_SIZE = [1920, 1080]
        pygame.init()
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        self.done = False
        self.clock = pygame.time.Clock()
        self.room = Room(self.screen)
        self.scenes = self.room.scene_list

    """Main Game Loop

    For now everything is in here, but methods may be created to clean up this code (2/13/2020)
    """

    def main_loop(self):
        print(self.room)
        pygame.time.set_timer(pygame.USEREVENT, 100)

        while not self.done:
            self.room.render_current_scene()
            for event in pygame.event.get():
                self.handle_event(event)

            self.clock.tick(30)
            pygame.display.update()
        pygame.quit()

    def main_menu(self):
        print('Main Menu Starting')  # Debug Print
        main_menu = True
        gb_img = pygame.image.load('assets/menu_bg.PNG')
        title_img = pygame.image.load('assets/title.png')
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
        play_button = Button(button1_rect, "PLAY",
                             button_font, button1_img, button1_hover)
        settings_button = Button(
            button2_rect, "SETTINGS", button_font, button2_img, button2_hover)
        exit_button = Button(button3_rect, "EXIT",
                             button_font, button3_img, button3_hover)
        all_buttons = [play_button, settings_button, exit_button]
        # gb_image = pygame.transform
        while main_menu:
            # render menu

            self.screen.blit(gb_img, (0, 0))
            self.screen.blit(title_img, (525, 60))
            # self.screen.blit(button_img, (720,420))
            # play_button.draw(self.screen)
            # self.screen.blit(button_img, (720, 630))
            # self.screen.blit(button_img, (720, 840))
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
                            if b.text == "PLAY":
                                return
                            if b.text == "EXIT":
                                pygame.quit()
                                exit()
                            else:
                                print('click')
                        elif 'enter' in button_events:
                            b.update()
                        else:
                            b.update()

            self.clock.tick(60)
            # play_button.update()
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
                self.room.get_next_scene()
            elif event.key == pygame.K_LEFT:
                print("Left, previous scene")
                self.room.get_prev_scene()
        else:
            self.room.update_current_scene(event.type)


"""Main Runner
Creates game object and runs the Game loop
"""
if __name__ == '__main__':
    game = Game()
    game.main_menu()
    game.main_loop()
