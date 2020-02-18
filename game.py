import pygame
from room import Room


class Game:
    """ Game Class that is the master to all other game content
    """

    """Game initializer

    Initializes pygame, the Screen, clock, room(s), and gets the scene list as of 2/13/2020
    """

    def __init__(self):
        WINDOW_SIZE = [640, 640]
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.done = False
        self.clock = pygame.time.Clock()
        self.room = Room(self.screen)
        self.scenes = self.room.scene_list
        self.current_scene = None

    """Main Game Loop

    For now everything is in here, but methods may be created to clean up this code (2/13/2020)
    """

    def main_loop(self):
        print(self.room)
        pygame.time.set_timer(pygame.USEREVENT, 150)

        while not self.done:
            if self.current_scene != self.room.current_scene:
                self.room.render_current_scene()
                self.current_scene = self.room.current_scene

            for event in pygame.event.get():
                self.handle_event(event)
            self.clock.tick(30)
            pygame.display.update()
        pygame.quit()

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
            self.room.update_current_scene()


"""Main Runner
Creates game object and runs the Game loop
"""
if __name__ == '__main__':
    game = Game()
    game.main_loop()
