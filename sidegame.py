import pygame
from room import Room
from scene import Scene
alpha = (255, 0, 200)
class Game:
    """ Game Class that is the master to all other game content
    """

    """Game initializer

    Initializes pygame, the Screen, clock, room(s), and gets the scene list as of 2/13/2020
    """

    def __init__(self):
        self.WINDOW_SIZE = [1920, 1080]
        pygame.init()
        self.fullscreen = True
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE, pygame.FULLSCREEN)
        # pygame.display.toggle_fullscreen()
        self.done = False
        self.clock = pygame.time.Clock()
        self.background_scene = pygame.image.load('scene.png')
        self.scene = Scene(self.background_scene, self.screen)
        self.alpha = alpha
        # self.room = Room(self.screen)
        # self.scenes = self.room.scene_list
        # self.current_scene = None

    """Main Game Loop

    For now everything is in here, but methods may be created to clean up this code (2/13/2020)
    """

    def main_loop(self):
        # print(self.room)
        pygame.time.set_timer(pygame.USEREVENT, 150)

        chars = pygame.image.load('alphachar.png').convert()
        chars.set_colorkey(chars.get_at((0,0)))
        while not self.done:
            self.scene.render_scene()
            self.screen.blit(chars, (600, 300))
            for event in pygame.event.get():
                self.handle_event(event)
            self.clock.tick(30)
            pygame.display.update()
        pygame.quit()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.done = True
                # Bring up pause menu
            if event.key == pygame.K_F11:
                self.fullscreen = not self.fullscreen
                if self.fullscreen:
                    self.screen = pygame.display.set_mode(self.WINDOW_SIZE, pygame.FULLSCREEN)
                else:
                    self.screen = pygame.display.set_mode(self.WINDOW_SIZE, 0)
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         print("Right, next scene")
        #         self.room.get_next_scene()

        #     elif event.key == pygame.K_LEFT:

        #         print("Left, previous scene")
        #         self.room.get_prev_scene()
        # else:
        #     self.room.update_current_scene()


"""Main Runner
Creates game object and runs the Game loop
"""
if __name__ == '__main__':
    game = Game()
    game.main_loop()
