import pygame
from room import Room


class Game:
    """ Game Class that is the master to all other game content
    """

    def __init__(self):
        WINDOW_SIZE = [640, 640]
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.done = False
        self.clock = pygame.time.Clock()
        self.room = Room(self.screen)
        self.scenes = self.room.scene_list

    def main_loop(self):
        print(self.room)
        pygame.time.set_timer(pygame.USEREVENT, 100)

        while not self.done:
            self.room.render_current_scene()
            for event in pygame.event.get():
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
            self.clock.tick(30)
            pygame.display.update()
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.main_loop()
