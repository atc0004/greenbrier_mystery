import pygame
from room import Room
import os

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
        button_img = pygame.image.load('assets/button.png')
        # gb_image = pygame.transform
        while main_menu:
            # render menu

            self.screen.blit(
                gb_img, (0, 0))
            self.screen.blit(title_img,(525, 60))
            self.screen.blit(button_img, (720,420))
            self.screen.blit(button_img, (720, 630))
            self.screen.blit(button_img, (720, 840))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                    pygame.quit()
            self.clock.tick(30)
            pygame.display.update()
        pygame.quit()
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
