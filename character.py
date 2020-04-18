import pygame
import os
class Character:
    def __init__(self, initial_position):
        self.walk = [pygame.transform.flip(pygame.image.load(os.path.join('assets/characters', 'boy_' + str(x) + '.png')), True, False) for x in range(1,4)]
        for x in self.walk:
            pygame.transform.flip(x, True, False)
        self.still = pygame.transform.flip(pygame.image.load(os.path.join('assets/characters', 'boy_2.png')), True, False)
        print(self.walk)
        self.pos_x = initial_position[0]
        self.pos_y = initial_position[1]
        self.walking = False
        self.walkcount = 0
    def draw(self, window):
        if self.walking:
            # self.pos_x +=10
            if self.walkcount > 4:
                self.walkcount = 0
            window.blit(self.walk[self.walkcount//2], (self.pos_x, self.pos_y))
            self.walkcount += 1
        else:
            self.walking = False
            window.blit(self.still, (self.pos_x, self.pos_y))